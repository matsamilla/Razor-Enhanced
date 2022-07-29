# Move big item to trap pouch & announce by MatsaMilla
# version 2.2 - fixed if you get drop after locked

#standard imports
from System.Collections.Generic import List
from System import Byte
import sys

lockBoxAfterDrop = True

# will not box item if serial in this list, like blessed relics
ignoreSerials = [0x402E5274]

# delay for login
Misc.Pause(2500)

msgColor = 66
dragtime = 600
backpack = Items.FindBySerial(Player.Backpack.Serial)
key = 0x100E
box = False

#dragon egg
eggList = [0x2a7c,0x47E6]

#meta relics
relicsList  = [0x2AA4]

#power scrolls
ps = 0x14F0

#skulls
skullList = [0x1AE1]

#crystals
crystalsList = [
0x35DA, #event crystal
0x0F21, #portal frag
]

perks = [ 0x2dd5,0x1f18,0x2da3,0x166e,0x26BB,0x139B,0x0FBE ]

# only boxes tame SSs, blaze color
ss = [ 0x2260 ]

#box types
trapBox = [0x9aa,0x9a9,0xe3e,0xe3c,0xe42,0xe43,0x280b,0xe7d,0xe7e,0xe3f,0xe3d,0x280c]


for b in backpack.Contains:
    if b.ItemID in trapBox:
        box = b
        Player.HeadMessage(msgColor, 'Trap Box Set to ' + box.Name)
        break
        
moveList = []

def dropWatch():
    for i in backpack.Contains:
        if i.ItemID in eggList:
            moveList.append(i.Serial)
        elif i.ItemID in relicsList:
            moveList.append(i.Serial)
        elif (i.ItemID == ps and i.Hue == 0x0481):
            moveList.append(i.Serial)
        elif i.ItemID in skullList and i.Hue == 0x0000:
            moveList.append(i.Serial)
        elif i.ItemID in crystalsList: 
            if i.Hue == 0x0489 or i.ItemID == 0x35DA:
                moveList.append(i.Serial)
        elif i.ItemID in perks:
            moveList.append(i.Serial)
        elif i.Hue == 0x0489 and i.ItemID in ss:
            moveList.append(i.Serial)
            
    for m in moveList:
        if m in ignoreSerials:
            moveList.remove(m)
            
    if len(moveList) > 0:
        boxItems()
        if lockBoxAfterDrop:
            lockBox()
        
def boxItems():
    Journal.Clear()
    for i in moveList:
        Items.Move(i, box, 0)
        Misc.Pause(dragtime)
        hotItem = Items.FindBySerial(i)
        Items.WaitForProps(hotItem, 500)
        itemName = Items.GetPropStringByIndex(hotItem, 0)
        if itemName:
            Player.HeadMessage(msgColor, itemName)
            hotItem = Items.FindBySerial(i)
            Misc.Pause(50)
            if hotItem.Container != box.Serial:
                Player.HeadMessage(33,'NOT IN BOX')
                if Journal.Search('It appears to be locked.'):
                    unlockBox()
            else:
                Player.ChatParty(itemName + ' In Box')
    del moveList[:]
        
def lockBox():
    Journal.Clear()
    boxKey = Items.FindByID(key,-1,Player.Backpack.Serial,True)
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
        
def unlockBox():
    Journal.Clear()
    boxKey = Items.FindByID(key,-1,Player.Backpack.Serial,True)
    if boxKey:
        Items.UseItem(boxKey)
        Target.WaitForTarget(1500)
        Target.TargetExecute(box)
        Misc.Pause(dragtime)
        if Journal.Search('You unlock it.'):
            Player.HeadMessage(msgColor, 'Box unLocked!!')
            Player.ChatParty('Box unLocked!!')
    else:
        Player.HeadMessage(msgColor, 'No Key!\n!!Still UnLOCKED!!')
    
    boxItems()
    

Journal.Clear()
while True:
    if not box:
        Misc.Pause(500)
        Misc.SendMessage('No trap box, stopping script', 33)
        sys.exit()
    Misc.Pause(50)
    dropWatch()   
