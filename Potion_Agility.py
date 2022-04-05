leftHand = Player.GetItemOnLayer('LeftHand')
chugtime = 650
msgColor = 66
noBow = True
bows = [ 0x13B2,0x26C2,0x0F50,0x13FD,0x0A12,0x0F6B] # 0x0A12,0x0F6B = torch

if not leftHand:
    noBow = True
elif leftHand.ItemID in bows:
    noBow = False
elif leftHand:
    noBow = True
    
def potDrink():
    Journal.Clear()
    if leftHand and noBow:
        Player.UnEquipItemByLayer('LeftHand')
        Misc.Pause(chugtime)
        Player.ChatSay( 1 , '[drink greaterAgilityPotion')
        Misc.Pause(100)
        if Journal.Search( 'You do not have any of those potions.'):
            Player.HeadMessage(msgColor, "No Agility pots!")
        Misc.Pause(chugtime)
        Player.EquipItem(leftHand)
        Misc.Pause(50)
    else:
        Player.ChatSay( 1 , '[drink greaterAgilityPotion')
        Misc.Pause(100)
        if Journal.Search( 'You do not have any of those potions.'):
            Player.HeadMessage(msgColor, "No Agility pots!")
        else:
            Misc.NoOperation()
        
def usePot():    
    pot = Items.FindByID(0x0F08,0,Player.Backpack.Serial,True)
    if pot:
        if leftHand and noBow:
            Player.UnEquipItemByLayer('LeftHand')
            Misc.Pause(chugtime)
            Items.UseItem(pot)
            Misc.Pause(chugtime)
            Player.EquipItem(leftHand)
            Misc.Pause(50)
        else:
            Items.UseItem(pot)
    else:
        Player.HeadMessage(msgColor, "No Agility pots!")
            
        
if Misc.ShardName() == "Ultima Forever" or Misc.ShardName() == "UOForever":
    potDrink()
else:
    usePot()
         
