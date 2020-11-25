leftHand = Player.GetItemOnLayer('LeftHand')
chugtime = 800
msgColor = 66
noBow = True
bows = [0x13B2,0x26C2,0x0F50,0x13FD]
basestr = 101

if not leftHand:
    noBow = True
elif leftHand.ItemID in bows:
    noBow = False
elif leftHand:
    noBow = True

Journal.Clear()
if Player.Str < basestr:
    Player.HeadMessage(msgColor, "Buffing Str")
    
    if leftHand and noBow:
        Player.UnEquipItemByLayer('LeftHand')
        Misc.Pause(650)
        Player.ChatSay( 1 , '[drink greaterStrengthPotion')
        Misc.Pause(100)
        if Journal.Search( 'You do not have any of those potions.'):
            Player.HeadMessage(msgColor, "No Strength pots!")
        Misc.Pause(chugtime)
        Player.EquipItem(leftHand)
        Misc.Pause(50)
    else:
        Player.ChatSay( 1 , '[drink greaterStrengthPotion')
        Misc.Pause(100)
        if Journal.Search( 'You do not have any of those potions.'):
            Player.HeadMessage(msgColor, "No Strength pots!")
        else:
            Misc.NoOperation()
else:
    Player.HeadMessage(msgColor, "Full Strength Buff")