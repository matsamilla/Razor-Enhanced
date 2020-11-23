#buff pots
leftHand = Player.GetItemOnLayer('LeftHand')
chugtime = 650
journalTimeout = 100
msgColor = 66
noBow = True
bows = [0x13B2,0x26C2,0x0F50,0x13FD]

if not leftHand:
    noBow = True
elif leftHand.ItemID in bows:
    noBow = False
elif leftHand:
    noBow = True
    
def str():
    Player.ChatSay( 1 , '[drink GreaterStrengthPotion ')
    Misc.Pause( journalTimeout )
    if Journal.Search( 'You do not have any of those potions.'):
        Player.HeadMessage(msgColor, "No Strenth pots!")
        Journal.Clear()
    else:
        Misc.Pause(chugtime)
        
def agil():
    Player.ChatSay( 1 , '[drink GreaterAgilityPotion')
    Misc.Pause( journalTimeout )
    if Journal.Search( 'You do not have any of those potions.'):
        Player.HeadMessage(msgColor, "No Agility pots!")
        Journal.Clear()
    else:
        Misc.Pause(chugtime)
        
def refresh():
    Player.ChatSay( 1 , '[drink totalrefreshpotion')
    Misc.Pause(100)
    if Journal.Search( 'You do not have any of those potions.'):
        Player.HeadMessage(msgColor, "No Refresh pots!")
        Journal.Clear()
    else:
        Misc.Pause(chugtime)
        
def clearHands():
    if leftHand and noBow:
        Player.UnEquipItemByLayer('LeftHand')
        Misc.Pause(650)
        return True
    else:
        return False
       
def reArm():
    Player.EquipItem(leftHand)
    Misc.Pause(50)
    
def buffUp():
    if Player.Str <= 100:
        if clearHands():
            disarmed = True
        else:
            disarmed = False
        str()
        agil()
        refresh()
        if disarmed:
            reArm()
    elif Player.Dex <= 100:
        if clearHands():
            disarmed = True
        else:
            disarmed = False
        str()
        agil()
        refresh()
        if disarmed:
            reArm()
    elif Player.Stam <= Player.StamMax:
        if clearHands():
            disarmed = True
        else:
            disarmed = False
        refresh()
        if disarmed:
            reArm()
    else:
        Player.HeadMessage(msgColor, 'Buffed and full stam')

buffUp()