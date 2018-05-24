pouchType = 0x0E79
pouchHue = 0x0026
self_pack = Player.Backpack.Serial

def getByItemID(itemid, itemhue, source):
    # Find an item id in backpack and return the item object
    for item in Items.FindBySerial(source).Contains:
        if item.ItemID == itemid and item.Hue == itemhue:
            return item
        else:
            Misc.NoOperation()
            
def usePouch():
    pouch = getByItemID(pouchType, pouchHue, self_pack)
    if pouch is not None:
        Misc.SendMessage('POUCH', 37)
        Items.UseItem(pouch)
    else:
        Misc.SendMessage('_NO POUCH_', 47)
        
usePouch()