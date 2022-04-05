#buff pots
leftHand = Player.GetItemOnLayer('LeftHand')
chugtime = 650
journalTimeout = 100
msgColor = 66
noBow = True
bows = [0x13B2,0x26C2,0x0F50,0x13FD,0x0A12,0x0F6B] # 0x0A12,0x0F6B = torch

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
        Player.HeadMessage(msgColor, "No Strength pots!")
        Journal.Clear()
    else:
        Misc.Pause(chugtime)
        
def strPot():
    whitePot = Items.FindByID(0x0F09,0,Player.Backpack.Serial,True)
    if whitePot:
        Items.UseItem(whitePot)
        Misc.Pause(chugtime)
    else:
        Player.HeadMessage(msgColor, "No Strength pots!")
        
def agil():
    Player.ChatSay( 1 , '[drink GreaterAgilityPotion')
    Misc.Pause( journalTimeout )
    if Journal.Search( 'You do not have any of those potions.'):
        Player.HeadMessage(msgColor, "No Agility pots!")
        Journal.Clear()
    else:
        Misc.Pause(chugtime)
        
def agilPot():
    bluePot = Items.FindByID(0x0F08,0,Player.Backpack.Serial,True)
    if bluePot:
        Items.UseItem(bluePot)
        Misc.Pause(chugtime)
    else:
        Player.HeadMessage(msgColor, "No Agility pots!")

        
def refresh():
    Player.ChatSay( 1 , '[drink totalrefreshpotion')
    Misc.Pause(100)
    if Journal.Search( 'You do not have any of those potions.'):
        Player.HeadMessage(msgColor, "No Refresh pots!")
        Journal.Clear()
#    else:
#        Misc.Pause(chugtime)

def refreshPot():
    redPot = Items.FindByID(0x0F0B,0,Player.Backpack.Serial,True)
    if redPot:
        Items.UseItem(redPot)
    else:
        Player.HeadMessage(msgColor, "No Refresh pots!")
        
def clearHands():
    if leftHand and noBow:
        Player.UnEquipItemByLayer('LeftHand')
        Misc.Pause(chugtime)
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
        
def buffUpPots():
    if Player.Str <= 100:
        if clearHands():
            disarmed = True
        else:
            disarmed = False
        strPot()
        agilPot()
        refreshPot()
        if disarmed:
            reArm()
    elif Player.Dex <= 100:
        if clearHands():
            disarmed = True
        else:
            disarmed = False
        strPot()
        agilPot()
        refreshPot()
        if disarmed:
            reArm()
    elif Player.Stam <= Player.StamMax:
        if clearHands():
            disarmed = True
        else:
            disarmed = False
        refreshPot()
        if disarmed:
            reArm()
    else:
        Player.HeadMessage(msgColor, 'Buffed and full stam')


if Misc.ShardName() == "Ultima Forever" or Misc.ShardName() == "UOForever":
    buffUp()
else:
    buffUpPots()
