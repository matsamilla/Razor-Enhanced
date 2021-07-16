from System.Collections.Generic import List
import sys
# Dragon Armor Crafter by MatsaMilla
# ToolTips must be enabled and must have a beetle
# Target a bag with empty bags in it, it will fill the empty bags with dragon armor
####################################################

scaleColor = 'blue' #pick color of scales, red, yellow, black, green, white, blue or blue2

fillBags = True # if true: Fill a bag with as many 
                # bags as you want to fill with armor sets.
                # Make sure bag is on beetle, lot of weight.

beetle = 0x00215F22
beetlePack = 0x434C292B # beetle container ID (inspect object in beetle pack for container ID

#####################################################

noColor = 0x0000
self_pack = Player.Backpack.Serial
self = Player.Serial
dragTime = 600
gmCheckDelay = 200
craftTime = 1000
gumpTimeout = 4000

dragonLegs = 0x2647
dragonTunic = 0x2641
dragonSleeves = 0x2657
dragonGloves = 0x2643
dragonHelm = 0x2645
dragonGorget = 0x2B69
dragonSuit = [(44,0x2643),(51,0x2B69),(58,0x2645),(65,0x2647),(72,0x2657),(79,0x2641)]

dragonScales = 0x26B4

smithHammer = 0x13E3

if scaleColor == 'red':
    scaleColorGumpAction = 6
elif scaleColor == 'yellow':
    scaleColorGumpAction = 13
elif scaleColor == 'black':
    scaleColorGumpAction = 20
elif scaleColor == 'green':
    scaleColorGumpAction = 27
elif scaleColor == 'white':
    scaleColorGumpAction = 34
elif scaleColor == 'blue':
    scaleColorGumpAction = 41
elif scaleColor == 'blue2':
    scaleColorGumpAction = 48

player_bag = Items.FindBySerial(Player.Backpack.Serial)

if fillBags:
    baseBag = Target.PromptTarget('Target bag with bags to fill')

bags = [ 0xe76, 0xe75 , 0xe74 , 0xe78 , 0xe77 , 0x0E79 ]

# Use neraby trashcan
trashBarrelFilter = Items.Filter()
trashBarrelFilter.OnGround = 1
trashBarrelFilter.Movable = False
trashBarrelFilter.RangeMin = 0
trashBarrelFilter.RangeMax = 2
trashBarrelFilter.Graphics = List[int]( [ 0x0E77 ] )
trashBarrelFilter.Hues = List[int]( [ 0x03B2 ] )
trashcanhere = Items.ApplyFilter( trashBarrelFilter )

if not trashcanhere:
    Player.HeadMessage( 1100, 'No trashcan nearby!' )
    sys.exit()
else:
    global trashcan
    trashcan = trashcanhere[ 0 ]
    
def restockScales():
    if Items.BackpackCount(dragonScales,-1) < 50:
        if Player.Mount:
            Mobiles.UseMobile(Player.Serial)
            Misc.WaitForContext(beetle, 1500)
            if Player.Visible:
                Misc.ContextReply(beetle, 10)
            else:
                Misc.ContextReply(beetle, 0)
            Misc.Pause(dragTime)

        beetleScales = Items.FindByID( dragonScales , -1  , beetlePack )
        if beetleScales:
            Items.Move( beetleScales , self_pack , 300 )
            Misc.Pause(dragTime)
        
def craftTools():
    currentTink = Items.FindByID(0x1EB8, -1, -1)
    
    if Items.BackpackCount(0x1BF2, noColor) < 10:
        Misc.SendMessage('Out of Ignots',33)
        winsound.PlaySound(error, winsound.SND_FILENAME)
        sys.exit()
    
    if Items.BackpackCount(0x1EB8, noColor) < 2:
        Items.UseItem(currentTink.Serial)
        Gumps.WaitForGump(949095101, 1500)
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101, 1500)
        Gumps.SendAction(949095101, 23)

    if Items.BackpackCount( smithHammer, noColor) < 1: 
        Items.UseItem(currentTink.Serial)
        Gumps.WaitForGump(949095101,1500)
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101,1500)
        Gumps.SendAction(949095101, 93)
    
def craftDragArmor(bag):
    Items.UseItem(bag)
    Misc.Pause(dragTime)
    for i in dragonSuit:
        while True:
            restockScales()
            craftTools()
            hammer = Items.FindByID(smithHammer,-1,Player.Backpack.Serial)
            if Items.FindByID( i[1] , -1 , bag.Serial ):
                break
            if hammer:
                if Gumps.CurrentGump() != 949095101:
                    Items.UseItem(hammer)
                Gumps.WaitForGump(949095101, gumpTimeout)
                Gumps.SendAction(949095101, 22) #Platemail Menu
                Gumps.WaitForGump(949095101, gumpTimeout)
                Gumps.SendAction(949095101, i[0])
                Gumps.WaitForGump(949095101, gumpTimeout)
                Misc.Pause(gmCheckDelay)
                craftedArmor = Items.FindByID(i[1],-1,Player.Backpack.Serial)
                if craftedArmor:
                    Items.WaitForProps(craftedArmor,500)
                    if Items.GetPropValue(craftedArmor,'Exceptional'):
                        moveToBag(craftedArmor,bag)
                        break
                    else:
                        trashItem(craftedArmor)
        
def trashItem(item):
    Items.Move(item, trashcan, 0)
    Misc.Pause(dragTime)
        
def moveToBag(item,container):
    if Player.Mount:
        Mobiles.UseMobile(Player.Serial)
        Misc.WaitForContext(beetle, 1500)
        if Player.Visible:
            Misc.ContextReply(beetle, 10)
        else:
            Misc.ContextReply(beetle, 0)
        Misc.Pause(dragTime)
    Items.Move(item, container, 0)
    Misc.Pause(dragTime)
        
def setColor():
    Items.UseItemByID(smithHammer,-1)
    Gumps.WaitForGump(949095101, gumpTimeout)
    Gumps.SendAction(949095101, 56)
    Gumps.WaitForGump(949095101, gumpTimeout)
    Gumps.SendAction(949095101, scaleColorGumpAction)
    Misc.Pause(dragTime)
        
Journal.Clear()
setColor()
fillBag = Items.FindBySerial(baseBag)
Items.UseItem(fillBag)
Misc.Pause(dragTime)

for b in fillBag.Contains:
    currentBag = Items.FindBySerial(b.Serial)
    if currentBag.IsContainer:
        craftDragArmor(currentBag)
if not Player.Mount:
    Mobiles.UseMobile(beetle)
            
Misc.SendMessage('All Done Crafting Dragon Armor')
        

        
