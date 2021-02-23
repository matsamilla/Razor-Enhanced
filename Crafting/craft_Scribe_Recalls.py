restockBeetle = False

amountToMake = 10000
restockChestSerial = 0x43510513
dragTime = 600
bp = 0x0F7A
bm = 0x0F7B
mr = 0x0F86
pen = 0x0FBF
scroll = 0x0EF3
recall = 0x1F4C
noColor = 0x0000
pack = Player.Backpack.Serial

beetle = 0x0023F0A0
beetleContainer = 0x439F1BD4 # Inspect item in beetle to get container


restockChest = Items.FindBySerial(restockChestSerial)

def craftRecall():
    #pens = Items.FindByID(0x0FBF,-1,pack)
    pens = FindItem(0x0FBF, Player.Backpack)
    Items.UseItem(pens)
    Gumps.WaitForGump(949095101, 2000)
    Gumps.SendAction(949095101, 22)
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
    recalls = Items.FindByID(recall, -1, pack)
    if recalls:
        if restockBeetle:
            if Player.Mount:
                Mobiles.UseMobile(self)
                Misc.Pause(dragTime)
                Items.Move(recalls, beetle, 0)
                Misc.Pause(dragTime)
            if not Player.Mount:
                Mobiles.UseMobile(beetle)
                Misc.Pause(dragTime)
                
        else:
            Items.Move(recalls, restockChest.Serial, 0)
            Misc.Pause(dragTime)
        
def FindItem( itemID, container, color = -1, ignoreContainer = [] ):
    '''
    Searches through the container for the item IDs specified and returns the first one found
    Also searches through any subcontainers, which Misc.FindByID() does not
    '''
    ignoreColor = False
    if color == -1:
        ignoreColor = True

    if isinstance( itemID, int ):
        foundItem = next( ( item for item in container.Contains if ( item.ItemID == itemID and ( ignoreColor or item.Hue == color ) ) ), None )
    elif isinstance( itemID, list ):
        foundItem = next( ( item for item in container.Contains if ( item.ItemID in itemID and ( ignoreColor or item.Hue == color ) ) ), None )
    else:
        raise ValueError( 'Unknown argument type for itemID passed to FindItem().', itemID, container )

    if foundItem != None:
        return foundItem

    subcontainers = [ item for item in container.Contains if ( item.IsContainer and not item.Serial in ignoreContainer ) ]
    for subcontainer in subcontainers:
        foundItem = FindItem( itemID, subcontainer, color, ignoreContainer )
        if foundItem != None:
            return foundItem    
        

def restock():
    recalls = Items.FindByID(recall, -1, pack)
    
    if restockBeetle:
        if Items.BackpackCount(scroll, -1) < 1 or Items.BackpackCount(bp, -1) < 1 or Items.BackpackCount(bm, -1) < 1 or Items.BackpackCount(mr, -1) < 1:
            if Player.Mount:
                Mobiles.UseMobile(Player.Serial)
                Misc.Pause(dragTime)
            backpackscrolls = Items.FindByID(scroll, noColor, pack)
            backpackBp = Items.FindByID(bp, noColor, pack)
            backpackBm = Items.FindByID(bm, noColor, pack)
            backpackMr = Items.FindByID(mr, noColor, pack)
            
            
            if backpackscrolls:
                Items.Move(backpackscrolls, beetle, beetleContainer)
                Misc.Pause(dragTime)
            if backpackBp:
                Items.Move(backpackBp, beetle, 0)
                Misc.Pause(dragTime)
            if backpackBm:
                Items.Move(backpackBm, beetle, 0)
                Misc.Pause(dragTime)
            if backpackMr:
                Items.Move(backpackMr, beetle, 0)
                Misc.Pause(dragTime)
            if recalls:
                Items.Move(recalls, beetle, 0)
                Misc.Pause(dragTime)
            
            Mobiles.SingleClick(beetle)
            Misc.WaitForContext(beetle, 1500)
            Misc.ContextReply(beetle, "Open Backpack")
            Misc.Pause(dragTime)
            
            beetleScrolls = Items.FindByID(scroll, noColor, beetleContainer)
            bps = Items.FindByID (bp , noColor, beetleContainer)
            bms = Items.FindByID (bm , noColor, beetleContainer)
            mrs = Items.FindByID (mr , noColor, beetleContainer)
            
            if beetleScrolls:
                Items.Move(beetleScrolls, pack, 100)
                Misc.Pause(dragTime)
            if bps:
                Items.Move(bps, pack, 100)
                Misc.Pause(dragTime)
            if bms:
                Items.Move(bms, pack, 100)
                Misc.Pause(dragTime)
            if mrs:
                Items.Move(mrs, pack, 100)
                Misc.Pause(dragTime)
                
        if not Player.Mount:
            Mobiles.UseMobile(beetle)
            Misc.Pause(dragTime)
    else:
        if Items.BackpackCount(scroll, -1) < 1:
            Items.UseItem(restockChest)
            Misc.Pause(dragTime)
            scrolls = Items.FindByID (scroll ,-1,restockChest.Serial)
            Items.Move(scrolls, pack, 100)
            Misc.Pause(dragTime)
            unload()
            
        if Items.BackpackCount(bp, -1) < 1:
            Items.UseItem(restockChest)
            Misc.Pause(dragTime)
            bps = Items.FindByID (bp ,-1,restockChest.Serial)
            Items.Move(bps, pack, 100)
            Misc.Pause(dragTime)
            unload()
        
        if Items.BackpackCount(bm, -1) < 1:
            Items.UseItem(restockChest)
            Misc.Pause(dragTime)
            bms = Items.FindByID (bm ,-1,restockChest.Serial)
            Items.Move(bms, pack, 100)
            Misc.Pause(dragTime)
            unload()
            
        if Items.BackpackCount(mr, -1) < 1:
            Items.UseItem(restockChest)
            Misc.Pause(dragTime)
            mrs = Items.FindByID (mr ,-1,restockChest.Serial)
            Items.Move(mrs, pack, 100)
            Misc.Pause(dragTime)
            unload()
    if Items.BackpackCount(pen, -1) < 1:
        restockPen = FindItem(pen, restockChest)
        Items.Move(restockPen, pack, 0)
        Misc.Pause(dragTime)
    
    if Items.BackpackCount(scroll, -1) < 1 or Items.BackpackCount(bp, -1) < 1 or Items.BackpackCount(bm, -1) < 1 or Items.BackpackCount(mr, -1) < 1:
        Stop
    if Items.BackpackCount(pen, -1) < 1:
        Misc.SendMessage('Out of pens', 33)
        Stop
for i in range(0,amountToMake):
    restock()    
    craftRecall()
    if i % 10 == 0:
        Misc.SendMessage ( 'Recalls made: %i' % ( i ) , 33)
        #Misc.SendMessage(i)
