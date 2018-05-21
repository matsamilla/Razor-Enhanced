bandagesType = 0x0E21
bandagesChest = 0x41CE34DA
            
def getByItemID(itemid, source):
    """find an item id in backpack"""
    for item in Items.FindBySerial(source).Contains:
        if item.ItemID == itemid:
            return item
        else:
            Misc.NoOperation()

# Heal when below 70%; mostly for training purposes
def healBelow70():
    while True:
        bandages = getByItemID(bandagesType, Player.Backpack.Serial)
        while Player.Hits < 70:
            if bandages.Amount < 2:
                Player.Run('West')
                Player.Run('West')
                Player.Run('West')

                #bandagesFromChest = getByItemID(bandagesType, bandagesChest)
                #Items.UseItem(bandagesChest)
                #Misc.Pause(600)
                #Misc.SendMessage(bandagesFromChest.Name)
                #Items.Move(bandagesFromChest, Player.Backpack, 200)
                #Misc.Pause(600)
            Items.UseItem(bandages)
            Target.WaitForTarget(7000,False)
            Target.Self()

healBelow70()