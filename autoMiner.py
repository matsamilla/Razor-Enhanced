#standard imports
import sys
from System.Collections.Generic import List

#global types
#generic
self = Player.Serial
self_pack = Player.Backpack.Serial
##Counts
oreCount = 0
##Ore, Colors
oreType = 0x19B9
ingotType = 0x1BF2
oreList = [
    ['iron', 0x0000, None],
    ['dullcopper', 0x0415, None],
    ['copper', 0x045F, None],
    ['bronze', 0x06D8, None],
    ['shadow', 0x0455, None],
    ['gold', 0x06B7, None],
    ['agapite', 0x097E, None],
    ['verite', 0x07D2, None],
    ['valorite', 0x0544, None],
]
##types lists
forgesList = List[int]((0x197A, 0x197E, 0x19A2, 0x1982, 0x1992, 0x1996, 0x199A, 0x0FB1))
tinkerTools = [0x1EB8, 0x1EBC]
minerTools = [0x0F39, 0x0E86]
## msg stubs
smeltSuccess = 'You smelt the ore removing the impurities and put the metal in your backpack.'
smeltFail = 'You burn away the impurities but are left with less useable metal.'

###################################
# Helper Functions
###################################
def getByItemID(itemid, source):
    #find an item id in container serial
    for item in Items.FindBySerial(source).Contains:
        if item.ItemID == itemid:
            return item
        else:
            Misc.NoOperation()
            
def countByItemID(itemid):
    # Count the number of items found in backpack by the ItemID
    count = 0
    for item in Player.Backpack.Contains:
        if item.ItemID == itemid:
            count = count + 1
        else:
            Misc.NoOperation()
    Misc.SendMessage('%i items found' % (count))
    return count

###################################
###################################

# Get any mining tool as soon as one is found
def getMinerTool():
    for item in minerTools:
        miningTool = getByItemID(item, self_pack)
        if miningTool is not None:
            return miningTool
            break
    if miningTool is None:
        craftPicks()

# If no mining tools present, use tinkertools to craft 3x pickaxes
def craftPicks():
    countMinerTools = 0
    for minertool in minerTools:
        countMinerTools = countMinerTools + countByItemID(minertool)
    while countMinerTools < 3:
        for item in tinkerTools:
            tinkerTool = getByItemID(item, self_pack)
        if tinkerTool is not None:
            if Gumps.HasGump():
                Gumps.WaitForGump(949095101, 10000)
                Gumps.SendAction(949095101, 0)
            Items.UseItem(tinkerTool)
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 8)
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 114)
        for minertool in minerTools:
            countMinerTools = countMinerTools + countByItemID(minertool)

# Read journal to determine if there is no metal at this spot
def readJournal():
    if Journal.Search('no metal'):
        Journal.Clear()
        return True
    else:
        Journal.Clear()
        return False

# Move x steps in target direction
def move(x):
    moveDirection = Player.Direction
    for _ in range(x):
        Player.Run(moveDirection)
        Misc.Pause(200)

# Search for new ore whos Item object has not been added to the oreList
def searchForNewOre():
    for item in Items.FindBySerial(self_pack).Contains:
        if item.ItemID == oreType:
            for ore in oreList:
                if item.Hue == ore[1]:
                    if ore[2] is None:
                        ore[2] = item
                        moveOre([ore])
                    else:
                        Misc.NoOperation()
        else:
            Misc.NoOperation

# Search of ore to be added to Item Object listed in oreList
def searchForKnownOre():
    for item in Items.FindBySerial(self_pack).Contains:
        if item.ItemID == oreType:
            for ore in oreList:
                if item.Hue == ore[1]:
                    if ore[2] is None:
                        Misc.NoOperation()
                    else:
                        Items.Move(item, ore[2], 0)
                        Misc.Pause(550)
        else:
            Misc.NoOperation

# move the ore to the tile infront of you
def moveOre(oreList):
    for ore in oreList:
        if ore[2] is not None:
            x, y, z = tileInFront()
            Items.MoveOnGround(ore[2], 0, x, y, z)
            Misc.Pause(550)

# Get the X Y Z for the tile in front of you
def tileInFront():
    direction = Player.Direction
    playerX = Player.Position.X
    playerY = Player.Position.Y
    playerZ = Player.Position.Z
    
    if direction == 'Up':
        tileX = playerX - 1
        tileY = playerY - 1
        tileZ = playerZ
    elif direction == 'North':
        tileX = playerX
        tileY = playerY - 1
        tileZ = playerZ
    elif direction == 'Right':
        tileX = playerX + 1
        tileY = playerY - 1
        tileZ = playerZ
    elif direction == 'East':
        tileX = playerX + 1
        tileY = playerY
        tileZ = playerZ
    elif direction == 'Down':
        tileX = playerX + 1
        tileY = playerY + 1
        tileZ = playerZ
    elif direction == 'South':
        tileX = playerX
        tileY = playerY + 1
        tileZ = playerZ
    elif direction == 'Left':
        tileX = playerX - 1
        tileY = playerY + 1
        tileZ = playerZ
    elif direction == 'West':
        tileX = playerX - 1
        tileY = playerY
        tileZ = playerZ
    return tileX, tileY, tileZ
    
# Find a if a forge graphics is within 2 tiles of you
def nearForge():
    forgeFilter = Items.Filter()
    forgeFilter.Enabled = True
    forgeFilter.OnGround = True
    forgeFilter.Movable = False
    forgeFilter.Graphics = forgesList
    forgeFilter.RangeMax = 2
    
    forges = Items.ApplyFilter(forgeFilter)
    Misc.SendMessage
    for forge in forges:
        if 'forge' in forge.Name or 'bellows' in forge.Name:
            return True
    return False
    
#Were near a forge, so smelt everything we have!
def smeltAllOre():
    #Move all ore to stacks
    searchForKnownOre()
    i = 0
    for ore in oreList:
        while ore[2] is not None:
            if ore[0] == 'iron':
                Misc.SendMessage('SMELT: ' + ore[0][:4] + ': ' + str(ore[2].Amount), ore[1])
                Items.UseItem(ore[2])
                Misc.Pause(550)
                oreList[i][2] = None
                break
            elif ore[0] == 'shadow' or ore[0] == 'dullcopper' or ore[0] == 'copper':
                Misc.SendMessage('SMELT: ' + ore[0][:4] + ': ' + str(ore[2].Amount), ore[1])
                Items.UseItem(ore[2])
                Misc.Pause(550)
                if Journal.Search(smeltSuccess):
                    Journal.Clear()
                    oreList[i][2] = None
                    break
            else:
                for j in range(ore[2].Amount):
                    Misc.SendMessage('SMELT: ' + ore[0][:4] + ': ' + str(ore[2].Amount), ore[1])
                    Items.UseItem(ore[2])
                    Misc.Pause(550)
                oreList[i][2] = None
                break
        i += 1

#Get the total ore count
def getOreCount():
    searchForKnownOre()
    oreCount = 0
    for ore in oreList:
        if ore[2] is not None:
            oreCount = oreCount + ore[2].Amount
    return oreCount
    
#Display pretty-like the ore counts
def printOreCounts():
    total = 0
    for ore in oreList:
        if ore[2] is not None:
            Misc.SendMessage(ore[0][:4] + ': ' + str(ore[2].Amount), ore[1])
            total = total + ore[2].Amount
    Misc.SendMessage('all : ' + str(total), 67)

#Main Handler for mining    
def autoMiner():
    while True:
            
        #Get a mining tool!
        miningTool = getMinerTool()
        
        #Use found mining tool
        Journal.Clear()
        Items.UseItem(miningTool)
        Target.WaitForTarget(2000,True)
        Target.TargetExecuteRelative(self,1)
        Misc.Pause(600)
        
        #search pack for ore, add to stack
        searchForNewOre()
        
        #if overweight move known ore to stack
        if Player.Weight >= Player.MaxWeight:
            searchForKnownOre()
            
        #Determine if no metal left and move accordingly
        boolMove = readJournal()
        if boolMove:
            move(2)
            moveOre(oreList)
        if boolMove:
            move(1)
        boolMove = False
        
        #if near forge, smelt all!
        smeltAll = nearForge()
        if smeltAll:
            oreCount = getOreCount()
        if smeltAll and oreCount > 50:
            smeltAllOre()
            
        #print the ore counts
        printOreCounts()
        

autoMiner()
