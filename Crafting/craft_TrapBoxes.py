# Trap Box Maker by MatsaMilla
# make sure to have plenty of wood and some ignots on crafter
# place as many explostion pots on crafter as boxes you want to make
from System.Collections.Generic import List

type = 2 # 2 for box, 9 for crate
dragTime = 600
saw = 0x1034
tink = 0x1EB8
wood = 0x1BD7
ignot = 0x1BF2
expPot = 0x0F0D
amountToMake = Items.BackpackCount(expPot, -1)

trapBox = [0x9aa,0x9a9,0xe3e,0xe3c,0xe42,0xe43,0x280b,0xe7d,0xe7e,0xe3f,0xe3d,0x280c]

def craftTools():
    currentTink = Items.FindByID(tink, -1, -1)
    
    if Items.BackpackCount(ignot, -1) < 10:
        Misc.SendMessage('Out of Ignots',33)
        winsound.PlaySound(error, winsound.SND_FILENAME)
        Misc.ScriptStop('craft_BentRod.py')
    
    if Items.BackpackCount(tink, -1) < 2:
        Items.UseItem(currentTink.Serial)
        Gumps.WaitForGump(949095101, 1500)
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101, 1500)
        Gumps.SendAction(949095101, 23)

    if Items.BackpackCount(saw, -1) < 1:
        Items.UseItem(currentTink.Serial)
        Gumps.WaitForGump(949095101,1500)
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101,1500)
        Gumps.SendAction(949095101, 51)
    
    Gumps.CloseGump(949095101)

# 2 for box, 9 for crate        
def craftBox(amount, type):
    i = 0
    while i < amount:
        currentSaw = Items.FindByID(saw, -1, -1)
        if currentSaw:
            if Gumps.CurrentGump != 949095101:
               Items.UseItem(currentSaw)
            
            Gumps.WaitForGump(949095101, 3000)
            Gumps.SendAction(949095101, 15)
            Gumps.WaitForGump(949095101, 3000)
            Gumps.SendAction(949095101, type)
            Gumps.WaitForGump(949095101, 3000)
            i = i + 1
        else:
            craftTools()
    Gumps.CloseGump(949095101)
            
# trap
def trapBoxes():
    trapList = []
    for i in Player.Backpack.Contains:
        if i.ItemID in trapBox:
            trapList.append( i.Serial )
    for t in trapList:
        currentTink = Items.FindByID( tink , -1 , -1 )
        if currentTink:
            if Gumps.CurrentGump != 949095101:
                Items.UseItem(currentTink)
            Gumps.WaitForGump(949095101, 3000)
            Gumps.SendAction(949095101, 50)
            Gumps.WaitForGump(949095101, 3000)
            Gumps.SendAction(949095101, 16)
            Target.WaitForTarget(8000, False)
            Target.TargetExecute(t)

craftBox(amountToMake, type)            
trapBoxes()
