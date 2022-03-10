# Craft Summon Water Elemental Scrolls, by MatsaMilla
#     - updated 3/10/22

# Put all crafting materials in a secured chest in your house, then target it.
# it will make as many as it can from the materials in the chest. 

Player.HeadMessage(66,'Target the OPENED Restock Chest')
restockChest = Target.PromptTarget()
dragTime = 600
bp = 0x0F7A
bm = 0x0F7B
mr = 0x0F86
ss = 0x0F8D
scroll = 0x0EF3
waterScroll = 0x1F6C
import sys

if Player.GetRealSkillValue('Inscription') < 100:
    Player.HeadMessage(33,"Wait, you arent even GM scribe? Git Gud")
    sys.exit()
        
def craftWaterEle():
    if not Gumps.CurrentGump() == 949095101:
        pen = Items.FindByID(0x0FBF,-1,Player.Backpack.Serial)
        if pen:
            Items.UseItem(pen)
        else:
            restock()
        Gumps.WaitForGump(949095101, 2000)
    Gumps.SendAction(949095101, 50)
    Gumps.WaitForGump(949095101, 2000)
    Gumps.SendAction(949095101, 51)
    Gumps.WaitForGump(949095101, 5000)
    
    # mana check
    if Player.Mana < 50:
        
        Player.UseSkill('Meditation')
        
        # dont do anything until full mana
        while Player.Mana < Player.ManaMax:
            Misc.Pause(100)

def unload():
    if Items.BackpackCount(waterScroll,-1) > 100:
        elescrolls = Items.FindByID(waterScroll, -1, Player.Backpack.Serial)
        if elescrolls:
            Items.Move(elescrolls, restockChest, 0)
            Misc.Pause(dragTime)
        

def restock():
    # restock pen, stop if out
    if Items.BackpackCount(0x0FBF, -1) < 1:
        restockPen = Items.FindByID (0x0FBF ,-1,restockChest, True)
        if restockPen:
            Items.Move(restockPen,Player.Backpack.Serial,1)
            Misc.Pause(dragTime)
        else:
            Player.HeadMessage(33,'Out of pens')
            sys.exit()

    # restock scrolls, stop if out
    if Items.BackpackCount(scroll, -1) < 1:
        scrolls = Items.FindByID (scroll ,-1,restockChest, True)
        if scrolls:
            Items.Move(scrolls, Player.Backpack.Serial, 100)
            Misc.Pause(dragTime)
        else:
            Player.HeadMessage(33,'Out of blank scrolls')
            sys.exit()
        
    # restock silk, stop if out
    if Items.BackpackCount(ss, -1) < 1:
        silk = Items.FindByID (ss ,-1,restockChest, True)
        if silk:
            Items.Move(silk, Player.Backpack.Serial, 100)
            Misc.Pause(dragTime)
        else:
            Player.HeadMessage(33,'Out of silk')
            sys.exit()
    
    # restock moss, stop if out
    if Items.BackpackCount(bm, -1) < 1:
        bloodmoss = Items.FindByID (bm ,-1,restockChest, True)
        if bloodmoss:
            Items.Move(bloodmoss, Player.Backpack.Serial, 100)
            Misc.Pause(dragTime)
        else:
            Player.HeadMessage(33,'Out of blood moss')
            sys.exit()
        
    # restock root, stop if out
    if Items.BackpackCount(mr, -1) < 1:
        root = Items.FindByID (mr ,-1,restockChest, True)
        if root:
            Items.Move(root, Player.Backpack.Serial, 100)
            Misc.Pause(dragTime)
        else:
            Player.HeadMessage(33,'Out of mandrake root')
            sys.exit()
        unload()
    
    
    unload()

while True:
    restock()    
    craftWaterEle()
   
