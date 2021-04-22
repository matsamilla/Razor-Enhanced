# Automatic Potion Butler Filler by MatsaMilla 
#   - Version 2, updated 1/5/21

# NEED: Restock Chest (containing BARBED leather / tailor kits (or ignots if you have tinkering))

#*******************************************************************#

Player.HeadMessage(66,'Target Butler')
butler = Target.PromptTarget('Target Butler')
Player.HeadMessage(66,'Target Restock Chest')
restockChest = Items.FindBySerial( Target.PromptTarget('Target Restock Chest') )

fillStopNumber = 50
dragTime = 800
butlerGump = 989312372

import sys
def setValues( armorValue , gump ):
    global armorID
    global gumpAction
    armorID = armorValue
    gumpAction = gump


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
            
def craftArmor(armor, amount):
    sewKit = FindItem( 0x0F9D , Player.Backpack )
    if not sewKit:
        restock()
        
    if armor == 'cap':
        setValues( 0x1DB9 , 9 )
    elif armor == 'gorget':
        setValues( 0x13C7 , 2)
    elif armor == 'arms':
        setValues( 0x13CD , 23 )
    elif armor == 'gloves':
        setValues( 0x13C6 , 16 )
    elif armor == 'chest':
        setValues( 0x13CC , 37 )
    elif armor == 'legs':
        setValues( 0x13CB , 30 )
    else:
        Misc.SendMessage('potType not defined, stopping', 33)
        sys.exit()
    while amount > 0:
        worldSave()
        restock()
        
        if Gumps.CurrentGump() != 949095101:
            sewKit = FindItem( 0x0F9D , Player.Backpack )
            Items.UseItem(sewKit)
            Gumps.WaitForGump(949095101, dragTime)
            # change to barbed
            Gumps.WaitForGump(949095101, dragTime)
            Gumps.SendAction(949095101, 7)
            Gumps.WaitForGump(949095101, dragTime)
            Gumps.SendAction(949095101, 27)
            Gumps.WaitForGump(949095101, dragTime)
        Gumps.SendAction(949095101, 36)
        Gumps.WaitForGump(949095101, dragTime)
        Gumps.SendAction(949095101, gumpAction)
        Gumps.WaitForGump(949095101, dragTime)
        Misc.Pause(200)
        restock()
        # move crafted armor to butler
        craftedArmor = FindItem( armorID , Player.Backpack)
        while craftedArmor:
            Items.Move(craftedArmor, butler, 0)
            Misc.Pause(dragTime)
            craftedArmor = FindItem( armorID , Player.Backpack)
            amount = amount - 1
            if amount < 1:
                break
        if amount < 1:
            break
        
def restock():
    
    leather = FindItem( 0x1081 , Player.Backpack, 0x059d )
    if not leather or leather.Amount < 12:
        leatherRestock = FindItem( 0x1081 , restockChest, 0x059d)
        if leatherRestock:
            Items.Move( leatherRestock , Player.Backpack , 200 )
            Misc.Pause(dragTime)
        else:
            Misc.SendMessage( 'No more leather' , 33 )
            sys.exit()
        
    sewKit = FindItem( 0x0F9D , Player.Backpack )
    if sewKit == None:
        if Player.GetRealSkillValue('Tinkering') > 80:
            tinkTool = FindItem( 0x1EB8 , Player.Backpack )
            if tinkTool:
                Items.UseItem(tinkTool)
                Gumps.WaitForGump(949095101, dragTime)
                Gumps.SendAction(949095101, 8)
                Gumps.WaitForGump(949095101, dragTime)
                Gumps.SendAction(949095101, 44)
                Gumps.WaitForGump(949095101, dragTime)
                Misc.Pause(200)
                Gumps.CloseGump(949095101)
        else:
            restockSewKit = FindItem( 0x0F9D , restockChest )
            if restockSewKit:
                Items.Move( restockSewKit , Player.Backpack , 200 )
                Misc.Pause(dragTime)
            else:
                Misc.SendMessage( 'No more sewing kits' , 33 )
                sys.exit()
    
def worldSave():
    if Journal.SearchByType('The world is saving, please wait.', 'Regular' ):
        Misc.SendMessage('Pausing for world save', 33)
        while not Journal.SearchByType('World save complete.', 'Regular'):
            Misc.Pause(1000)
        Misc.SendMessage('Continuing', 33)
        Journal.Clear()
    
Journal.Clear()
Misc.Pause(1000)
Mobiles.UseMobile(butler)
Misc.Pause(1000)

fillList = [('cap',4),('gorget',5),('arms',6),('gloves',7),('chest',8),('legs',9)]

while True:
    # verify its butler gump
    if Gumps.CurrentGump() == butlerGump:
        # iterate through fillList
        for i in fillList:
            # read gump line
            fillNumber = fillStopNumber - int(float(Gumps.LastGumpGetLine(i[1])))
            while fillNumber > 0: #int(float(Gumps.LastGumpGetLine(i[1]))) < fillStopNumber:
                if Gumps.CurrentGump() == butlerGump:
                    Gumps.CloseGump(butlerGump)
                Misc.SendMessage('Filling ' + str(i[0])+ ', ' + str(fillNumber) + ' left', 66)
                Misc.Pause(dragTime)
                craftArmor (i[0], fillNumber)
                Mobiles.UseMobile(butler)
                Misc.Pause(dragTime)
                fillNumber = fillStopNumber - int(float(Gumps.LastGumpGetLine(i[1])))
        Misc.SendMessage('Butler is as full as we can get it!', 66)
        Gumps.CloseGump(butlerGump)
        sys.exit()
    else:
        Mobiles.UseMobile(butler)
        Misc.Pause(dragTime)
