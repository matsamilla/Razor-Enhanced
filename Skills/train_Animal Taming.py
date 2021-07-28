'''
Author: Aga - original author of the uosteam script
Other Contributors: TheWarDoctor95 - converted to Razor Enhanced script
                    MatsaMilla - Converted to be all-in-1 script
Last Contribution By: MatsaMilla - 7/27/21
Description: Tames nearby animals to train Animal Taming to GM
'''

########## Script options ###############
# True to kill tame, false to not
killTame = False
# Change to the name that you want to rename the tamed animals to
if killTame:
    renameTamedAnimalsTo = 'kill me'
    killList = []
else:
    renameTamedAnimalsTo = 'Thanks Matsa'
    
# Change to the number of followers you would like to keep.
# The script will auto-release the most recently tamed animal if the follower number exceeds this number
# Some animals have a follower count greater than one, which may cause them to be released if this number is not set high enough
numberOfFollowersToKeep = 1

# Set to the maximum number of times to attempt to tame a single animal. 0 == attempt until tamed
maximumTameAttempts = 10

# Set the minimum taming difficulty to use when finding animals to tame
minimumTamingDifficulty = 31

# Set this to how you would like to heal your character if they take damage
# Options are:
# 'Healing' = use bandages (you should just use my Bandage_Self.py instead)
# 'Magery' = uses the Heal and Greater Heal ability depending on how much health is missing
# 'None' = do not auto-heal
healUsing = 'None'

# True or False to use Peacemaking if needed
enablePeacemaking = True

# True or False to track the animal being tamed
enableFollowAnimal = True

# Change depending on the latency to your UO shard
journalEntryDelayMilliseconds = 100
targetClearDelayMilliseconds = 600

################ END SETUP SECTION ######################
import sys

if not Misc.CurrentScriptDirectory() in sys.path:
    sys.path.append(Misc.CurrentScriptDirectory())

from System.Collections.Generic import List
from System import Byte
import math

noAnimalsToTrainTimerMilliseconds = 10000
playerStuckTimerMilliseconds = 5000
catchUpToAnimalTimerMilliseconds = 20000
animalTamingTimerMilliseconds = 12500
peacemakingTimerMilliseconds = 5000
bandageTimerMilliseconds = 10000

if Player.GetRealSkillValue('Animal Taming') < 35:
    Misc.SendMessage('Buy Taming Skill Up, stopping', 33)
    sys.exit()
    
from System.Collections.Generic import List

class Animal:
    name = ''
    mobileID = 0
    color = 0
    minTamingSkill = -1
    maxTamingSkill = -1
    packType = None

    def __init__ ( self, name, mobileID, color, minTamingSkill, maxTamingSkill, packType ):
        self.name = name
        self.mobileID = mobileID
        self.color = color
        self.minTamingSkill = minTamingSkill
        self.maxTamingSkill = maxTamingSkill

animals = {
    # Organized based on taming difficulty with no previous owners according to uo.com, then alphabetically by and within species
    # https://uo.com/wiki/ultima-online-wiki/skills/animal-taming/tameable-creatures/#mobs

    ### Min skill 0, Max skill 10 ###
    'dog': Animal( 'dog', 0x00D9, 0x0000, 0, 10, [ 'canine' ] ),
    'gorilla': Animal( 'gorilla', 0x001D, 0x0000, 0, 10, None ),
    'parrot': Animal( 'parrot', 0x033F, 0x0000, 0, 10, None ),

    # Rabbits
    'rabbit (brown)': Animal( 'rabbit', 0x00CD, 0x0000, 0, 10, None ),
    'rabbit (black)': Animal( 'rabbit', 0x00CD, 0x090E, 0, 10, None ),
    'jack rabbit': Animal( 'jack rabbit', 0x00CD, 0x01BB, 0, 10, None ),

    'skittering hopper': Animal( 'skittering hopper', 0x012E, 0x0000, 0, 10, None ),
    'squirrel': Animal( 'squirrel', 0x0116, 0x0000, 0, 10, None ),


    ### Min skill 0, Max skill 20 ###
    'mongbat': Animal( 'mongbat', 0x0027, 0x0000, 0, 20, None ),


    ### Min skill 10, Max skill 20 ###
    # Birds
    # Note: the following share a color code:
    # 0x0835: Finch, hawk
    # 0x0847: Tern, Towhee
    # 0x0851: Nuthatch, woodpecker
    # 0x0901: Crow, Magpie, raven
    'chickadee': Animal( 'chickadee', 0x0006, 0x0840, 10, 20, None ),
    'crossbill': Animal( 'crossbill', 0x0006, 0x083A, 10, 20, None ),
    'crow': Animal( 'crow', 0x0006, 0x0901, 10, 20, None ),
    'finch': Animal( 'finch', 0x0006, 0x0835, 10, 20, None ),
    'hawk': Animal( 'hawk', 0x0006, 0x0835, 10, 20, None ),
    'kingfisher': Animal( 'kingfisher', 0x0006, 0x083F, 10, 20, None ),
    'lapwing': Animal( 'lapwing', 0x0006, 0x0837, 10, 20, None ),
    'magpie': Animal( 'magpie', 0x0006, 0x0901, 10, 20, None ),
    'nuthatch': Animal( 'nuthatch', 0x0006, 0x0851, 10, 20, None ),
    'plover': Animal( 'plover', 0x0006, 0x0847, 10, 20, None ),
    'raven': Animal( 'raven', 0x0006, 0x0901, 10, 20, None ),
    'skylark': Animal( 'skylark', 0x0006, 0x083C, 10, 20, None ),
    'starling': Animal( 'starling', 0x083E, 0x0845, 10, 20, None ),
    'swift': Animal( 'swift', 0x0006, 0x0845, 10, 20, None ),
    'tern': Animal( 'tern', 0x0006, 0x0847, 10, 20, None ),
    'towhee': Animal( 'towhee', 0x0006, 0x0847, 10, 20, None ),
    'woodpecker': Animal( 'woodpecker', 0x0006, 0x0851, 10, 20, None ),
    'wren': Animal( 'wren', 0x0006, 0x0850, 10, 20, None ),

    'cat': Animal( 'cat', 0x00C9, 0x0000, 10, 20, [ 'feline' ] ),
    'chicken': Animal( 'chicken', 0x00D0, 0x0000, 10, 20, None ),
    'mountain goat': Animal( 'mountain goat', 0x0058, 0x0000, 10, 20, None ),
    'rat': Animal( 'rat', 0x00EE, 0x0000, 10, 20, None ),
    'sewer rat': Animal( 'sewer rat', 0x00EE, 0x0000, 10, 20, None ),


    ### Min skill 20, Max skill 30 ###
    'cow (brown)': Animal( 'cow', 0x00E7, 0x0000, 20, 30, None ),
    'cow (black)': Animal( 'cow', 0x00D8, 0x0000, 20, 30, None ),
    'goat': Animal( 'goat', 0x00D1, 0x0000, 20, 30, None ),
    'pig': Animal( 'pig', 0x00CB, 0x0000, 20, 30, None ),
    'sheep': Animal( 'sheep', 0x00CF, 0x0000, 20, 30, None ),


    ### Min skill 20, Max skill 50 ###
    'giant beetle': Animal( 'giant beetle', 0x0317, 0x0000, 20, 50, None ),
    'slime': Animal( 'slime', 0x0033, 0x0000, 20, 50, None ),


    ### Min skill 30, Max skill 40 ###
    'eagle': Animal( 'eagle', 0x0005, 0x0000, 30, 40, None ),
    'bouraRuddy': None, # Not on UO Forever


    ### Min skill 40, Max skill 50 ###
    'boar': Animal( 'boar', 0x0122, 0x0000, 40, 50, None ),
    'bullfrog': Animal( 'bullfrog', 0x0051, 0x0000, 40, 50, None ),
    'lowland boura': None, # Not on UO Forever
    'ferret': Animal( 'ferret', 0x0117, 0x0000, 40, 50, None ),
    'giant rat': Animal( 'giant rat', 0x00D7, 0x0000, 40, 50, None ),
    'hind': Animal( 'hind', 0x00ED, 0x0000, 40, 50, None ),

    # Horses
    'horse': Animal( 'horse', 0x00C8, 0x0000, 40, 50, None ),
    'horse2': Animal( 'horse', 0x00E2, 0x0000, 40, 50, None ),
    'horse3': Animal( 'horse', 0x00CC, 0x0000, 40, 50, None ),
    'horse4': Animal( 'horse', 0x00E4, 0x0000, 40, 50, None ),
    'horsePack': Animal( 'pack horse', 0x0123, 0x0000, 40, 50, None ),
    'horsePalomino': None,
    'horseWar': None,

    # Llamas
    'pack llama': Animal( 'pack llama', 0x0124, 0x0000, 40, 50, None ),
    'llamaRideable': None,

    # Ostards
    'ostard': Animal( 'desert ostard', 0x00D2, 0x0000, 40, 50, [ 'ostard' ] ),
    'forest ostard (green)': Animal( 'forest ostard', 0x00DB, 0x88A0, 40, 50, [ 'ostard' ] ),
    'forest ostard (red)': Animal( 'forest ostard', 0x00DB, 0x889D, 40, 50, [ 'ostard' ] ),

    'timber wolf': Animal( 'timber wolf', 0x00E1, 0x0000, 40, 50, [ 'canine' ] ),
    'rideable wolf': Animal( 'rideable wolf', 0x0115, 0x0000, 40, 50, [ 'canine' ] ),


    ### Min skill 50, Max skill 60 ###
    'black bear': Animal( 'black bear', 0x00D3, 0x0000, 50, 60, [ 'bear' ] ),
    'polar bear': Animal( 'polar bear', 0x00D5, 0x0000, 50, 60, [ 'bear' ] ),
    'deathwatch beetle': None,
    'llama': Animal( 'llama', 0x00DC, 0x0000, 50, 60, None ),
    'walrus': Animal( 'walrus', 0x00DD, 0x0000, 50, 60, None ),


    ### Min skill 60, Max skill 70 ###
    'alligator': Animal( 'alligator', 0x00CA, 0x0000, 60, 70, None ),
    'brown bear': Animal( 'brown bear', 0x00A7, 0x0000, 60, 70, [ 'bear' ] ),
    'high plains boura': None, # Not on UO Forever
    'cougar': Animal( 'cougar', 0x003F, 0x0000, 60, 70, [ 'feline' ] ),
    'paralithode': None, # Not on UO Forever
    'scorpion': Animal( 'scorpion', 0x0030, 0x0000, 60, 70, None ),


    ### Min skill 70, Max skill 80 ###
    'rideable polar bear': Animal( 'rideable polar bear', 0x00D5, 0x0000, 70, 80, [ 'bear' ] ),
    'grizzly bear': Animal( 'grizzly bear', 0x00D4, 0x0000, 70, 80, [ 'bear' ] ),
    'young dragon': Animal( 'young dragon', 0x003C, 0x0000, 70, 80, None ),
    'great hart': Animal( 'great hart', 0x00EA, 0x0000, 70, 80, None ),
    'snow leopard': Animal( 'snow leopard', 0x0040, 0x0000, 70, 80, [ 'feline' ] ),
    'snow leopard2': Animal( 'snow leopard', 0x0041, 0x0000, 70, 80, [ 'feline' ] ),
    'panther': Animal( 'panther', 0x00D6, 0x0000, 70, 80, [ 'feline' ] ),
    'snake': Animal( 'snake', 0x0034, 0x0000, 70, 80, None ),
    'giant spider': Animal( 'giant spider', 0x001C, 0x0000, 70, 80, None ),
    'grey wolf (light grey)': Animal( 'grey wolf', 0x0019, 0x0000, 70, 80, [ 'canine' ] ),
    'grey wolf (dark grey)': Animal( 'grey wolf', 0x001B, 0x0000, 70, 80, [ 'canine' ] ),


    ### Min skill 80, Max skill 90 ###
    'gaman': None,
    'slithStone': None,
    'white wolf (dark grey)': Animal( 'white wolf', 0x0022, 0x0000, 80, 90, [ 'canine' ] ),
    'white wolf (light grey)': Animal( 'white wolf', 0x0025, 0x0000, 80, 90, [ 'canine' ] ),


    ### Min skill 90, Max skill 100 ###
    'bull (solid, brown)': Animal( 'bull', 0x00E8, 0x0000, 90, 100, [ 'bull' ] ),
    'bull (solid, black)': Animal( 'bull', 0x00E8, 0x0901, 90, 100, [ 'bull' ] ),
    'bull (spotted, brown)': Animal( 'bull', 0x00E9, 0x0000, 90, 100, [ 'bull' ] ),
    'bull (spotted, black)': Animal( 'bull', 0x00E9, 0x0901, 90, 100, [ 'bull' ] ),
    'foxBlood': None,
    'hellcat (small)': Animal( 'hellcat', 0x00C9, 0x0647, 90, 100, [ 'feline' ] ),
    'mongbatGreater': None,
    'frenzied ostard': Animal( 'frenzied ostard', 0x00DA, 0x0000, 90, 100, [ 'ostard' ] ),
    'osseinRam': None,
    'frost spider': Animal( 'frost spider', 0x0014, 0x0000, 90, 100, None ),
    'giant toad': Animal( 'giant toad', 0x0050, 0x0000, 90, 100, None ),
    'unicorn': None,
    'giant ice worm': Animal( 'giant ice worm', 0x0050, 0x0000, 90, 100, None ),


    ### Min skill 100, Max skill 110 ###
    # Drakes
    # pathaleo drake: 0x003C
    'drake (brown)': Animal( 'drake', 0x003C, 0x0000, 100, 110, None ),
    'drake (red)': Animal( 'drake', 0x003D, 0x0000, 100, 110, None ),
    'drakeCrimson': None,
    'drakePlatinum': None,
    'drakeStygian': None,

    'hellcat (large)': Animal( 'hellcat', 0x007F, 0x0000, 100, 110, [ 'feline' ] ),
    'hellhound': Animal( 'hellhound', 0x0062, 0x0000, 100, 110, [ 'canine' ] ),
    'imp': Animal( 'imp', 0x004A, 0x0000, 100, 110, [ 'daemon' ] ),
    'kitsuneBake': None,
    'lava lizard': Animal( 'lava lizard', 0x00CE, 0x0000, 100, 110, None ),

    # ridgebacks
    'ridgeback': Animal( 'ridgeback', 0x00BB, 0x0000, 100, 110, None ),
    'savage ridgeback': Animal( 'savage ridgeback', 0x00BC, 0x0000, 100, 110, None ),

    'slith': None,
    'dire wolf': Animal( 'dire wolf', 0x0017, 0x0000, 100, 110, [ 'canine' ] ),


    ### Min skill 110, Max skill 120 ###
    'beetleDeath': None,
    'beetleFire': None,
    'rune beetle': Animal( 'rune beetle', 0x00F4, 0x0000, 110, 120, None ),

    'dragon': Animal( 'dragon', 0x003B, 0x0000, 110, 120, None ),
    'dragonSwamp': None,
    'dragonWater': None,
    'dragonDeepWater': None,

    'drakeCold': None,

    'hiryu': None,
    'hiryuLesser': None,

    'lion': None,
    'kiRin': None,
    'nightbear': None,
    'nightdragon': None,
    'nightfrenzy': None,
    'nightmare': None,
    'nightllama': None,
    'nightridge': None,
    'nightwolf': None,
    'skree': None,
    'dread spider': Animal( 'dread spider', 0x000B, 0x0000, 110, 120, None ),
    'unicorn': None,
    'wolfTsuki': None,
    'white wyrm': Animal( 'white wyrm', 0x00B4, 0x0000, 110, 120, None ),


    ### Challenging ###
    'cuSidhe': None,

    'dimetrosaur': None, # Not on UO Forever

    # Dragons
    'dragonBane': None,
    'dragonFrost': None,
    'a greater dragon': None, #0x000C
    'dragonSerpentine': None,

    'gallusaurus': None,

    # Horses
    'steedFire': None, # Pack type: Daemon, Equine
    'steedSkeletal': None, # Pack type: Daemon, Equine
    'horseDreadWar': None,

    'miteFrost': None,
    'najasaurus': None, # Not on UO Forever
    'phoenix': None,
    'raptor': None, # Pack type: Raptor
    'reptalon': None, # Not on UO Forever
    'saurosurus': None, # Not on UO Forever

    # Tigers
    'tigerWild': None,
    'tigerSabreToothed': None,

    'triceratops': None, # Not on UO Forever
    'turtleHatchlingDragon': None,
    'wolfDragon': None,
    'shadow wyrm': Animal( 'shadow wyrm', 0x006A, 0x0000, 120, 120, None )
}


def GetAnimalIDsAtOrOverTamingDifficulty( minimumTamingDifficulty ):
    '''
    Looks through the list of tameables for animals at or over the minimum taming level
    '''
    global animals

    animalList = List[int]()
    for animal in animals:
        if ( not animals[ animal ] == None and
                not animalList.Contains( animals[ animal ].mobileID ) and
                animals[ animal ].minTamingSkill >= minimumTamingDifficulty ):
            animalList.Add( animals[ animal ].mobileID )

    return animalList


def FindAnimalToTame():
    '''
    Finds the nearest tameable animal nearby
    '''
    global renameTamedAnimalsTo
    global minimumTamingDifficulty

    animalFilter = Mobiles.Filter()
    animalFilter.Enabled = True
    animalFilter.Bodies = GetAnimalIDsAtOrOverTamingDifficulty( minimumTamingDifficulty )
    animalFilter.RangeMin = 0
    animalFilter.RangeMax = 12
    animalFilter.IsHuman = 0
    animalFilter.IsGhost = 0
    animalFilter.CheckLineOfSite = True
    animalFilter.Friend = False
    animalFilter.CheckIgnoreObject = True

    tameableMobiles = Mobiles.ApplyFilter( animalFilter )

    # Exclude animals that have already been tamed by this player
    tameableMobilesTemp = tameableMobiles[:]
    for tameableMobile in tameableMobiles:
        if tameableMobile.Name == renameTamedAnimalsTo:
            tameableMobilesTemp.Remove( tameableMobile )

    tameableMobiles = tameableMobilesTemp

    if len( tameableMobiles ) == 0:
        return None
    elif len( tameableMobiles ) == 1:
        return tameableMobiles[ 0 ]
    else:
        return Mobiles.Select( tameableMobiles, 'Nearest' )


def PlayerWalk( direction ):
    '''
    Moves the player in the specified direction
    '''

    playerPosition = Player.Position
    if Player.Direction == direction:
        Player.Walk( direction )
    else:
        Player.Walk( direction )
        Player.Walk( direction )
    return
    


def FollowMobile( mobile, maxDistanceToMobile = 2, startPlayerStuckTimer = False ):
    '''
    Uses the X and Y coordinates of the animal and player to follow the animal around the map
    Returns True if player is not stuck, False if player is stuck
    '''

    if not Timer.Check( 'catchUpToAnimalTimer' ):
        return False

    mobilePosition = mobile.Position
    playerPosition = Player.Position
    directions = []
    if mobilePosition.X > playerPosition.X and mobilePosition.Y > playerPosition.Y:
        directions.append( 'Down' )
    if mobilePosition.X < playerPosition.X and mobilePosition.Y > playerPosition.Y:
        directions.append( 'Left' )
    if mobilePosition.X > playerPosition.X and mobilePosition.Y < playerPosition.Y:
        directions.append( 'Right' )
    if mobilePosition.X < playerPosition.X and mobilePosition.Y < playerPosition.Y:
        directions.append( 'Up' )
    if mobilePosition.X > playerPosition.X and mobilePosition.Y == playerPosition.Y:
        directions.append( 'Down' )
        directions.append( 'Right' )
    if mobilePosition.X < playerPosition.X and mobilePosition.Y == playerPosition.Y:
        directions.append( 'Up' )
        directions.append( 'Left' )
    if mobilePosition.X == playerPosition.X and mobilePosition.Y > playerPosition.Y:
        directions.append( 'Down' )
        directions.append( 'Left' )
    if mobilePosition.X == playerPosition.X and mobilePosition.Y < playerPosition.Y:
        directions.append( 'Up' )
        directions.append( 'Right' )

    if startPlayerStuckTimer:
        Timer.Create( 'playerStuckTimer', playerStuckTimerMilliseconds )

    playerPosition = Player.Position
    for direction in directions:
        PlayerWalk( direction )

    newPlayerPosition = Player.Position
    if playerPosition == newPlayerPosition and not Timer.Check( 'playerStuckTimer' ):
        # Player has been stuck in the same position for a while, try to find them a way out of the stuck position
        if Player.Direction == 'Up':
            for i in range ( 5 ):
                Player.Walk( 'Down' )
        elif Player.Direction == 'Down':
            for i in range( 5 ):
                Player.Walk( 'Up' )
        elif Player.Direction == 'Right':
            for i in range( 5 ):
                Player.Walk( 'Left' )
        elif Player.Direction == 'Left':
            for i in range( 5 ):
                Player.Walk( 'Right' )
        Timer.Create( 'playerStuckTimer', playerStuckTimerMilliseconds )
    elif playerPosition != newPlayerPosition:
        Timer.Create( 'playerStuckTimer', playerStuckTimerMilliseconds )

    if Player.DistanceTo( mobile ) > maxDistanceToMobile:
        # This pause may need further tuning
        # Don't want to create a ton of infinite calls if the player is stuck, but also don't want to not be able to catch up to animals
        Misc.Pause( 100 )
        FollowMobile( mobile, maxDistanceToMobile )
        #pathfindToMobile( mobile )

    return True
        
def pathfindToMobile(mobile):
    mobilePosition = mobile.Position
    mobileCoords = PathFinding.Route()
    mobileCoords.MaxRetry = 5
    mobileCoords.StopIfStuck = True
    mobileCoords.UseResync = True
    mobileCoords.X = mobilePosition.X - 1
    mobileCoords.Y = mobilePosition.Y

    if PathFinding.Go(mobileCoords):
        Misc.SendMessage('First Try')
        Misc.NoOperation()
    else:
        mobileCoords.X = mobilePosition.X + 1
        if PathFinding.Go(mobileCoords):
            Misc.SendMessage('Second Try')
            Misc.NoOperation()
        else:
            mobileCoords.X = mobilePosition.X
            mobileCoords.Y = mobilePosition.Y - 1
            if PathFinding.Go(mobileCoords):
                Misc.SendMessage('Third Try')
                Misc.NoOperation()
            else:
                mobileCoords.Y = mobilePosition.Y + 1
                PathFinding.Go(mobileCoords)
                Misc.SendMessage('Last Try')

def makePeace():
    enemyFilter = Mobiles.Filter()
    enemyFilter.Enabled = True
    enemyFilter.CheckIgnoreObject = False
    enemyFilter.Notorieties = GetEnemyNotorieties()
    enemyFilter.RangeMin = 0
    enemyFilter.RangeMax = 12
    enemyFilter.Friend = False
    enemies = Mobiles.ApplyFilter( enemyFilter )

    enemyAtWar = False
    enemyToPutToPeace = None
    for enemy in enemies:
        if enemy.WarMode:
            enemyAtWar = True
            enemyToPutToPeace = enemy
            break

    #Timer.Create( 'peacemakingTimer', 1 )
    #Timer.Create( 'skillTimer', 1 )
    while enemyAtWar:
        #if not Timer.Check( 'peacemakingTimer' ):
        if not Timer.Check( 'skillTimer' ):
            try:
                enemyToPutToPeace = Mobiles.FindBySerial(enemyToPutToPeace.Serial)
                if enemyToPutToPeace == None or enemyToPutToPeace.WarMode == False :
                    break
                
                # Clear any previously selected target and the target queue
                Target.ClearLastandQueue()
                # Wait for the target to finish clearing
                Misc.Pause( targetClearDelayMilliseconds )

                Player.UseSkill( 'Peacemaking' )
                # Wait for journal entry to come up
                Misc.Pause( journalEntryDelayMilliseconds )
                if Journal.SearchByType( 'What instrument shall you play?', 'System' ):
                    instrument = findInstrument()
                    if instrument == None:
                        Misc.SendMessage( 'No instruments to peacemake with.', 1100 )
                        break
                    else:
                        Target.WaitForTarget( 2000, False )
                        Target.TargetExecute( instrument.Serial )

                if Journal.SearchByType( 'Whom do you wish to calm?', 'System' ):
                    Target.WaitForTarget( 2000, False )
                    Target.TargetExecute( enemyToPutToPeace )
                    #Timer.Create( 'peacemakingTimer', peacemakingTimerMilliseconds )
                    Timer.Create( 'skillTimer', peacemakingTimerMilliseconds )

                enemyAtWar = False
                enemyToPutToPeace = None
#                for enemy in enemies:
#                    if enemy.WarMode:
#                        enemyAtWar = True
#                        enemyToPutToPeace = enemy
#                        break
            except:
                break

        # Wait a little bit so that the while loop does not consume as much CPU
        Misc.Pause( 50 )
        if killTame == False:
            if Player.WarMode:
                Player.SetWarMode( False )

def heal():           
    if healUsing != 'None':
        if healUsing == 'Healing' and not Timer.Check( 'bandageTimer' ):
            # Clear any previously selected target and the target queue
            Target.ClearLastandQueue()
            # Wait for the target to finish clearing
            Misc.Pause( targetClearDelayMilliseconds )

            bandage = Items.FindByID(0x0E21, 0, Player.Backpack.Serial)
            Items.UseItem( bandage )
            Target.WaitForTarget(1500)
            Target.Self()

            Timer.Create( 'bandageTimer', bandageTimerMilliseconds )
        elif healUsing == 'Magery':
            if ( Player.HitsMax - Player.Hits ) > 30:
                if not Target.HasTarget():
                    if Player.Poisoned:
                        Spells.CastMagery('Cure')
                        Target.WaitForTarget(1500)
                        Target.Self()
                        Misc.Pause(500)
                    else:
                        Spells.CastMagery('Greater Heal')
                        Target.WaitForTarget(1500)
                        Target.Self()
                        Misc.Pause(500)
            elif ( Player.HitsMax - Player.Hits ) > 10:
                if not Target.HasTarget():
                    if Player.Poisoned:
                        Spells.CastMagery('Cure')
                        Target.WaitForTarget(1500)
                        Target.Self()
                        Misc.Pause(500)
                    else:
                        Spells.CastMagery('Heal')
                        Target.WaitForTarget(1500)
                        Target.Self()
                        Misc.Pause(500)
            
def TrainAnimalTaming():
    '''
    Trains Animal Taming to GM
    '''

    # User variables
    global renameTamedAnimalsTo
    global numberOfFollowersToKeep
    global maximumTameAttempts
    global enablePeacemaking
    global enableFollowAnimal
    global journalEntryDelayMilliseconds
    global targetClearDelayMilliseconds

    # Script variables
    global noAnimalsToTrainTimerMilliseconds
    global playerStuckTimerMilliseconds
    global catchUpToAnimalTimerMilliseconds
    global animalTamingTimerMilliseconds
    global peacemakingTimerMilliseconds
    global bandageTimerMilliseconds

    if Player.GetRealSkillValue( 'Animal Taming' ) == Player.GetSkillCap( 'Animal Taming' ):
        Misc.SendMessage( 'You\'ve already maxed out Animal Taming!', 65 )
        return

    # Initialize variables
    animalBeingTamed = None
    tameHandled = False
    tameOngoing = False
    timesTried = 0
    bandageBeingApplied = False

    # Initialize skill timers
#    Timer.Create( 'animalTamingTimer', 1 )
#    if enablePeacemaking:
#        Timer.Create( 'peacemakingTimer', 1 )

    if healUsing == 'Healing':
        Timer.Create( 'bandageTimer', 1 )
    elif healUsing == 'Magery':
        Timer.Create( 'healSpellTimer', 1 )

    # Initialize the journal and ignore object list
    Journal.Clear()
    Misc.ClearIgnore()

    # Toggle war mode to make sure the player isn not going to kill the animal being tamed
    if killTame == False:
        Player.SetWarMode( True )
        Player.SetWarMode( False )

    while not Player.IsGhost:
        
        if not maximumTameAttempts == 0 and timesTried > maximumTameAttempts:
            if killTame:
                Mobiles.Message( animalBeingTamed, 1100, 'Tried more than %i times to tame. Killing animal' % maximumTameAttempts )
                Player.Attack( animalBeingTamed )
                Misc.Pause(600)
                Misc.IgnoreObject( animalBeingTamed )
            else:
                Mobiles.Message( animalBeingTamed, 1100, 'Tried more than %i times to tame. Ignoring animal' % maximumTameAttempts )
                Misc.IgnoreObject( animalBeingTamed )
            animalBeingTamed = None
            timesTried = 0


        if enablePeacemaking:
            makePeace()
            
        if Player.Hits != Player.HitsMax:
            heal()

        # If there is no animal being tamed, try to find an animal to tame
        if animalBeingTamed == None:
            animalBeingTamed = FindAnimalToTame()
            if animalBeingTamed == None:
                # No animals in the area. Pause for a while so that this is constantly running until something is available to tame
                Misc.Pause( 1000 )
                continue
            else:
                Mobiles.Message( animalBeingTamed, 90, 'Found animal to tame' )

        # Check if animal is close enough to tame
        if Player.DistanceTo( animalBeingTamed ) > 12:
            Misc.SendMessage( 'Animal moved too far away, ignoring for now', 1100  )
            animalBeingTamed = None
            continue
        elif animalBeingTamed != None and Player.DistanceTo( animalBeingTamed ) > 1:
            if enableFollowAnimal:
                Timer.Create( 'catchUpToAnimalTimer', catchUpToAnimalTimerMilliseconds )
                playerStuck = not FollowMobile( animalBeingTamed, 2, True )
                if playerStuck:
                    Player.HeadMessage( 1100, 'Player stuck!' )
                    return
            elif Timer.Check('notclose') == False:
                while Player.DistanceTo( animalBeingTamed ) > 2:
                    if enablePeacemaking:
                        makePeace()
                    if Timer.Check('notclose') == False:
                        Mobiles.Message( animalBeingTamed, 34, 'Not close enough!' )
                        Timer.Create('notclose', 2000)
                    Misc.Pause( 500 )

        # If peacemaking is enabled, make sure the animal being tamed is calm
        if enablePeacemaking:
            makePeace()

        # Tame the animal if a tame is not currently being attempted and enough time has passed since last using Animal Taming
#        if not tameOngoing and not Timer.Check( 'animalTamingTimer' ):
        if not tameOngoing and not Timer.Check( 'skillTimer' ):
            # Clear any previously selected target and the target queue
            Target.ClearLastandQueue()
            # Wait for the target to finish clearing
            Misc.Pause( targetClearDelayMilliseconds )

            # Hey, we are finally using the Animal Taming skill! about time!
            Player.UseSkill( 'Animal Taming' )
            Target.WaitForTarget( 2000, False )
            Target.TargetExecute( animalBeingTamed )

            # Check if Animal Taming was successfully triggered
            if Journal.Search( 'Tame which animal?' ):
                timesTried += 1
                
                # Restart the timer so that it will go off when we will be able to use the skill again
#                Timer.Create( 'animalTamingTimer', animalTamingTimerMilliseconds )
                Timer.Create( 'skillTimer', animalTamingTimerMilliseconds )

                # Set tameOngoing to true to start the journal checks that will handle the result of the taming
                tameOngoing = True
            else:
                continue

        if tameOngoing:
            try:
                animalBeingTamed = Mobiles.FindBySerial(animalBeingTamed.Serial)
                if animalBeingTamed == None:
                    break
            except:
                break
            if ( Journal.SearchByName( 'It seems to accept you as master.', animalBeingTamed.Name ) or
                    Journal.Search( 'That wasn\'t even challenging.' ) ):
                # Animal was successfully tamed
                if animalBeingTamed.Name != renameTamedAnimalsTo:
                    Misc.PetRename( animalBeingTamed, renameTamedAnimalsTo )
                if Player.Followers > numberOfFollowersToKeep:
                    # Release recently tamed animal
                    Misc.WaitForContext( animalBeingTamed.Serial, 2000 )
                    Misc.ContextReply( animalBeingTamed.Serial, 8 )
                    Gumps.WaitForGump( 2426193729, 10000 )
                    Gumps.SendAction( 2426193729, 2 )
                    Misc.Pause(600)
                
                if killTame:
                    Player.Attack(animalBeingTamed)
                    Misc.Pause(600)
                    
                Misc.IgnoreObject( animalBeingTamed )
                animalBeingTamed = None
                timesTried = 0
                tameHandled = True
            elif ( Journal.SearchByName( 'You fail to tame the creature.', animalBeingTamed.Name ) or
                    Journal.SearchByName( 'The animal is too angry to continue taming.', animalBeingTamed.Name ) or
                    Journal.SearchByType( 'You must wait a few moments to use another skill.', 'System' ) ):
                tameHandled = True
                Misc.SendMessage('Tame attempt ' + str(timesTried),66)
                
            elif ( Journal.SearchByType( 'That is too far away.', 'System' ) or
                    Journal.SearchByName( 'You are too far away to continue taming.', animalBeingTamed.Name ) ):
                # Animal moved too far away, set to None so that another animal can be found
                animalBeingTamed = None
                timesTried = 0
                Timer.Create( 'skillTimer', 1 )
                #Timer.Create( 'animalTamingTimer', 1 )
                tameHandled = True
                
            elif ( Journal.SearchByName( 'You have no chance of taming this creature', animalBeingTamed.Name ) or
                    Journal.SearchByType( 'Target cannot be seen', 'System' ) or
                    Journal.SearchByType( 'Do not have a clear path to the animal','System' ) or
                    Journal.Search( 'This animal has had too many owners' ) or
                    Journal.Search( 'That animal looks tame already' ) ):
                # Ignore the object and set to None so that another animal can be found
                Misc.IgnoreObject( animalBeingTamed )
                animalBeingTamed = None
                timesTried = 0
                Timer.Create( 'skillTimer', 1 )
                #Timer.Create( 'animalTamingTimer', 1 )
                tameHandled = True

            if tameHandled:
                Journal.Clear()
                tameHandled = False
                tameOngoing = False

        # Wait a little bit so that the while loop does not consume as much CPU
        Misc.Pause( 50 )
        
def findInstrument():
    instruments = [0xe9e, 0x2805, 0xe9c, 0xeb3, 0xeb1, 0x0eb2, 0x0E9D ] 
    #instrument check
    for i in Player.Backpack.Contains:
        if i.ItemID in instruments:
            Target.TargetExecute(i)
            Player.HeadMessage(msgColour, "Instrument Found")
            Journal.Clear()
            Misc.Pause(200)
            break
            
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


def GetEnemies( Mobiles, minRange = 0, maxRange = 12, notorieties = GetEnemyNotorieties(), IgnorePartyMembers = False ):
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
    enemyFilter.CheckIgnoreObject = True
    enemies = Mobiles.ApplyFilter( enemyFilter )

    if IgnorePartyMembers:
        partyMembers = [ enemy for enemy in enemies if enemy.InParty ]
        for partyMember in partyMembers:
            enemies.Remove( partyMember )

    return enemies

# Start Animal Taming
TrainAnimalTaming()
