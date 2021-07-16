# Toggle alternate wep by MatsaMilla
# updated 7/16/21

leftHand = Player.GetItemOnLayer('LeftHand')
rightHand = Player.GetItemOnLayer('RightHand')
shields = [ 0x1B76,0x1B74,0x1B7B,0x1B73,0x1B72,0x1B79,0x1B7A ]

import sys

if Misc.CheckSharedValue(Player.Name + 'wep'):
    tempwep = Items.FindBySerial(Misc.ReadSharedValue(Player.Name + 'wep'))
    if tempwep:
        wep = tempwep
    else:
        Player.HeadMessage(66,'Target New Wep')
        wep = Items.FindBySerial( Target.PromptTarget() )
        if wep:
            Misc.SetSharedValue(Player.Name + 'wep', wep.Serial)
            Player.HeadMessage(66, 'Wep Set')
        else:
            Player.HeadMessage(33, 'Wep Not Set')
            sys.exit()
else:
    Player.HeadMessage(66,'Target Wep')
    wep = Items.FindBySerial( Target.PromptTarget() )
    if wep:
        Misc.SetSharedValue(Player.Name + 'wep', wep.Serial)
        Player.HeadMessage(66, 'Wep Set')
    else:
        Player.HeadMessage(33, 'Wep Not Set')
        sys.exit()
    
def toggleWep():
    if wep.IsTwoHanded:
        Misc.SendMessage('Two Handed')
        if rightHand:
            Items.Move(rightHand.Serial,Player.Backpack.Serial,0)
            Misc.Pause(600)
        if leftHand:
            if leftHand.Serial == wep.Serial:
                Items.Move(wep,Player.Backpack.Serial,0)
                Misc.Pause(600)
            else:
                Items.Move(leftHand.Serial,Player.Backpack.Serial,0)
                Misc.Pause(600)
                Player.EquipItem(wep)
        else:
            Player.EquipItem(wep)
            
    elif wep.ItemID in shields:
        Misc.SendMessage('Shield')
        if leftHand:
            if leftHand.Serial == wep.Serial:
                Items.Move(wep,Player.Backpack.Serial,0)
            else:
                Items.Move(leftHand.Serial,Player.Backpack.Serial,0)
                Misc.Pause(600)
                Player.EquipItem(wep)
        else:
            Player.EquipItem(wep) 
        
        
    else:
        if rightHand:
            if rightHand.Serial == wep.Serial:
                Items.Move(wep,Player.Backpack.Serial,0)
            else:
                Items.Move(rightHand,Player.Backpack.Serial,0)
                Misc.Pause(600)
                Player.EquipItem(wep)
                
        if leftHand:
            if leftHand.Serial == wep.Serial:
                Items.Move(wep,Player.Backpack.Serial,0)
            elif leftHand.ItemID in shields:
                Player.EquipItem(wep)
            else:                
                Items.Move(leftHand,Player.Backpack.Serial,0)
                Misc.Pause(600)
                Player.EquipItem(wep)
        
        else:
            Player.EquipItem(wep)
        
toggleWep()
