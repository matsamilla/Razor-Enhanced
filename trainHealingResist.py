
bandageType = 0x0E21
self_pack = Player.Backpack.Serial

def getByItemID(itemid, source):
    """find an item id in backpack"""
    for item in Items.FindBySerial(source).Contains:
        if item.ItemID == itemid:
            return item
        else:
            Misc.NoOperation()
            
def readJournalWait():
    bool = True
    maxwait = 0
    while bool:
        Misc.SendMessage('waiting ' + str(maxwait) + ' ms', 47)
        bool = not Journal.Search('they barely help')
        if not bool:
            break
        bool = not Journal.Search('finish applying the bandages')
        if not bool:
            break
        Misc.Pause(500)
        maxwait += 500
        if maxwait >= 18000:
            break
    Journal.Clear()

def trainHealingResist():
    while True:
        bandages = getByItemID(bandageType, self_pack)
        Journal.Clear()
        if Player.Hits > 90 and bandages.Amount > 2:
            while Player.Mana < 60:
                Player.UseSkill('Meditation')
                Misc.Pause(8000)
            Spells.CastMagery('Flamestrike')
            Target.WaitForTarget(7000)
            Target.Self()
            Misc.Pause(1200)
        if Player.Hits < 95 and bandages.Amount > 2:
            Items.UseItem(bandages)
            Target.WaitForTarget(5000)
            Target.Self()
            Journal.Clear()
            readJournalWait()
            
trainHealingResist()
        