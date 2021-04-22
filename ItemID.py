# ItemID script by MatsaMilla v2
# Item ID
from System.Collections.Generic import List
import sys
import winsound
#**********************************************************


# turn to true if client has tool tips enabled
toolTipsOn = True

# True if you want to keep scrolls
sortScrolls = False

#if you mark sortScrolls true and this false all lvl8 scrolls go in scroll chest
keeplvl8Scrolls = False

# True to place all junk in trash barrel, else leaves in chest
tossJunk = False

# path to sound when overweight
sound = "D:\\Program Files\\CUO Launcher\\ClassicUO\\Data\\Plugins\\Razor-Enhanced\\Sounds\\pssst.wav"

# Servers drag delay
dragTime = 650
    
#**********************************************************

# constant chests
regChest = 0x43510513
netChest = 0x4012EC5A
goldChest = 0x463A35DB
gemChest = 0x4208D8F2
lvl8bag = 0x424A881A #where to put lvl 8 scrolls
scrollChest = 0x41FF4A29 #chest for all other scrolls

# bags inside scrollChest, from 1-8 for lvls
scrollBags = [ 0x424A8818,0x424A881B,0x424A8817,0x424A8816,0x424A8819,0x424A8815,0x424A8814,0x424A881A]

#**********************************************************

containerToOrganize = Target.PromptTarget('Select container to ID stuff in')
sellBag = Target.PromptTarget('Select Sell to NPC Bag')
goodChest = Target.PromptTarget('Select KEEPER container (GOOD SHIT)')

# Will use ID Wand if skill Item ID below 80
if Player.GetRealSkillValue('Item ID') < 80:
    idWand = True
else:
    idWand = False
##############################################################
# Use neraby trashcan
##############################################################
 
trashBarrelFilter = Items.Filter()
trashBarrelFilter.OnGround = 1
trashBarrelFilter.Movable = False
trashBarrelFilter.RangeMin = 0
trashBarrelFilter.RangeMax = 2
trashBarrelFilter.Graphics = List[int]( [ 0x0E77 ] )
trashBarrelFilter.Hues = List[int]( [ 0x03B2 ] )
trashcanhere = Items.ApplyFilter( trashBarrelFilter )

if not trashcanhere:
    Player.HeadMessage( 1100, 'No trashcan nearby!' )
    sys.exit()
else:
    global trashCan
    trashCan = trashcanhere[ 0 ]

msgColor = 45
stopWeight = 380
rightHand = Player.CheckLayer('RightHand')
leftHand = Player.CheckLayer('LeftHand')

# I do not know what this is
loot = [0x2260,0x2831] #0x2831 = Recipe Scroll

perk = [0x2dd5,0x1f18,0x2da3,0x166e,0x26BB,0x139B]
gold = [0xeed]
gems = [0xf16,0xf15,0xf19,0xf25,0xf21,0xf10,0xf26,0xf2d,0xf13,0x1F4C] #0x1F4C recall
wands = [0xdf5,0xdf3,0xdf4,0xdf2]
regs= [0xf7a,0xf7b,0xf86,0xf84,0xf85,0xf88,0xf8d,0xf8c]
net = [0x0DCA]

boneArmor = [0x1450,0x1f0b,0x1452,0x144f,0x1451,0x144e]

weps = [0xf62,0x1403,0xe87,0x1405,0x1401,0xf52,0x13b0,0xdf0,0x1439,0x1407,0xe89,0x143d,0x13b4,0xe81,0x13f8,
0xf5c,0x143b,0x13b9,0xf61,0x1441,0x13b6,0xec4,0x13f6,0xf5e,0x13ff,0xec3,0xf43,0xf45,0xf4d,0xf4b,0x143e,
0x13fb,0x1443,0xf47,0xf49,0xe85,0xe86,0x13fd,0xf50,0x13b2,]

armor = [0x1b72,0x1b73,0x1b7b,0x1b74,0x1b79,0x1b7a,0x1b76,0x1408,0x1410,0x1411,0x1412,0x1413,0x1414,0x1415,
0x140a,0x140c,0x140e,0x13bb,0x13be,0x13bf,0x13ee,0x13eb,0x13ec,0x13f0,0x13da,0x13db,0x13d5,0x13d6,0x13dc,
0x13c6,0x13cd,0x13cc,0x13cb,0x13c7,0x1db9,0x1c04,0x1c0c,0x1c02,0x1c00,0x1c08,0x1c06,0x1c0a,]

# useless items no matter how good they are, aka bad shields & ringmail
sellItems = [ 0x1B72,0x13DB,0x13D5,0x13DA,0x1B7B,0x1DB9,0x13BB,0x1B79,0x13EB,0x1B7A,0x13F0,0x1C02,0x1C0C,
0x13EC,0x1B73,0x13DC,0x13BE,0x13EE,0x13D6,0x13BF ]

trash = [0x171c,0x1717,0x1718,0x1544,0x1540,0x1713,0x1715,0x1714,0x1716,0x1717,0x1718,0x1719,0x171a,0x171b,
0x171c,0x2306,0x13f6,0xec4,0x1716,0x171c,0xe81,0xe86,]

keepArmorMods = ['Invulnerability','Exceptional'] #'Fortification', 'Hardening', 'Guarding', 'Defence'
keepArmorHPMods = ['Indestructible','Fortified','Massive'] # 'Substantial' , 'Durable'

keepWepDmgMods = ['Power'] # 'Force', 'Might', 'Ruin'
keepWepAccuracyMods = ['Supremely Accurate','Exceedingly Accurate'] # 'Eminently Accurate', 'Surpassingly Accurate', 'Accurate'
keepProps = ['Vanquishing']
slayerProps = ['Silver','Undead','Snake','Lizardman','Dragon','Reptile','Terathan',
'Orc Slaying','Ogre','Water','Earth','Elemental','Repond','Fey','Daemon','Exorcism','Poison','Arachnid']
# 'Scorpion','Flame','Vacuum','Gargoyle','Spider'

lvl1Scrolls = [
0x1f2e,# Clumsy
0x1f2f,# Create Food
0x1f30,# Feeblemind
0x1f31,# Heal
0x1f32,# Magic Arrow
0x1f33,# Night Sight
0x1f2d,# Reactive Armor
0x1f34,# Weaken
]
lvl2Scrolls = [
0x1f35,# Agility
0x1f36,# Cunning
0x1f37,# Cure
0x1f38,# Harm
0x1f39,# Magic Trap
0x1f3a,# Magic Untrap
0x1f3b,# Protection
0x1f3c,# Strength
]
lvl3Scrolls = [
0x1f3d,# Bless
0x1f3e,# Fireball
0x1f3f,# Magic Lock
0x1f40,# Poison
0x1f41,# Telekinesis
0x1f42,# Teleport
0x1f43,# Unlock
0x1f44,# Wall of Stone
]
lvl4Scrolls = [
0x1f45,# Arch Cure
0x1f46,# Arch Protection
0x1f47,# Curse
0x1f48,# Fire Field
0x1f49,# Greater Heal
0x1f4a,# Lightning
0x1f4b,# Mana Drain
0x1f4c,# Recall
]
lvl5Scrolls = [
0x1f4d,# Blade Spirit
0x1f4e,# Dispel Field
0x1f4f,# Incognito
0x1f50,# Magic Reflection
0x1f51,# Mind Blast
0x1f52,# Paralyze
0x1f53,# Poison Field
0x1f54,# Summon Creature
]
lvl6Scrolls = [
0x1f55,# Dispel
0x1f56,# Energy Bolt
0x1f57,# Explosion
0x1f58,# Invisibility
0x1f59,# Mark
0x1f5a,# Mass# Curse
0x1f5b,# Paralyze Field
0x1f5c,# Reveal
]
lvl7Scrolls = [
0x1f5d,# Chain Lightning
0x1f5e,# Energy Field
0x1f5f,# Flamestrike
0x1f60,# Gate Travel
0x1f61,# Mana Vampire
0x1f62,# Mass Dispel
0x1f63,# Meteor Swarm
0x1f64,# Polymorph
]
lvl8Scrolls = [
0x1f65,# Earthquake
0x1f66,# Energy Vortex
0x1f67,# Ressurrection
0x1f68,# Summon Air Elemental
0x1f69,# Summon Daemon
0x1f6a,# Summon Earth Elemental
0x1f6b,# Summon Fire Elemental
0x1f6c,# Summon Water Elemental
]
if sortScrolls or keeplvl8Scrolls:
    Items.UseItem(scrollChest)
    Misc.Pause(dragTime)

def equipWand():
    global wandSerial
    player_bag = Items.FindBySerial(Player.Backpack.Serial)
    if leftHand:
        Player.UnEquipItemByLayer('LeftHand')
        Misc.Pause(dragTime)
    if not rightHand:
        for i in player_bag.Contains:
            if i.ItemID in wands:
                Player.EquipItem(i.Serial)
                Misc.Pause(dragTime)
                wandSerial = Player.GetItemOnLayer('RightHand').Serial
    elif Player.GetItemOnLayer('RightHand').ItemID in wands:
        wandSerial = Player.GetItemOnLayer('RightHand').Serial
    else:
        Player.ChatSay(33, "No Wands Found, Stopping Script")
        sys.exit()
    Misc.Pause(dragTime)
        
def idTarget():
    worldSave()
    if idWand:
        equipWand()
        Items.UseItem(wandSerial)
        Misc.Pause(100)
    else:
        Player.UseSkill('Item ID')
        Misc.Pause(100)
    if not Target.HasTarget():
        Misc.Pause(1000)
        idTarget()

def checkWeight():
    if Player.Weight >= stopWeight:
        Player.HeadMessage(msgColor, 'Go Sell this shit')
        winsound.PlaySound(sound, winsound.SND_ALIAS)
        sys.exit()
        
def idStuff(container, type):
    idContainer = Items.FindBySerial(container)
    
    if type == 'weps':
        idItems = weps
        tier1 = keepWepDmgMods
        tier2 = keepWepAccuracyMods
        worthlessBag = sellBag
    elif type == 'armor':
        idItems = armor
        tier1 = keepArmorMods
        tier2 = keepArmorHPMods
        worthlessBag = sellBag
    elif type == 'bone':
        idItems = boneArmor
        tier1 = keepArmorMods
        tier2 = ['Indestructible']
        worthlessBag = trashCan
    
        
    for i in idContainer.Contains:
        worldSave()
        if i.ItemID in idItems:
            checkWeight()
            Journal.Clear()
            idTarget()
            Target.WaitForTarget(1500)
            Target.TargetExecute(i.Serial)
            Misc.Pause(dragTime)
            Items.SingleClick(i)
            if any(Journal.Search(keep) for keep in keepProps):
                #** Good Stuff Move **
                Items.Move(i, goodChest, 0)
                Misc.Pause(dragTime)
            elif any(Journal.Search(slash) for slash in tier1):
                #moves items if in sell ids
                if i.ItemID in sellItems:
                    #** Sell Stuff Move **
                    Items.Move(i, worthlessBag, 0)
                    Misc.Pause(dragTime)
                elif any(Journal.Search(sub) for sub in tier2):
                    #** Good Stuff Move **
                    Items.Move(i, goodChest, 0)
                    Misc.Pause(dragTime)
                else:
                    #** Sell Stuff Move **
                    Items.Move(i, worthlessBag, 0)
                    Misc.Pause(dragTime)
            else:
                #** Sell Stuff Move **
                Items.Move(i, worthlessBag, 0)
                Misc.Pause(dragTime)
                
def idStuffToolTips(container, type):
    idContainer = Items.FindBySerial(container)
    
    if type == 'weps':
        idItems = weps
        tier1 = keepWepDmgMods
        tier2 = keepWepAccuracyMods
        worthlessBag = sellBag
    elif type == 'armor':
        idItems = armor
        tier1 = keepArmorMods
        tier2 = keepArmorHPMods
        worthlessBag = sellBag
    elif type == 'bone':
        idItems = boneArmor
        tier1 = keepArmorMods
        tier2 = ['Indestructible']
        worthlessBag = trashCan
    
        
    for i in idContainer.Contains:
        worldSave()
        if i.ItemID in idItems:
            checkWeight()
            Journal.Clear()
            idTarget()
            Target.WaitForTarget(1500)
            Target.TargetExecute(i.Serial)
            Misc.Pause(dragTime)
            Items.WaitForProps(i,2000)
            props = Items.GetPropStringList(i)
            if any(elem in keepProps for elem in props):
                #** Good Stuff Move **
                Items.Move(i, goodChest, 0)
                Misc.Pause(dragTime)
            elif any(elem in tier1 for elem in props):
                #moves items if in sell ids
                if i.ItemID in sellItems:
                    #** Sell Stuff Move **
                    Items.Move(i, worthlessBag, 0)
                    Misc.Pause(dragTime)
                elif any(elem in tier2 for elem in props):
                    #** Good Stuff Move **
                    Items.Move(i, goodChest, 0)
                    Misc.Pause(dragTime)
                else:
                    #** Sell Stuff Move **
                    Items.Move(i, worthlessBag, 0)
                    Misc.Pause(dragTime)
            else:
                #** Sell Stuff Move **
                Items.Move(i, worthlessBag, 0)
                Misc.Pause(dragTime)
        
def organizeItems(container):    
    idContainer = Items.FindBySerial(container)
    for i in idContainer.Contains:
        worldSave()
        if i.ItemID in loot:
            Items.Move(i, Player.Backpack.Serial, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in perk:
            Items.Move(i, Player.Backpack.Serial, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in gold:
            Items.Move(i, goldChest, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in regs:
            Items.Move(i, regChest, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in gems:
            Items.Move(i, gemChest, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in net:
            Items.Move(i, netChest, 0)
            Misc.Pause(dragTime)
        elif i.ItemID in lvl8Scrolls:
            if keeplvl8Scrolls and sortScrolls == False:
                Items.Move(i, scrollBags[7], 0)
                Misc.Pause(dragTime)
    for i in idContainer.Contains:
        if i.ItemID in lvl1Scrolls:
            scrollSorter(i, scrollBags[0])
        elif i.ItemID in lvl2Scrolls:
            scrollSorter(i, scrollBags[1])
        elif i.ItemID in lvl3Scrolls:
            scrollSorter(i, scrollBags[2])
        elif i.ItemID in lvl4Scrolls:
            scrollSorter(i, scrollBags[3])
        elif i.ItemID in lvl5Scrolls:
            scrollSorter(i, scrollBags[4])
        elif i.ItemID in lvl6Scrolls:
            scrollSorter(i, scrollBags[5])
        elif i.ItemID in lvl7Scrolls:
            scrollSorter(i, scrollBags[6])
        elif i.ItemID in lvl8Scrolls:
            scrollSorter(i, scrollBags[7])
        elif i.ItemID in trash:
            if tossJunk:
                Items.Move(i, trashCan, 0)
                Misc.Pause(dragTime)
                
def scrollSorter(item, destination):
    if sortScrolls:
        Items.Move(item, destination, 0)
        Misc.Pause(dragTime)  
    else:
        if tossJunk:
            Items.Move(item, trashCan, 0)
            Misc.Pause(dragTime)
                
def worldSave():
    if Journal.SearchByType('The world is saving, please wait.', 'Regular' ):
        Misc.SendMessage('Pausing for world save', 33)
        while not Journal.SearchByType('World save complete.', 'Regular'):
            Misc.Pause(1000)
        Misc.SendMessage('Continuing', 33)
        Journal.Clear()
        
def findChest():
    # Filters
    chest = Items.Filter()
    chest.Enabled = True
    chest.OnGround = True
    chest.Movable = True
    chest.RangeMax = 1
    chest.Graphics = List[int]( [ 0x0E40,0x0E43,0x0E41,0x0E43,0x09AB,0x0E42 ] )
    chest.CheckIgnoreObject = True
    chest = Items.ApplyFilter(chest)
    sortChest = Items.Select(chest, 'Nearest')
    

    if sortChest:
        Items.UseItem(sortChest)
        Misc.Pause(dragTime)
        if Journal.Search("locked")== True:
            lockpickchest(sortChest)
            Misc.Pause(3000)
            Items.UseItem( sortChest )
        while Player.Hits < Player.HitsMax:
            Spells.CastMagery('Greater Heal')
            Target.WaitForTarget(1500)
            Target.Self()
            Misc.Pause(2500)
            Items.UseItem( sortChest )
            Misc.Pause(dragTime)
        organizeItems(sortChest.Serial)
        if toolTipsOn:
            idStuffToolTips(sortChest.Serial, 'weps')
            idStuffToolTips(sortChest.Serial, 'armor')
            idStuffToolTips(sortChest.Serial, 'bone')
        else:
            idStuff(sortChest.Serial, 'weps')
            idStuff(sortChest.Serial, 'armor')
            idStuff(sortChest.Serial, 'bone')
        Player.HeadMessage(msgColor, 'Chest Cleared')
#        Items.Move(sortChest.Serial, trashCan, 0)
#        Misc.Pause(dragTime)
#        Misc.IgnoreObject(sortChest.Serial)

def lockpickchest(chest):
    lockpicks = Items.FindByID(0x14FC, -1, Player.Backpack.Serial)
    if lockpicks == None:
        Player.HeadMessage( 33, 'You don\'t have any lockpicks!' )
        return
    
    Items.UseItem(lockpicks)
    lockedChest = Items.FindBySerial( chest.Serial )
                
    Player.HeadMessage( 44, 'Starting chest unlock!' )
    
    Journal.Clear()
    while not ( Journal.SearchByName( 'The lock quickly yields to your skill.', '' ) or
            Journal.SearchByType( 'This does not appear to be locked.', 'Regular' ) ):
        Items.UseItem( lockpicks )
        Target.WaitForTarget( 2000, True )
        Target.TargetExecute( lockedChest )
        Misc.Pause( 4000 )
        Misc.Pause( 120 )

        lockpicks = Items.FindByID(0x14FC, -1, Player.Backpack.Serial)
        if lockpicks == None:
            Player.HeadMessage( 33, 'Ran out of lockpicks!' )
            return
        
    else:
        return False
        
Items.UseItem(containerToOrganize)
Misc.Pause(dragTime)
Items.UseItem(sellBag)
Misc.Pause(dragTime)
Journal.Clear()
organizeItems(containerToOrganize)
if toolTipsOn:
    idStuffToolTips(containerToOrganize, 'weps')
    idStuffToolTips(containerToOrganize, 'armor')
    idStuffToolTips(containerToOrganize, 'bone')
else:
    idStuff(containerToOrganize, 'weps')
    idStuff(containerToOrganize, 'armor')
    idStuff(containerToOrganize, 'bone')
Player.HeadMessage(msgColor, 'Chest Cleared')
Items.Move(containerToOrganize, trashCan, 0)
