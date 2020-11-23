leftHand = Player.GetItemOnLayer('LeftHand')
chugtime = 800
msgColor = 66
noBow = True
bows = [ 0x13B2,0x26C2,0x0F50,0x13FD ]

if not leftHand:
    noBow = True
elif leftHand.ItemID in bows:
    noBow = False
elif leftHand:
    noBow = True

Journal.Clear()
if Player.Poisoned:
    if leftHand and noBow:
        Player.UnEquipItemByLayer('LeftHand')
        Misc.Pause(650)
        Player.ChatSay( 1 , '[drink greatercurepotion')
        Misc.Pause(100)
        if Journal.Search( 'You do not have any of those potions.'):
            Player.HeadMessage(msgColor, "No Cure pots!")
        Misc.Pause(chugtime)
        Player.EquipItem(leftHand)
        Misc.Pause(50)
    else:
        Player.ChatSay( 1 , '[drink greatercurepotion')
        Misc.Pause(100)
        if Journal.Search( 'You do not have any of those potions.'):
            Player.HeadMessage(msgColor, "No Cure pots!")
        else:
            Misc.NoOperation()
else:
    Player.HeadMessage(msgColor, "Not Poisoned")