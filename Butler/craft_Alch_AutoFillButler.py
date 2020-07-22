# Automatic Potion Butler Filler by MatsaMilla
# Must have TOOLTIPSON ([toggletooltips in game to turn off/on)
# Target items requested
# Makes Make sure restock chest & motar bags are open
# For best results have refill keg in backpack


butler = Target.PromptTarget('Target Butler')
restockChest = Target.PromptTarget('Target Restock Chest')
kegTarget =  Target.PromptTarget('Target keg to fill (optional)')
mortarBag = Target.PromptTarget('Mortar Restock Bag (optional)')

if kegTarget != -1:
    Misc.SendMessage('Using targeted Keg', 66)
    keg = Items.FindBySerial(kegTarget)
else:
    keg = Items.FindByID( 0x1940 , -1 ,  Player.Backpack.Serial )
    if keg:
        Misc.SendMessage('Using keg in pack', 66)
    else:
        Misc.SendMessage('Need a keg', 33)

fillStopNumber = 4900
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
    
    while not Items.GetPropValue(keg,'The Keg Is Completely Full.'): #not Journal.SearchByType('The keg will not hold any more!', 'Regular'):
        # find mortar, even if nested in backpack
        mortar = FindItem( 0x0E9B , Player.Backpack )
        if not mortar:
            if mortarBag != -1:
                mortarFound = Items.FindByID(0x0E9B , -1 , mortarBag)
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
        if Items.BackpackCount(regID) < 10:
            regFound = Items.FindByID( regID, -1, restockChest)
            Items.WaitForProps( regFound.Serial , dragTime)
            if regFound:
                Items.Move( regFound, Player.Backpack , 250 )
                Misc.Pause(dragTime)
                if Items.BackpackCount(regID) < 10:
                    Misc.SendMessage('Out of regs for this pot type, moving to next pot', 33)
                    break
            else:
                Misc.SendMessage('Out of regs for this pot type, moving to next pot', 33)
                break
#            if Items.BackpackCount(regID) < 10:
#                Misc.SendMessage('Out of regs for this pot type, moving to next pot', 33)
#                break
            
            
        # move pot to keg  
        pot = FindItem( potID , Player.Backpack)
        while pot:
            Items.Move(pot, keg, 0)
            Misc.Pause(dragTime)
            pot = FindItem( potID , Player.Backpack)
        
        # make sure you have empty bottle
        if Items.BackpackCount(0x0F0E) < 1:
            emptyPot = Items.FindByID( 0x0F0E, -1, restockChest)
            Items.Move(emptyPot, Player.Backpack.Serial, 1)
            Misc.Pause(dragTime)
        
#        #make sure you have empty bottle
#        if Gumps.LastGumpTextExist('You need an empty bottle to make a potion.'):
#            pot = FindItem( potID , Player.Backpack)
#            Misc.SendMessage('Moving Pot')
#            Items.Move(pot, keg, 0)
#            Misc.Pause(dragTime)
            
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
        Items.WaitForProps(keg, dragTime)
    
    # move keg to butler
    Items.Move( keg , butler , 0 )
    Misc.Pause(dragTime)
    Journal.Clear()
    



Journal.Clear()
Mobiles.UseMobile(butler)
Misc.Pause(1000)
if Gumps.LastGumpTextExist( 'Remove Leather Tub?' ):
    Misc.SendMessage('Leather Tub Detected')
    fillList = [('explode',37),('strength',38),('refresh',39),('agility',40),('heal',41),('cure',42)]
else:
    fillList = [('explode',35),('strength',36),('refresh',37),('agility',38),('heal',39),('cure',40)]

while True:
    
    if Gumps.CurrentGump() == butlerGump:
        for i in fillList:
            while int(Gumps.LastGumpGetLine(i[1])) < fillStopNumber:
                Gumps.CloseGump(butlerGump)
                Misc.SendMessage('Filling ' + i[0], 66)
                Misc.Pause(dragTime)
                craftPot (i[0])
                Mobiles.UseMobile(butler)
                Misc.Pause(dragTime)
        Misc.SendMessage('Butler is as full as we can get it!', 66)
        Stop
    else:
        Mobiles.UseMobile(butler)
        Misc.Pause(dragTime)
