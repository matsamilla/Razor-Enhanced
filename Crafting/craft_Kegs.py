from System.Collections.Generic import List
import sys
# Empty Potion Keg Maker by MatsaMilla Version 1.1
# Target restock container, then container for empty potion kegs
# will make as many as maxToMake, or until mats run out
maxToMake = 120

journalPause = 120
dragTime = 600

kegGump1 = 15
kegGump2 = 163
lidGump1 = 1
lidGump2 = 9
stavesGump1 = 1
stavesGump2 = 2
hoopGump1 = 15
hoopGump2 = 37
barrelTap1 = 15
barrelTap2 = 16
potionKegGump1 = 43
potionKegGump2 = 44
tinkKitGump1 = 8
tinkKigGump2 = 23
sawGump1 = 8
sawGump2 = 51
ignot = 0x1BF2
wood = 0x1BD7
tink = 0x1EB8
saw = 0x1034
bottle = 0x0F0E
hoop = 0x1DB7
stave = 0x1EB1
lid = 0x1DB8
tap = 0x1004

def tinkCraft (gump1, gump2):
    Gumps.CloseGump(949095101)
    currentTink = FindItem(tink,Player.Backpack)
    if Gumps.CurrentGump() != 949095101:
        Items.UseItem(currentTink)
    Gumps.WaitForGump(949095101, 1500)
    Gumps.SendAction(949095101, gump1)
    Gumps.WaitForGump(949095101, 1500)
    Gumps.SendAction(949095101, gump2)
    Gumps.WaitForGump(949095101, 1500)
    Misc.Pause(journalPause)
    
def carpCraft (gump1, gump2):
    Gumps.CloseGump(949095101)
    currentsaw = FindItem(saw,Player.Backpack)
    if Gumps.CurrentGump() != 949095101:
        Items.UseItem(currentsaw)
    Gumps.WaitForGump(949095101, 1500)
    Gumps.SendAction(949095101, gump1)
    Gumps.WaitForGump(949095101, 1500)
    Gumps.SendAction(949095101, gump2)
    Gumps.WaitForGump(949095101, 1500)
    Misc.Pause(journalPause)
    
def craftKegs(i):
    for i in range( 0, i ):
        craftKeg()

def craftKeg():
    checkMats ()
    while Items.BackpackCount(stave,-1) < 3:
        carpCraft(stavesGump1, stavesGump2)
        checkMats ()
    while Items.BackpackCount(lid,-1) < 2:
        carpCraft(lidGump1, lidGump2)
        checkMats ()
    if Items.BackpackCount(hoop,-1) < 1:
        tinkCraft(hoopGump1, hoopGump2)
    checkMats ()
    if Items.BackpackCount(tap,-1) < 1:
        tinkCraft(barrelTap1, barrelTap2)
    checkMats ()
    carpCraft(kegGump1, kegGump2)
    checkMats ()
    tinkCraft(potionKegGump1, potionKegGump2)
    moveKegs(potionKegContainer)
    
def restock(container):
    restockWood = FindItem(wood, container,0x0000)
    if Items.BackpackCount(wood, -1) < 19:
        if restockWood:
            Items.Move(restockWood, Player.Backpack, 500)
        Misc.Pause(dragTime)
    restockIgnots = FindItem(ignot, container)
    if Items.BackpackCount(ignot, -1) < 10:
        if restockIgnots:
            Items.Move(restockIgnots, Player.Backpack, 100)
            Misc.Pause(dragTime)
    restockBottle = FindItem(bottle, container)
    if Items.BackpackCount(bottle, -1) < 10:
        if restockBottle:
            Items.Move(restockBottle, Player.Backpack, 100)
            Misc.Pause(dragTime)
        
def moveKegs(container):
    potionKeg = FindItem(0x1940, Player.Backpack)
    while potionKeg:
        Items.Move(potionKeg, container, 0)
        Misc.Pause(dragTime)
        potionKeg = FindItem(0x1940, Player.Backpack)
        if Journal.Search('That container cannot hold more weight.'):
            Player.HeadMessage(33, 'Potion container full, stopping')
            sys.exit()
    
def checkMats ():
    # Stop if low on iron
    if Items.BackpackCount(ignot, -1) < 10:
        restock(restockContainer)
        Misc.Pause(journalPause)
        if Items.BackpackCount(ignot, -1) < 10:
            Misc.SendMessage('Out of Ignots',33)
            sys.exit()
    # Stop if low on wood
    if Items.BackpackCount(wood, -1) < 19:
        restock(restockContainer)
        Misc.Pause(journalPause)
        if Items.BackpackCount(wood, -1) < 19:
            Misc.SendMessage('Out of Wood',33)
            sys.exit()
            
    # Stop if low on bottles
    if Items.BackpackCount(bottle, -1) < 10:
        restock(restockContainer)
        Misc.Pause(journalPause)
        if Items.BackpackCount(bottle, -1) < 10:
            Misc.SendMessage('Out of Bottles',33)
            sys.exit()
    # always have 2 tinker kits
    if Items.BackpackCount(tink, -1) < 2:
        tinkCraft (tinkKitGump1, tinkKigGump2)
    # craft saw
    if Items.BackpackCount(saw, -1) < 1:
        tinkCraft (sawGump1, sawGump2)
        

        
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
            
    
    
restockContainer = Items.FindBySerial( Target.PromptTarget('Target Restock Container') )
potionKegContainer = Items.FindBySerial( Target.PromptTarget('Target Bag for Potion Kegs'))
Items.UseItem(restockContainer)
Misc.Pause(dragTime)
Journal.Clear()
craftKegs(maxToMake)
