'''
Author: TheWarDoctor95
Other Contributors:
    Last Contribution By: Matsamilla - 10/20/20 - updated to not need imports

Description: Selects enemies to use the Provocation skill on.
    • Automatically selects an instrument if one is needed
    • Maintains a list of enemies that have been successfully been provoked together and will ignore enemies that have been provoked together
    • If one of the enemies that has already been provokd dies, the script will detect the death and free up the enemy that is still alive to be provoked again
    • Priority:
        1. PKs
        2. Paragons
        3. Enemies in War Mode
        4. Any other enemy
'''

## Script options ##
# Change depending on whether or not you want a more verbose output on what is being provoked or ignored by the script
showTargets = True

import re
from System.Collections.Generic import List
from System import Byte

journalEntryDelayMilliseconds = 200
targetClearDelayMilliseconds = 200
dragDelayMilliseconds = 600

enemiesProvodSharedValue = 'enemiesProvod'

pkFilter = Mobiles.Filter()
pkFilter.Enabled = True
pkFilter.RangeMax = 12
pkFilter.IsHuman = True
pkFilter.IsGhost = False
pkFilter.Friend = False
pkFilter.Notorieties = List[Byte](bytes([ 6 ]))

def GetEmptyMobileList( Mobiles ):
    '''
    Creates a filter that returns an empty list, and then returns the empty list
    '''
    emptyFilter = Mobiles.Filter()
    emptyFilter.Enabled = True
    emptyFilter.Name = 'there_is_no_way this_is someones_name_since_its_way_too_long'
    return Mobiles.ApplyFilter( emptyFilter )

class Notoriety:
    byte = Byte( 0 )
    color = ''
    description = ''

    def __init__ ( self, byte, color, description ):
        self.byte = byte
        self.color = color
        self.description = description

notorieties = {
    'innocent': Notoriety( Byte( 1 ), 'blue', 'innocent' ),
    'ally': Notoriety( Byte( 2 ), 'green', 'guilded/ally' ),
    'attackable': Notoriety( Byte( 3 ), 'gray', 'attackable but not criminal' ),
    'criminal': Notoriety( Byte( 4 ), 'gray', 'criminal' ),
    'enemy': Notoriety( Byte( 5 ), 'orange', 'enemy' ),
    'murderer': Notoriety( Byte( 6 ), 'red', 'murderer' ),
    'npc': Notoriety( Byte( 7 ), '', 'npc' )
}

def GetNotorietyList ( notorieties ):
    '''
    Returns a byte list of the selected notorieties
    '''
    notorietyList = []
    for notoriety in notorieties:
        notorietyList.append( notoriety.byte )

    return List[Byte]( notorietyList )

def GetEnemyNotorieties( minRange = 0, maxRange = 12 ):
    '''
    Returns a list of the common enemy notorieties
    '''
    global notorieties

    return GetNotorietyList( [
        notorieties[ 'attackable' ],
        notorieties[ 'criminal' ],
        notorieties[ 'enemy' ],
        notorieties[ 'murderer' ]
    ] )


def GetEnemies( Mobiles, minRange = 0, maxRange = 12, notorieties = GetEnemyNotorieties(), IgnorePartyMembers = True ):
    '''
    Returns a list of the nearby enemies with the specified notorieties
    '''

    if Mobiles == None:
        raise ValueError( 'Mobiles was not passed to GetEnemies' )

    enemyFilter = Mobiles.Filter()
    enemyFilter.Enabled = True
    enemyFilter.RangeMin = minRange
    enemyFilter.RangeMax = maxRange
    enemyFilter.Notorieties = notorieties
    enemyFilter.Friend = False
    enemyFilter.CheckIgnoreObject = True
    enemies = Mobiles.ApplyFilter( enemyFilter )

    if IgnorePartyMembers:
        partyMembers = [ enemy for enemy in enemies if enemy.InParty ]
        for partyMember in partyMembers:
            enemies.Remove( partyMember )

    return enemies

class myItem:
    name = None
    itemID = None
    color = None
    category = None
    weight = None

    def __init__ ( self, name, itemID, color, category, weight ):
        self.name = name
        self.itemID = itemID
        self.color = color
        self.category = category
        self.weight = weight


def FindItem( itemID, container, color = -1, ignoreContainer = [] ):
    '''
    Searches through the container for the item IDs specified and returns the first one found
    Also searches through any subcontainers, which Misc.FindByID() does not
    '''

    ignoreColor = False
    if color == -1:
        ignoreColor = True

    if isinstance( itemID, int ):
        foundItem = next( ( item for item in container.Contains if ( item.ItemID == itemID and ( ignoreColor or item.Hue == color ) ) ), None )
    elif isinstance( itemID, list ):
        foundItem = next( ( item for item in container.Contains if ( item.ItemID in itemID and ( ignoreColor or item.Hue == color ) ) ), None )
    else:
        raise ValueError( 'Unknown argument type for itemID passed to FindItem().', itemID, container )

    if foundItem != None:
        return foundItem

    subcontainers = [ item for item in container.Contains if ( item.IsContainer and not item.Serial in ignoreContainer ) ]
    for subcontainer in subcontainers:
        foundItem = FindItem( itemID, subcontainer, color, ignoreContainer )
        if foundItem != None:
            return foundItem
            
colors = {
    'green': 65,
    'cyan': 90,
    'orange': 43,
    'red': 1100,
    'yellow': 52
}

instruments = {
    'drum': myItem( 'drum', 0x0E9C, 0x0000, 'instrument', None ),
    'flute': myItem( 'flute', 0x2805, 0x0000, 'instrument', None ),
    'lute': myItem( 'lute', 0x0EB3, 0x0000, 'instrument', None ),

    # Harps
    'lap harp': myItem( 'lap harp', 0x0EB2, 0x0000, 'instrument', None ),
    'standing harp': myItem( 'standing harp', 0x0EB1, 0x0000, 'instrument', None ),

    # Tambourines
    'tambourine': myItem( 'tambourine', 0x0E9E, 0x0000, 'instrument', None ),
    'tambourine (tassle)': myItem( 'tambourine', 0x0E9D, 0x0000, 'instrument', None )
}

def FindInstrument( container ):
    '''
    Uses FindItem to look through the players backpack for an instrument
    '''
    global instruments

    instrumentIDs = [ instruments[ instrument ].itemID for instrument in instruments ]

    return FindItem( instrumentIDs, container )

def CheckPlayerInDungeon( Player ):
    '''
    Uses the Players X and Y coordinates to determine if they are in a dungeon
    '''

    if Player.Position.X < 5120:
        # Player is west of the dungeon cutoff
        return False

    if Player.Position.Y < 2305:
        # Player is east of the dungeon cutoff and to the north of the Lost Lands
        return True

    if Player.Position.X > 6140:
        # Player is east of the Lost Lands
        return True

    # Player is in the Lost Lands
    return False

def SelectEnemyToProvo( enemies ):
    '''
    Selects the nearest enemy who is not provoked to use Provocation on
    '''

    enemiesAlreadyProvod = None
    enemiesAlreadyProvodCheck = Misc.CheckSharedValue( enemiesProvodSharedValue )
    if enemiesAlreadyProvodCheck:
        enemiesAlreadyProvod = Misc.ReadSharedValue( enemiesProvodSharedValue )

        # Make sure the enemies we provoked previously are still around
        verifiedEnemiesAlreadyProvod = None
        enemySets = enemiesAlreadyProvod.split( ',' )
        for enemySet in enemySets:
            enemySerials = enemySet.split( '`' )
            bothEnemiesStillExist = True

            for enemySerial in enemySerials:
                enemyMobile = Mobiles.FindBySerial( int( enemySerial ) )
                if enemyMobile == None:
                    bothEnemiesStillExist = False

            if bothEnemiesStillExist and verifiedEnemiesAlreadyProvod == None:
                verifiedEnemiesAlreadyProvod = enemySet
            elif bothEnemiesStillExist:
                verifiedEnemiesAlreadyProvod += ',' + enemySet

        # Update the stored values
        enemiesAlreadyProvod = verifiedEnemiesAlreadyProvod
        if verifiedEnemiesAlreadyProvod == None:
            Misc.RemoveSharedValue( enemiesProvodSharedValue )
        else:
            Misc.SetSharedValue( enemiesProvodSharedValue, verifiedEnemiesAlreadyProvod )

    enemiesNotYetProvod = enemies
    if enemiesAlreadyProvod != None:
        # Remove the enemies we have already provoked from the list of potential enemies to provo
        enemiesAlreadyProvodSerials = []
        enemySets = enemiesAlreadyProvod.split( ',' )
        for enemySet in enemySets:
            enemySerials = enemySet.split( '`' )
            for enemy in enemySerials:
                enemiesAlreadyProvodSerials.append( int( enemy ) )

        enemiesNotYetProvodPythonList = list( filter( lambda enemy: enemy.Color == 1157 or not ( enemy.Serial in enemiesAlreadyProvodSerials ), enemies ) )

        # We have the Python formatted list, but we need a C# list to pass to Mobiles.Select()
        enemiesNotYetProvodCSharpList = GetEmptyMobileList( Mobiles )
        for enemy in enemiesNotYetProvodPythonList:
            enemiesNotYetProvodCSharpList.Add( enemy )
        enemiesNotYetProvod = enemiesNotYetProvodCSharpList

    # Make sure there are still enemies yet to be provod, if not, use all of the enemies given
    enemiesToProvo = enemiesNotYetProvod
    if len( enemiesToProvo ) == 0:
        enemiesToProvo = enemies

    # Select the enemy to provo
    paragons = [ enemy for enemy in enemiesToProvo if enemy.Color == 1157 ]
    if len( paragons ) > 0:
        paragonMobiles = GetEmptyMobileList( Mobiles )
        for paragon in paragons:
            paragonMobiles.Add( paragon )
        return Mobiles.Select( paragonMobiles, 'Nearest' )

    if not CheckPlayerInDungeon( Player ):
        # Make sure we are pulling enemies attacking and not birds or rabbits
        enemiesInWarMode = [ enemy for enemy in enemiesToProvo if enemy.WarMode ]
        if len( enemiesInWarMode ) > 0:
            warModeMobiles = GetEmptyMobileList( Mobiles )
            for enemyInWarMode in enemiesInWarMode:
                warModeMobiles.Add( enemyInWarMode )
            return Mobiles.Select( warModeMobiles, 'Nearest' )

    return Mobiles.Select( enemiesToProvo, 'Nearest' )


def ProvoEnemies():
    '''
    Identifies enemies that need to be provoked and uses the Provocation skill on them
    Having this encapsulated in a function makes it possible to use the 'return' keyword
    '''

    global showTargets

    Misc.ClearIgnore()

    provoAttemptCompleted = False

    while not provoAttemptCompleted:
        enemies = GetEnemies( Mobiles, 0, 12, GetEnemyNotorieties(), IgnorePartyMembers = True )
        #murderer = GetEnemies( Mobiles, 0, 12, 'murderer' , IgnorePartyMembers = True )

        if enemies == None or len( enemies ) < 2:
            Misc.SendMessage( 'Not enough enemies to provo!', colors[ 'red' ] )
            return
        else:
            # Clear any previously selected target and the target queue
            Target.ClearLastandQueue()

            # Wait for the target to finish clearing
            Misc.Pause( targetClearDelayMilliseconds )

            Player.UseSkill( 'Provocation' )

            # Wait for the journal entry to appear
            Misc.Pause( journalEntryDelayMilliseconds )

            if Journal.SearchByType( 'You must wait a few moments to use another skill.', 'Regular' ):
                # Something is on cooldown, nothing we can do
                Player.HeadMessage( 55, 'Skill Timer, try again')
                Journal.Clear()
                return
            elif Journal.SearchByType( 'What instrument shall you play?', 'Regular' ):
                instrument = FindInstrument( Player.Backpack )
                if instrument == None:
                    Misc.SendMessage( 'No instrument to provo with!', colors[ 'red' ] )
                    return
                Target.WaitForTarget( 2000, True )
                Target.TargetExecute( instrument )

            Target.WaitForTarget( 2000, True )
            enemyToProvo1 = SelectEnemyToProvo( enemies )
            Target.TargetExecute( enemyToProvo1 )

            # Wait for the journal entry to appear
            Misc.Pause( journalEntryDelayMilliseconds )

            if Journal.SearchByType( 'Target cannot be seen', 'Regular' ):
                if showTargets:
                    Mobiles.Message( enemyToProvo1, colors[ 'red' ], 'Target 1 cannot be seen' )
                Misc.IgnoreObject( enemyToProvo1 )
                Journal.Clear()
                provoAttemptCompleted = False
                Misc.Pause( 1000 )
                continue

            # Remove the selected enemy to ensure we don not provo an enemy onto themselves
            enemies.Remove( enemyToProvo1 )
            
            pkscan = Mobiles.ApplyFilter( pkFilter )
            pk = Mobiles.Select( pkscan , 'Nearest' )
            

            Target.WaitForTarget( 2000, True )
            if pk:
                Target.TargetExecute(pk)
                Player.HeadMessage( 33 , 'Provo on ' + pk.Name)
                Target.SetLast(pk)
            else:
                enemyToProvo2 = SelectEnemyToProvo( enemies )
                Target.TargetExecute( enemyToProvo2 )

            # Wait for the journal entry to appear
            Misc.Pause( journalEntryDelayMilliseconds )

            if Journal.SearchByType( 'Target cannot be seen', 'Regular' ):
                if showTargets:
                    Mobiles.Message( enemyToProvo2, colors[ 'red' ], 'Target 2 cannot be seen' )
                Misc.IgnoreObject( enemyToProvo2 )
                Journal.Clear()
                provoAttemptCompleted = False
                Misc.Pause( 1000 )
                continue

            if showTargets:
                Mobiles.Message( enemyToProvo1, colors[ 'cyan' ], 'Provo Target 1' )
                Mobiles.Message( enemyToProvo2, colors[ 'cyan' ], 'Provo Target 2' )

            # Wait for the journal entry to appear
            Misc.Pause( journalEntryDelayMilliseconds )

            if Journal.SearchByType( 'Your music succeeds, as you start a fight.', 'Regular' ):
                Journal.Clear()
                newEntry = '%i`%i' % ( enemyToProvo1.Serial, enemyToProvo2.Serial )
                enemiesAlreadyProvodCheck = Misc.CheckSharedValue( enemiesProvodSharedValue )
                if enemiesAlreadyProvodCheck:
                    enemiesAlreadyProvod = Misc.ReadSharedValue( enemiesProvodSharedValue )
                    Misc.SetSharedValue( enemiesProvodSharedValue, enemiesAlreadyProvod + ',' + newEntry )
                else:
                    Misc.SetSharedValue( enemiesProvodSharedValue, newEntry )
            provoAttemptCompleted = True

# Run ProvoEnemies
ProvoEnemies()
