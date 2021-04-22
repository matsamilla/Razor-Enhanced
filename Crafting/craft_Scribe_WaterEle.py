restockBeetle = False

amountToMake = 5000
restockChest = 0x43510513
dragTime = 600
bp = 0x0F7A
bm = 0x0F7B
mr = 0x0F86
ss = 0x0F8D
pen = 0x0FBF
scroll = 0x0EF3
recall = 0x1F4C3
waterScroll = 0x1F6C
noColor = 0x0000
pack = Player.Backpack.Serial

beetle = 0x0023F0A0
beetleContainer = 0x439F1BD4 # Inspect item in beetle to get container

import sys
def craftRecall():
    pens = Items.FindByID(0x0FBF,-1,pack)
    Items.UseItem(pens)
    Gumps.WaitForGump(949095101, 2000)
    Gumps.SendAction(949095101, 22)
    Gumps.WaitForGump(949095101, 2000)
    Gumps.SendAction(949095101, 51)
    Gumps.WaitForGump(949095101, 2000)
    
    if Player.Mana < 20:
        med()
        
def craftWaterEle():
    pens = Items.FindByID(0x0FBF,-1,pack)
    Items.UseItem(pens)
    Gumps.WaitForGump(949095101, 2000)
    Gumps.SendAction(949095101, 50)
    Gumps.WaitForGump(949095101, 2000)
    Gumps.SendAction(949095101, 51)
    Gumps.WaitForGump(949095101, 2000)
    
    if Player.Mana < 20:
        med()
        
def med():
    Player.UseSkill('Meditation')
    Timer.Create('med', 7000)
    Misc.Pause(dragTime)
    while Player.Mana < Player.ManaMax:
        if not Player.BuffsExist('Meditation') and Timer.Check('med') == False:
            Misc.Pause(2000)
            Player.UseSkill('Meditation')
            Timer.Create('med', 7000)
        Misc.Pause(100)
    

def unload():
    scrolls = Items.FindByID(waterScroll, -1, pack)
    if scrolls:
        Items.Move(scrolls, restockChest, 0)
        Misc.Pause(dragTime)
        

def restock():

    if Items.BackpackCount(scroll, -1) < 1:
        Items.UseItem(restockChest)
        Misc.Pause(dragTime)
        scrolls = Items.FindByID (scroll ,-1,restockChest)
        Items.Move(scrolls, pack, 100)
        Misc.Pause(dragTime)
        unload()
        
    if Items.BackpackCount(ss, -1) < 1:
        Items.UseItem(restockChest)
        Misc.Pause(dragTime)
        sss = Items.FindByID (ss ,-1,restockChest)
        Items.Move(sss, pack, 100)
        Misc.Pause(dragTime)
        unload()
    
    if Items.BackpackCount(bm, -1) < 1:
        Items.UseItem(restockChest)
        Misc.Pause(dragTime)
        bms = Items.FindByID (bm ,-1,restockChest)
        Items.Move(bms, pack, 100)
        Misc.Pause(dragTime)
        unload()
        
    if Items.BackpackCount(mr, -1) < 1:
        Items.UseItem(restockChest)
        Misc.Pause(dragTime)
        mrs = Items.FindByID (mr ,-1,restockChest)
        Items.Move(mrs, pack, 100)
        Misc.Pause(dragTime)
        unload()
    
    if Items.BackpackCount(scroll, -1) < 1 or Items.BackpackCount(ss, -1) < 1 or Items.BackpackCount(bm, -1) < 1 or Items.BackpackCount(mr, -1) < 1:
        sys.exit()

for i in range(0,amountToMake):
    restock()    
    craftWaterEle()
    if Items.BackpackCount(pen, -1) < 1:
        Misc.SendMessage('Out of pens', 33)
        sys.exit()
