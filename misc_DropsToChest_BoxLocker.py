# Move big item to trap pouch & announce by MatsaMilla
# version 2.2 - 8/30/21

############ setup ########################

lockBoxAfterDrop = False

# list of items to toss in box
itemsToBox = [
    0x2a7c, #egg
    0x47E6, #egg
    0x2AA4, #relic
    0x14F0, #ps
    0x1AE1, #skull
    0x35DA, #event frag
    0x0F21, #portal frag
    0x2dd5, #perk
    0x1f18, #perk
    0x2da3, #perk
    0x166e, #perk
    0x26BB, #perk
    0x139B, #perk
    0x0FBE, #perk
    0x2260, #skill scroll
    0x422B, #crab bite
    0x0C65, #dragon fruit
    
]

# add specific items to not box here (like blessed relics)
ignoreSerials = [0x402E5274]

#########################################################

#standard imports
from System.Collections.Generic import List
from System import Byte
import sys

# delay for login
Misc.Pause(2500)

msgColor = 66
dragtime = 600
backpack = Items.FindBySerial(Player.Backpack.Serial)
key = 0x100E
box = False

#box types
trapBox = [0x9aa,0x9a9,0xe3e,0xe3c,0xe42,0xe43,0x280b,0xe7d,0xe7e,0xe3f,0xe3d,0x280c]

for b in backpack.Contains:
    if b.ItemID in trapBox:
        box = b
        Player.HeadMessage(msgColor, 'Trap Box Set to ' + box.Name)
        break
        
moveList = []

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

def dropWatch():
    for i in backpack.Contains:
        if i.ItemID in itemsToBox:
            moveList.append(i.Serial)        
            
    for m in moveList:
        if m in ignoreSerials:
            moveList.remove(m)
            
    if len(moveList) > 0:
        boxItems()
        if lockBoxAfterDrop:
            lockBox()
        
def boxItems():
    for i in moveList:
        Items.Move(i, box, 0)
        Misc.Pause(dragtime)
        hotItem = Items.FindBySerial(i)
        Items.WaitForProps(hotItem, 500)
        itemName = Items.GetPropStringByIndex(hotItem, 0)
        if itemName:
            Player.HeadMessage(msgColor, itemName)
            hotItem = Items.FindBySerial(i)
            if hotItem.Container != box.Serial:
                Player.HeadMessage(33,'NOT IN BOX')
            Player.ChatParty(itemName + ' In Box')
    del moveList[:]
        
def lockBox():
    Journal.Clear()
    boxKey = FindItem(key,Player.Backpack)
    if boxKey:
        Items.UseItem(boxKey)
        Target.WaitForTarget(1500)
        Target.TargetExecute(box)
        Misc.Pause(200)
        if Journal.Search('You lock it.'):
            Player.HeadMessage(msgColor, 'Box Locked!!')
            Player.ChatParty('Box Locked!!')
        else:
            lockBox()
    else:
        Player.HeadMessage(msgColor, 'No Key!\n!!NOT LOCKED!!')

Journal.Clear()
while True:
    if not box:
        Misc.Pause(500)
        Misc.SendMessage('No trap box, stopping script', 33)
        Misc.ScriptStop('misc_Drops To Chest.py')
    Misc.Pause(50)
    dropWatch()   