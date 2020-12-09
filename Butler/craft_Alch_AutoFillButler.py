# Automatic Potion Butler Filler by MatsaMilla 
#   - Version 2, updated 12/9/20

# Must have TOOLTIPSON ([toggletooltips in game to turn off/on)

# NEED: Restock Chest (containing regs / empty pots), 
#       Mortars in backpack or in restock chest (can be in a bag in restock chest, has to be open).
#       Empty keg in toons backpack.

# Makes Make sure restock chest & motar restock bags are open

#*******************************************************************#

Player.HeadMessage(66,'Target Butler')
butler = Target.PromptTarget('Target Butler')
Player.HeadMessage(66,'Target Restock Chest')
restockChest = Items.FindBySerial( Target.PromptTarget('Target Restock Chest') )
#Player.HeadMessage(66,'Mortar Restock Bag (optional)')
#mortarBag = Items.FindBySerial( Target.PromptTarget('Mortar Restock Bag (optional)') )
        
keg = Items.FindByID( 0x1940 , -1 ,  Player.Backpack.Serial )
if keg:
    Misc.SendMessage('Using keg in pack', 66)
else:
    Player.HeadMessage(66,'Target keg to fill')
    kegTarget =  Target.PromptTarget('Target keg to fill')
    Misc.SendMessage('Using targeted Keg', 66)
    keg = Items.FindBySerial(kegTarget)

fillStopNumber = 5000
dragTime = 800
butlerGump = 989312372

def setValues( regValue , potValue , gump1 , gump2 ):
    global regID
    global potID
    global gumpAction1
    global gumpAction2
    regID = regValue
    potID = potValue
    gumpAction1 = gump1
    gumpAction2 = gump2


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
            
def craftPot (potType):
    
    # set values for pot items
    if potType == 'cure':
        setValues( 0x0F84 , 0x0F07 , 43 , 16 )
    elif potType == 'heal':
        setValues( 0x0F85, 0x0F0C , 22 , 16 )
    elif potType == 'refresh':
        setValues ( 0x0F7A , 0x0F0B , 1 , 9 )
    elif potType == 'explode':
        setValues ( 0x0F8C, 0x0F0D , 50 , 16 )
    elif potType == 'strength':
        setValues ( 0x0F86 , 0x0F09 , 29 , 9 )
    elif potType == 'agility':
        setValues ( 0x0F7B, 0x0F08 , 8 , 9 )
    elif potType == 'DP':
        setValues ( 0x0F88 , 0x0F0A , 36 , 23 )
    else:
        Misc.SendMessage('potType not defined, stopping', 33)
        Misc.ScriptStop('craft_Alch_FillButler.py')
    
    while not Items.GetPropValue(keg,'The Keg Is Completely Full.'): 
    #while not Journal.SearchByType('The keg will not hold any more!', 'Regular'): # non-tool tips change
        
        worldSave()
        
        # find mortar, even if nested in backpack
        mortar = FindItem( 0x0E9B , Player.Backpack )
        if not mortar:
            if mortarBag != -1:
                mortarFound = FindItem( 0x0E9B , restockChest )#Items.FindByID(0x0E9B , -1 , mortarBag)
                if mortarFound:
                    Items.Move(mortarFound, Player.Backpack.Serial, 0)
                    Misc.Pause(dragTime)
                else:
                    Misc.SendMessage('Out of Mortars!', 33)
                    Misc.Pause(5000)
                    Stop
            else:
                Misc.SendMessage('Out of Mortars!', 33)
                Misc.Pause(5000)
                Stop
         
        # count / restock reg type
        packRegs = FindItem(regID, Player.Backpack)
        if not packRegs or packRegs.Amount < 10:
        #if Items.BackpackCount(regID) < 10:
            Misc.Pause(100)
            regFound = FindItem(regID, restockChest) #Items.FindByID( regID, -1, restockChest)
            if regFound:
                Items.WaitForProps( regFound.Serial , dragTime)
                Items.Move( regFound, Player.Backpack , 250 )
                Misc.Pause(800)
                packRegs = FindItem(regID, Player.Backpack)
                if not packRegs or packRegs.Amount < 10:
                #if Items.BackpackCount(regID) < 10:
                    Misc.NoOperation()
                    #Misc.SendMessage('Out of regs for this pot type, moving to next pot - 1', 33)
                    break
            else:
                Misc.SendMessage('Out of regs for this pot type, moving to next pot', 33)
                break
            
        # move pot to keg  
        pot = FindItem( potID , Player.Backpack)
        while pot:
            Items.Move(pot, keg, 0)
            Misc.Pause(dragTime)
            pot = FindItem( potID , Player.Backpack)
        
        # make sure you have empty bottle
        if Items.BackpackCount(0x0F0E) < 1:
            emptyPot = FindItem(0x0F0E,restockChest) #Items.FindByID( 0x0F0E, -1, restockChest)
            if emptyPot:
                Items.Move(emptyPot, Player.Backpack.Serial, 2)
                Misc.Pause(dragTime)
            else:
                Player.HeadMessage(33,'Need empty pot(s) in restock container or in backpack.')
                Stop
        # empty keg of other potion
        if Journal.Search('You decide that it would be a bad idea to mix different types of potions.'):
            Misc.SendMessage('Oops')
            Items.Move( keg , butler , 0 )
            Misc.Pause(dragTime)
            Journal.Clear()
            
        #craft pot
        Items.UseItem(mortar)
        Gumps.WaitForGump(949095101, dragTime)
        Gumps.SendAction(949095101, gumpAction1)
        Gumps.WaitForGump(949095101, dragTime)
        Gumps.SendAction(949095101, gumpAction2)
        Gumps.WaitForGump(949095101, dragTime)
        Misc.Pause(120)
        #check keg level
        Items.WaitForProps(keg, dragTime)
    
    # move keg to butler
    Items.Move( keg , butler , 0 )
    Misc.Pause(dragTime)
    Journal.Clear()
    
def worldSave():
    if Journal.SearchByType('The world is saving, please wait.', 'Regular' ):
#    if Journal.SearchByType('The world will save in 1 minute.', 'Regular' ):
        Misc.SendMessage('Pausing for world save', 33)
        while not Journal.SearchByType('World save complete.', 'Regular'):
            Misc.Pause(1000)
        Misc.SendMessage('Continuing', 33)
        Journal.Clear()
    
Journal.Clear()
Misc.Pause(1000)
Mobiles.UseMobile(butler)
Misc.Pause(1000)

# check for dye tub, adjust buttons if yes
if Gumps.LastGumpTextExist( 'Remove Leather Tub?' ):
    Misc.SendMessage('Leather Tub Detected')
    fillList = [('explode',37),('strength',38),('refresh',39),('agility',40),('heal',41),('cure',42)]
else:
    fillList = [('explode',35),('strength',36),('refresh',37),('agility',38),('heal',39),('cure',40)]

while True:
    # verify its butler gump
    if Gumps.CurrentGump() == butlerGump:
        # iterate through fillList
        for i in fillList:
            # read gump line
            fillNumber = fillStopNumber - int(float(Gumps.LastGumpGetLine(i[1])))
            while fillNumber > 100: #int(float(Gumps.LastGumpGetLine(i[1]))) < fillStopNumber:
                Gumps.CloseGump(butlerGump)
                Misc.SendMessage('Filling ' + str(i[0])+ ', ' + str(fillNumber) + ' left', 66)
                Misc.Pause(dragTime)
                craftPot (i[0])
                Mobiles.UseMobile(butler)
                Misc.Pause(dragTime)
                fillNumber = fillStopNumber - int(float(Gumps.LastGumpGetLine(i[1])))
        Misc.SendMessage('Butler is as full as we can get it!', 66)
        Gumps.CloseGump(butlerGump)
        Stop
    else:
        Mobiles.UseMobile(butler)
        Misc.Pause(dragTime)
