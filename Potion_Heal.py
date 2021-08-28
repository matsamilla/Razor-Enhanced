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
    if Player.Hits == Player.HitsMax:
        Player.HeadMessage(msgColor, "At Full Health")
        return
    Journal.Clear()
    if leftHand and noBow:
        Player.UnEquipItemByLayer('LeftHand')
        Misc.Pause(chugtime)
        Player.ChatSay( 1 , '[drink greaterhealpotion')
        Misc.Pause(100)
        if Journal.Search( 'You do not have any of those potions.'):
            Player.HeadMessage(msgColor, "No Heal pots!")
        Misc.Pause(chugtime)
        Player.EquipItem(leftHand)
        Misc.Pause(50)
    else:
        Player.ChatSay( 1 , '[drink greaterhealpotion')
        Misc.Pause(100)
        if Journal.Search( 'You do not have any of those potions.'):
            Player.HeadMessage(msgColor, "No Heal pots!")
        else:
            Misc.NoOperation()
        
def usePot():
    if Player.Hits == Player.HitsMax:
        Player.HeadMessage(msgColor, "At Full Health")
        return
    
    pot = Items.FindByID(0x0F0C,0,Player.Backpack.Serial,True)
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
        Player.HeadMessage(msgColor, "No Heal pots!")
            
        
if Misc.ShardName() == "Ultima Forever":
    potDrink()
else:
    usePot()
         
