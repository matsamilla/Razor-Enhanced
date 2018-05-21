import sys

bp = 0x0F7A
mr = 0x0F86
ns = 0x0F88
ss = 0x0F8D
bm = 0x0F7B
chestSerial = 0x40428562
targetMobile = 0x001C82BD
backpackList = []

def getByItemID(itemid, source):
    """find an item id in backpack"""
    for item in Items.FindBySerial(source).Contains:
        if item.ItemID == itemid:
            return item
        else:
            Misc.NoOperation()

def trainMagery():
    while True:
        while Player.Mana < 40:
            meditate()
        getReagents([bp, mr, ss, bm], chestSerial)
        Misc.Pause(600)
        Spells.CastMagery('Mana Vampire')
        Target.WaitForTarget(6000,True)
        Target.TargetExecute(targetMobile)
        Misc.Pause(600)
    
def meditate():
    Player.UseSkill('Meditation')
    Misc.Pause(8500)
    
def getReagents(listOfReagentsRequired, source):
    for reagent in listOfReagentsRequired:
        backpackList = []
        for r in Player.Backpack.Contains:
            backpackList.append(r.ItemID)
        if reagent not in backpackList:
            reg = getByItemID(reagent, chestSerial)
            Items.UseItem(chestSerial)
            Misc.Pause(600)
            Misc.SendMessage(reg.Name)
            Items.Move(reg, Player.Backpack, 1)
            Misc.Pause(600)
    
trainMagery()