# Drag-Drop organizer by Mourn
# contributions by MatsaMilla
# adjust to your servers drag delay in ms
dragDelay = 600

startX = 0
startY = 0
verticalIncrement = 0
horizontalIncrement = 5
endX = 0
endY = 0
item = Items.FindBySerial( Target.PromptTarget( 'Choose type' ))
container = Items.FindBySerial( item.Container )
itemID = item.ItemID
itemHue = item.Hue
destPrompt = Target.PromptTarget( 'Chose Destination' )
itemsToMove = []
# gems
gems = [0x0F19, 0x0F25, 0x0F13, 0x0F16, 0x0F21, 0x0F26, 0x0F15, 0x0F2D, 0x0F10]
#glowing runes
glowingRunes = [0x483b, 0x483e, 0x4841, 0x4844, 0x4847, 0x484a, 0x484d,
 0x4850, 0x4853, 0x4856, 0x4859, 0x485c, 0x485f, 0x4862, 0x4865, 0x4868, 
 0x486b, 0x486e, 0x4871, 0x4874, 0x4877, 0x487a, 0x487d, 0x4880, 0x4883]
#Regs
regs = [0x0F86, 0x0F88, 0x0F8D, 0x0F85,0x0F7B, 0x0F84, 0x0F8C, 0x0F7A]

#Misc.SendMessage(str(dest))

def getSize(container):
    global startX
    global startY
    global endX
    global endY
    global verticalIncrement
    global horizontalIncrement
    
    if "backpack" in container.Name:
        Misc.SendMessage("Setting size to Backpack or a Pouch")
        startX = 45
        startY = 75
        endX = 160
        endY = 150
        verticalIncrement = 20
    elif "pouch" in container.Name:
        Misc.SendMessage("Setting size to Pouch")
        startX = 45
        startY = 75
        endX = 160
        endY = 150
        verticalIncrement = 20
    elif "bag" in container.Name:
        Misc.SendMessage("Setting size to Bag")
        startX = 30
        startY = 40
        endX = 115
        endY = 120
        verticalIncrement = 20
    elif "ornate" in container.Name:
        Misc.SendMessage("Setting size to Box")
        startX = 15
        startY = 50
        endX = 155
        endY = 120
        verticalIncrement = 20
    elif "wooden box" in container.Name:
        Misc.SendMessage("Setting size to Box")
        startX = 15
        startY = 50
        endX = 155
        endY = 120
        verticalIncrement = 20
    elif "metal chest" in container.Name:
        Misc.SendMessage("Setting size to Metal Chest")
        startX = 20
        startY = 105
        endX = 135
        endY = 150
        verticalIncrement = 10
    else:
        Misc.SendMessage("Setting size to Unknown")
        startX = 50
        startY = 50
        endX = 115
        endY = 120
        verticalIncrement = 20
        
if destPrompt == Player.Serial:
    dest = Player.Backpack.Serial
    Misc.SendMessage("Setting size to Backpack")
    startX = 45
    startY = 75
    endX = 160
    endY = 150
    verticalIncrement = 20
else:
    dest = Items.FindBySerial( destPrompt )
    getSize(dest)
        
if item.ItemID in gems:
    for items in container.Contains:
        if items.ItemID in gems:
            Items.Move(items,dest,0)
            Misc.Pause(600)
    Stop
elif item.ItemID in glowingRunes:
    for items in container.Contains:
        if items.ItemID in glowingRunes:
            Items.Move(items,dest,0)
            Misc.Pause(600)
    Stop
elif item.ItemID in regs:
    for items in container.Contains:
        if items.ItemID in regs:
            Items.Move(items,dest,0)
            Misc.Pause(600)
    Stop
else:
    for items in container.Contains:
        if items.ItemID == itemID and items.Hue == itemHue :
            itemsToMove.append( items.Serial )


x = startX
y = startY
total = len( itemsToMove )
timeToMove = ( total * dragDelay ) / 1000

Player.HeadMessage( 66, "Moving " + str( total ) + ' Items' )
Misc.Pause( 200 )
Player.HeadMessage( 66, str( timeToMove ) + ' Seconds' )
Journal.Clear()
        
for items in itemsToMove:
    if x > endX:
        x = startX
        y = y + verticalIncrement
    if y >= endY:
        y = startY + verticalIncrement
    Items.Move( items , dest , 0 , x , y )
    Misc.Pause( dragDelay )
    x = x + horizontalIncrement
    if Journal.Search('That container cannot hold more items.'):
        Player.HeadMessage( 66, "Container full, stopping" )
        Journal.Clear()
        Stop
    
Player.HeadMessage( 76 ,'Items have been moved' )