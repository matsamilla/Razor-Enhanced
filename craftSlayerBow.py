#ItemIDS
bowType = 0x13B2
fletchingType = 0x1022
boardType = 0x1BD7

#ItemSerials
trashcan = 0x4007B816
bowStorage = 0x40F52E4E
beetleStorage = ''

def getByItemID(itemid):
    # Find an item id in backpack and return the item object
    for item in Player.Backpack.Contains:
        if item.ItemID == itemid:
            return item
        else:
            Misc.NoOperation()
            
def moveBowToTrash():
    Items.UseItem(trashcan)
    Misc.Pause(600)
    trashBow = getByItemID(bowType)
    Items.Move(trashBow, trashcan, 1)
    Misc.Pause(600)
    
def moveBowToStorage():
    Items.UseItem(bowStorage)
    Misc.Pause(600)
    storageBow = getByItemID(bowType)
    Items.Move(storageBow, bowStorage, 1)
    Misc.Pause(600)

def searchJournal():
    if Journal.Search("slayer"):
        Misc.SendMessage('Slayer Item Crafted.', 98)
        moveBowToStorage()
        Misc.Pause(600)
        Journal.Clear()
    else:
        Misc.SendMessage('No Slayer Item Crafted', 15)
        moveBowToTrash()
        Misc.Pause(600)
        Journal.Clear()
        
def dismount(mobileSerial):
    Misc.SendMessage('dismount')
    
def mount(mobileSerial):
    Misc.SendMessage('mount')

def moveToMobileStorage(mobileSerial):
    Misc.SendMessage('Move to Mobile')
        
def craftBow():
    boards = getByItemID(boardType)
    while boards.Amount > 7:
        Journal.Clear()
        fletching = getByItemID(fletchingType)
        Items.UseItem(fletching)
        Gumps.WaitForGump(949095101, 3000)
        Gumps.SendAction(949095101, 15)
        Gumps.WaitForGump(949095101, 3000)
        Gumps.SendAction(949095101, 2)
        Gumps.WaitForGump(949095101, 3000)
        if not Gumps.HasGump():
            Misc.Pause(2000)
        searchJournal()
    
craftBow()


    