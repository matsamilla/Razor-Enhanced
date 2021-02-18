# Weapon Swapper by Matsamilla
# Swaps between 2 weps

leftHand = Player.GetItemOnLayer('LeftHand')
rightHand = Player.GetItemOnLayer('RightHand')

if Misc.CheckSharedValue(Player.Name + 'swep'):
    tempwep = Items.FindBySerial(Misc.ReadSharedValue(Player.Name + 'swep'))
    if tempwep:
        wep = tempwep.Serial
    else:
        Player.HeadMessage(66,'Target New Wep')
        wep = Target.PromptTarget()
        Misc.SetSharedValue(Player.Name + 'swep', wep)
        Player.HeadMessage(66, 'Wep Set')
else:
    Player.HeadMessage(66,'Target Wep')
    wep = Target.PromptTarget()
    Misc.SetSharedValue(Player.Name + 'swep', wep)
    Player.HeadMessage(66, 'Wep Set')
    
if Misc.CheckSharedValue(Player.Name + 'swep2'):
    tempwep2 = Items.FindBySerial(Misc.ReadSharedValue(Player.Name + 'swep2'))
    if tempwep2:
        wep2 = tempwep2.Serial
    else:
        Player.HeadMessage(66,'Target Wep 2')
        wep2 = Target.PromptTarget()
        Misc.SetSharedValue(Player.Name + 'swep2', wep2)
        Player.HeadMessage(66, 'Wep 2 Set')
else:
    Player.HeadMessage(66,'Target Wep')
    wep2 = Target.PromptTarget()
    Misc.SetSharedValue(Player.Name + 'swep2', wep2)
    Player.HeadMessage(66, 'Wep 2 Set')
    
if Misc.CheckSharedValue(Player.Name + 'weplist'):
    weplist = Misc.ReadSharedValue(Player.Name + 'weplist')
else:
    weplist = [wep,wep2]
    Misc.SetSharedValue(Player.Name + 'weplist', weplist)
for i in weplist:    
    Misc.SendMessage(i)
    

if rightHand:
    Items.Move(rightHand,Player.Backpack.Serial,0)
    Misc.Pause(600)
        
if leftHand:
    Items.Move(leftHand,Player.Backpack.Serial,0)
    Misc.Pause(600)

Player.EquipItem(weplist[0])
weplist.reverse()
weplist.pop()
if not weplist:
    Misc.RemoveSharedValue(Player.Name + 'weplist')
else:
    weplist = Misc.ReadSharedValue(Player.Name + 'weplist')
