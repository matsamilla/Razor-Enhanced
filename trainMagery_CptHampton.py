import sys

bp = 0x0F7A
mr = 0x0F86
ns = 0x0F88
ss = 0x0F8D
bm = 0x0F7B
chestSerial = 0x40428562
targetMobile = 0x0002CF77
backpackList = []

def getByItemID(itemid, source):
    """find an item id in backpack"""
    for item in Items.FindBySerial(source).Contains:
        if item.ItemID == itemid:
            return item
        else:
            Misc.NoOperation()

def trainMagery():
    while Player.GetSkillValue('Magery') <= 62.8:
        while Player.Mana < 11:
            while Player.ManaMax < 11:
                raiseInt(targetMobile)
            meditate()
        getReagents([bp, mr, ss], chestSerial)
        Misc.Pause(600)
        Spells.CastMagery('Mana Drain')
        Target.WaitForTarget(6000,True)
        Target.SelfQueued()
        Misc.Pause(600)
        
    while Player.GetSkillValue('Magery') > 62.8 and Player.GetSkillValue('Magery') <= 75.5:
        while Player.Mana < 20:
            while Player.ManaMax < 20:
                raiseInt(targetMobile)
            meditate()
        getReagents([bm, ns], chestSerial)
        Misc.Pause(600)
        Spells.CastMagery('Invisibility')
        Target.WaitForTarget(6000,True)
        Target.SelfQueued()
        Misc.Pause(600)
        
    while Player.GetSkillValue('Magery') > 75.5 and Player.GetSkillValue('Magery') < 100:
        while Player.Mana < 40:
            while Player.ManaMax < 40:
                raiseInt(targetMobile)
            meditate()
        getReagents([bp, bm, mr, ss], chestSerial)
        Misc.Pause(600)
        Spells.CastMagery('Mana Vampire')
        Target.WaitForTarget(6000,True)
        Target.SelfQueued()
        Misc.Pause(600)
        
    if Player.GetSkillValue('Magery') == 100:
        sys.exit
    
def meditate():
    Player.UseSkill('Meditation')
    Misc.Pause(8500)

def raiseInt(target):
    Player.UseSkill('Evaluating Intelligence')
    Target.ClearQueue
    Target.WaitForTarget(7000, False)
    Target.TargetExecute(target)
    Misc.Pause(7000)
    
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
