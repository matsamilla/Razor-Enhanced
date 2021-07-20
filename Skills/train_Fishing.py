'''
Author: TheWarDoctor95
Other Contributors:
    Last Contribution By: MatsaMilla - 7/19/21

Description: Train fishing, Fishing up MIBs, nets, maps & scales
'''

#############    Setup Section    ################

cutCorpse = True # True if you want to cut corpses

#update for MAGE heal macro - use MatsaMilla Bandage_Self.py if you have healing
healMacroName = 'cast_BigHeal.py' #found in MatsaMilla github

# true to attack serpents - will attack by magery if no tactics
attack = True
    
###########  End  Setup Section    ###############

from System.Collections.Generic import List
from System import Byte
import sys
dragTime = 600
journalEntryDelay = 200

fishIDs = [ 0x09CF, 0x09CE, 0x09CC, 0x09CD ]
player_bag = Items.FindBySerial(Player.Backpack.Serial)

hornedFilter = Items.Filter()
hornedFilter.OnGround = 1
hornedFilter.Movable = True
hornedFilter.RangeMin = 0
hornedFilter.RangeMax = 2
hornedFilter.Graphics = List[int]( [ 0x1079 , 0x1081 ] ) #cut leather graphic 0x1081
hornedFilter.Hues = List[int]( [ 0x0900 ] )

fishsteakFilter = Items.Filter()
fishsteakFilter.OnGround = 1
fishsteakFilter.Movable = True
fishsteakFilter.RangeMin = 0
fishsteakFilter.RangeMax = 2
fishsteakFilter.Graphics = List[int]( [ 0x097A ] )

# mobile filter
def find(notoriety):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = 12
    fil.IsHuman = False
    fil.IsGhost = False
    fil.Friend = False
    fil.Notorieties = List[Byte](bytes(notoriety))
    list = Mobiles.ApplyFilter(fil)

    return list
    
def Fish( fishingPole, x, y ):
    '''
    Casts the fishing pole and returns True while the fish are biting
    '''
    
    global fishIDs
    
    # eats special fish
    if Items.BackpackCount(0x0DD6,-1) > 0:
        spFish = Items.FindByID(0x0DD6,-1,Player.Backpack.Serial)
        Items.UseItem(spFish)
        Misc.Pause( dragTime )

    Journal.Clear()
    Items.UseItemByID(0x0DBF,-1)
    
    Target.WaitForTarget( 2000, True )
    
    statics = Statics.GetStaticsTileInfo( x, y, 0 )
    if len( statics ) > 0:
        water = statics[ 0 ]
        Target.TargetExecute( x, y, water.StaticZ, water.StaticID )
    else:
        Target.TargetExecute( x, y, -5, 0x0000 )
        
    
    Misc.Pause( dragTime )
    Target.Cancel()
        
    Timer.Create( 'timeout', 20000 )
    while not ( Journal.SearchByType( 'You pull', 'System' ) or
            Journal.SearchByType( 'You fish a while, but fail to catch anything.', 'System' ) or
            Journal.SearchByType( 'Your fishing pole bends as you pull a big fish from the depths!', 'System' ) or
            Journal.SearchByType( 'Uh oh! That doesn\'t look like a fish!', 'System' )):
        
        if not Timer.Check( 'timeout' ):
            return False
        
        if (Journal.SearchByType( 'The fish don\'t seem to be biting here', 'System' ) or
            Journal.SearchByType( 'You need to be closer to the water to fish!', 'System' )):
            return False
        
        enemy = Mobiles.Select(find([3,4]),'Nearest')
        if enemy != None:
            FightEnemy()
        Misc.Pause( 50 )

    
    if Player.Weight >= Player.MaxWeight - 20 :
        for fish in player_bag.Contains:
            # cuts fish
            if fish.ItemID in fishIDs:
                Items.UseItemByID( 0x0F52 )
                Target.WaitForTarget( 2000, True )
                Target.TargetExecute( fish )
                Misc.Pause( dragTime )
            # cuts up leather
            if fish.ItemID == 0x1079:
                Items.UseItemByID( 0x0F9F )
                Target.WaitForTarget( 2000, True )
                Target.TargetExecute( fish )
                Misc.Pause( dragTime )
        stackItem(0x097A, -1, fishsteakFilter) #stacks fish to feet
        stackItem(0x1081, -1, hornedFilter) #stacks cut leather to feet
        stackItem(0x1079, -1, hornedFilter) #stacks leather to feet if not cut
    
    return True



def FightEnemy():
    enemy = Mobiles.Select(find([3,4]),'Nearest')
    if attack == False:
        return
    if Player.GetRealSkillValue('Tactics') > 60:
        if enemy != None:
            Timer.Create('fishattack', 60000)
            Misc.ScriptRun( autoFightMacroName )
            while enemy != None:
                enemy = enemy.serial
                Misc.Pause( 100 )
                if Timer.Check('fishattack') == False:
                    for i in range( 0, 3 ):
                        Player.ChatSay( 0, 'back one' )
                        Misc.Pause( 320 )
                    break
                    
    elif Player.GetRealSkillValue('Magery') > 70:
        while enemy!= None:
            enemy = Mobiles.FindBySerial( enemy.Serial )
            if enemy == None:
                break
            while Player.Mana > 20 and enemy != None:
                enemy = Mobiles.FindBySerial( enemy.Serial )
                if enemy == None:
                    break
                Spells.CastMagery( 'Energy Bolt' )
                Target.WaitForTarget( 2000, False )
                Target.TargetExecute( enemy )
                Misc.Pause( 1600 )
            if Player.Hits < 40:
                Misc.ScriptRun(healMacroName)
            Player.UseSkill( 'Meditation' )
            while Player.Mana < 34:
                Misc.Pause( 100 )
                if Player.Hits < 40:
                    Misc.ScriptRun(healMacroName)
            if enemy == None:
                break
                    
def scoopCorpse():
    for i in range( 0, 3 ):
        Player.ChatSay( 0, 'back one' )
        Misc.Pause( 320 )
        
    for i in range( 0, 4 ):
        Player.ChatSay( 0, 'forward one' )
        Misc.Pause( 320 )
        
    for i in range( 0, 5 ):    
        Player.ChatSay( 0, 'left one' )
        Misc.Pause( 320 )
    
    for i in range( 0, 10 ):
        Player.ChatSay( 0, 'right one' )
        Misc.Pause( 320 )
        
    for i in range( 0, 5 ):    
        Player.ChatSay( 0, 'left one' )
        Misc.Pause( 320 )

    corpseFilter = Items.Filter()
    corpseFilter.Movable = False
    corpseFilter.RangeMax = 2
    corpseFilter.Graphics = List[int]( [ 0x2006 ] )
    corpseFilter.CheckIgnoreObject = True
    corpses = Items.ApplyFilter( corpseFilter )
    corpse = None
    
    for corpse in corpses:
        if cutCorpse:
            Items.UseItemByID( 0x0F52 )
            Target.WaitForTarget( 2000, True )
            Target.TargetExecute( corpse.Serial )
            Misc.Pause( dragTime )
            Misc.IgnoreObject( corpse.Serial )
        
        #if Items.BackpackCount( 0x1079 , -1 ) > 0:
        leather = Items.FindByID( 0x1079 , -1 , Player.Backpack.Serial) 
        if leather:
            Items.UseItemByID( 0x0F9F )
            Target.WaitForTarget( 2000, True )
            Target.TargetExecute( leather )
            Misc.Pause( dragTime )
            stackItem(0x1081, -1, hornedFilter) #stacks cut leather to feet

def UseFishing():
    global moveForwardBackward
    
    fishingPole = Items.FindByID( 0x0DBF, -1 , Player.Backpack.Serial )
    
    if fishingPole == None:
        Misc.SendMessage('No fishing poles!!', 33)
        sys.exit()
            
    Misc.SendMessage(fishingPole)
    while True:
        x = Player.Position.X - 3
        y = Player.Position.Y - 3
        while Fish( fishingPole, x, y ):
            enemy = Mobiles.Select(find([3,4]),'Nearest')
            if enemy != None:
                FightEnemy()
                
        x = Player.Position.X + 3
        y = Player.Position.Y - 3
        while Fish( fishingPole, x, y ):
            enemy = Mobiles.Select(find([3,4]),'Nearest')
            if enemy != None:
                FightEnemy()

        x = Player.Position.X + 3
        y = Player.Position.Y + 3
        while Fish( fishingPole, x, y ):
            enemy = Mobiles.Select(find([3,4]),'Nearest')
            if enemy != None:
                FightEnemy()
        
        x = Player.Position.X - 3
        y = Player.Position.Y + 3
        while Fish( fishingPole, x, y ):
            enemy = Mobiles.Select(find([3,4]),'Nearest')
            if enemy != None:
                FightEnemy()

        Misc.Pause( 320 )
        
        scoopCorpse()
        
        for i in range( 0, 20 ):
            Player.ChatSay( 0, 'Forward one')
            Misc.Pause( 320 )
        Misc.Pause( 320 )

        Misc.Pause( journalEntryDelay )
        
        if Journal.Search( 'Ar, we\'ve stopped sir.' ):
            Misc.Beep()
            Journal.Clear()
                    
def stackItem ( item , hue , filter):
    itemOnGround = Items.ApplyFilter( filter )
    if Items.BackpackCount( item , hue ) > 0:
        itemInPack = Items.FindByID( item , hue , Player.Backpack.Serial )
        if not itemOnGround:
            Items.DropItemGroundSelf( itemInPack , 0 )
        else:
            itemStack = itemOnGround[ 0 ]
            Items.Move( itemInPack , itemStack , 0 )
    Misc.Pause( dragTime )
    
def hide():
    if Player.GetRealSkillValue('Hiding') > 50:
        if Timer.Check('hideskill' + Player.Name) == False and not Player.BuffsExist('Hiding'):
            if Journal.SearchByType('You can\'t seem to hide right now.' , 'System' ):
                Player.ChatSay( 22 , 'Forward' )
                Misc.Pause(10000)
            Player.UseSkill('Hiding')
            Timer.Create('hideskill' + Player.Name,11000)
            

# Start Fishing

UseFishing()
