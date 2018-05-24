#ItemIDS
axeType = 0x0F49
axeHue = 0x0000
hammerType = 0x13E3
hammerHue = 0x0000
ingotType = 0x1BF2
ingotHue = 0x0000

self_pack = Player.Backpack.Serial

#ItemSerials
trashcan = 0x4007B816
axeStorage = 0x40201DBF
beetleStorage = ''

def getByItemID(itemid, itemhue, source):
    # Find an item id in backpack and return the item object
    for item in Items.FindBySerial(source).Contains:
        if item.ItemID == itemid:
            return item
        else:
            Misc.NoOperation()
            
def smeltAxe():
    Misc.Pause(600)
    trashAxe = getByItemID(axeType, axeHue, self_pack)
    hammer = getByItemID(hammerType, hammerHue, self_pack)
    if Gumps.HasGump():
        Gumps.WaitForGump(949095101, 3500)
        Gumps.SendAction(949095101, 0)
        Misc.Pause(600)
    Items.UseItem(hammer)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 14)
    Target.WaitForTarget(10000, True)
    Target.TargetExecute(trashAxe.Serial)
    Misc.Pause(600)
    
def moveAxeToStorage():
    Items.UseItem(axeStorage)
    Misc.Pause(600)
    storageAxe = getByItemID(axeType, axeHue, self_pack)
    Items.Move(storageAxe, axeStorage, 1)
    Misc.Pause(600)

def searchJournal():
    if Journal.Search("slayer"):
        Misc.SendMessage('Slayer Item Crafted.', 98)
        moveAxeToStorage()
        Misc.Pause(600)
        Journal.Clear()
    else:
        Misc.SendMessage('No Slayer Item Crafted', 15)
        smeltAxe()
        Misc.Pause(600)
        Journal.Clear()
        
def dismount(mobileSerial):
    Misc.SendMessage('dismount')
    
def mount(mobileSerial):
    Misc.SendMessage('mount')

def moveToMobileStorage(mobileSerial):
    Misc.SendMessage('Move to Mobile')
        
def craftAxe():
    ingots = getByItemID(ingotType, ingotHue, self_pack)
    while ingots.Amount > 7:
        Journal.Clear()
        hammer = getByItemID(hammerType, hammerHue, self_pack)
        if Gumps.HasGump():
            Gumps.WaitForGump(949095101, 3500)
            Gumps.SendAction(949095101, 0)
            Misc.Pause(600)
        Items.UseItem(hammer)
        Gumps.WaitForGump(949095101, 3500)
        Gumps.SendAction(949095101, 50)
        Gumps.WaitForGump(949095101, 3500)
        Gumps.SendAction(949095101, 2)
        Gumps.WaitForGump(949095101, 3500)
        if not Gumps.HasGump():
            Misc.Pause(2000)
        searchJournal()
    
craftAxe()


