# Bent Rod Crafter by MatsaMilla
# Last edit: Matsamilla 6/4/19

# Moves bent rods to beetle

from System.Collections.Generic import List
import winsound

#***************SETUP SECTION**********************************
#ItemSerials
beetle = 0x00215F22
keepGM = False # true to keep all GM rods too
keepCount = 30 # how many GM rods to keep
#**************************************************************

error = "Sounds2\error.wav"
dragTime = 600
saw = 0x1034
tink = 0x1EB8
cloth = 0x1766
wood = 0x1BD7
logs = 0x1BDD
ignot = 0x1BF2
pole = 0x0DBF
noColor = 0x0000
self_pack = Player.Backpack.Serial
self = Player.Serial
gmCount = 0

# Use neraby trashcan
trashBarrelFilter = Items.Filter()
trashBarrelFilter.OnGround = 1
trashBarrelFilter.Movable = False
trashBarrelFilter.RangeMin = 0
trashBarrelFilter.RangeMax = 2
trashBarrelFilter.Graphics = List[int]( [ 0x0E77 ] )
trashBarrelFilter.Hues = List[int]( [ 0x03B2 ] )
trashcanhere = Items.ApplyFilter( trashBarrelFilter )

if trashcanhere:
    global trashcan
    for t in trashcanhere:
        trashcan = t
else:
    Misc.SendMessage('No trashcan nearby, stopping',33)
    Misc.ScriptStop('craft_BentRod.py')

if keepGM:
    Mobiles.UseMobile(self)
    Misc.Pause(dragTime)
    Mobiles.SingleClick(beetle)
    Misc.WaitForContext(beetle, 1500)
    Misc.ContextReply(beetle, "Open Backpack")
    Misc.Pause(dragTime)
    gmBag = Target.PromptTarget('Select Bag for GM Rods')
    
def moveToBeetle():
    global gmCount
    if keepGM:
        if gmRod:
            gmCount = gmCount +1
            Misc.SendMessage(gmCount)
            if Player.Mount:
                Mobiles.UseMobile(self)
                Misc.Pause(dragTime)
                Items.Move(bentRod, gmBag, 1)
                Misc.Pause(dragTime)
                Mobiles.UseMobile(beetle)
                Misc.Pause(dragTime)
            if gmCount == keepCount:
                Misc.SendMessage('GM Rod Count Reached, stopping.',33)
                winsound.PlaySound(error, winsound.SND_FILENAME)
                Misc.ScriptStop('craft_Carp_BentRod.py')
        else:
            if Player.Mount:
                Mobiles.UseMobile(self)
                Misc.Pause(dragTime)
                Items.Move(bentRod, beetle, 1)
                Misc.Pause(dragTime)
                Mobiles.UseMobile(beetle)
                Misc.Pause(dragTime)
        
    else:
        if Player.Mount:
            Mobiles.UseMobile(self)
            Misc.Pause(dragTime)
            Items.Move(bentRod, beetle, 1)
            Misc.Pause(dragTime)
            Mobiles.UseMobile(beetle)
            Misc.Pause(dragTime)
        
def trashPole():
    if trashcan:
        Items.Move(bentRod, trashcan.Serial, 1)
        Misc.Pause(dragTime)
    else:
        Misc.SendMessage('No trashcan nearby, stopping',33)
        Misc.ScriptStop('craft_BentRod.py')
    
def hide():
    if not Player.BuffsExist('Hiding'):
        Player.UseSkill('Hiding')

def checkMats():
    if Items.BackpackCount(cloth, -1) < 5:
        Misc.SendMessage('Out of Cloth',33)
        winsound.PlaySound(error, winsound.SND_FILENAME)
        Misc.ScriptStop('craft_Carp_BentRod.py')
        
    if Items.BackpackCount(wood, -1) < 5 and Items.BackpackCount(logs, -1) < 5:
        Misc.SendMessage('Out of Wood',33)
        winsound.PlaySound(error, winsound.SND_FILENAME)
        Misc.ScriptStop('craft_Carp_BentRod.py')
        
    if Items.BackpackCount(saw, noColor) < 1:
        craftTools()
            
def craftTools():
    currentTink = Items.FindByID(tink, -1, -1)
    
    if Items.BackpackCount(ignot, noColor) < 10:
        Misc.SendMessage('Out of Ignots',33)
        winsound.PlaySound(error, winsound.SND_FILENAME)
        Misc.ScriptStop('craft_BentRod.py')
    
    if Items.BackpackCount(tink, noColor) < 2:
        Items.UseItem(currentTink.Serial)
        Gumps.WaitForGump(949095101, 1500)
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101, 1500)
        Gumps.SendAction(949095101, 23)

    if Items.BackpackCount(saw, noColor) < 1:
        Items.UseItem(currentTink.Serial)
        Gumps.WaitForGump(949095101,1500)
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101,1500)
        Gumps.SendAction(949095101, 51)

def craftPole():
    if not Player.Mount:
        Mobiles.UseMobile(beetle)
        Misc.Pause(dragTime)
    currentSaw = Items.FindByID(saw, -1, -1)
    if currentSaw:
        Items.UseItem(currentSaw)
        Gumps.WaitForGump(949095101,1500)
        Gumps.SendAction(949095101, 22)
        Gumps.WaitForGump(949095101, 1500)
        Gumps.SendAction(949095101, 37)
        Misc.Pause(2000)
    
def bentRodCheck():
    global bentRod
    global gmRod
    bentRod = Items.FindByID(pole, -1, self_pack)
    gmRod = False
    
    
    if bentRod:
        if keepGM:
            Items.SingleClick(bentRod.Serial)
            Misc.Pause(dragTime)
            if Journal.Search('a bent rod'):
                moveToBeetle()
                Journal.Clear()
            elif Journal.Search('Exceptional'):
                gmRod = True
                moveToBeetle()
                Journal.Clear()
            else:
                trashPole()
        else:
            Items.SingleClick(bentRod.Serial)
            Misc.Pause(dragTime)
            if Journal.Search('a bent rod'):
                moveToBeetle()
                Journal.Clear()
            else:
                trashPole()
            
while True:
    Journal.Clear()
    if Player.GetRealSkillValue('Hiding') > 30:
        hide() 
    checkMats()           
    craftPole()
    while Items.BackpackCount(pole, -1) > 0:
        bentRodCheck()
