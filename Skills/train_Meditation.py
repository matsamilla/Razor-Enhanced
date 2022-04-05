# train meditation to GM by Mastamilla
# purchase magical wizard hat from mage shop

wizardHat = Items.FindByID( 0x1718 , -1 , Player.Backpack.Serial )

if not wizardHat:
    wizardHat = Player.GetItemOnLayer('Head')
    
if wizardHat:
    while Player.GetRealSkillValue("Meditation") < 100:
        if Player.Mana >= Player.ManaMax:
            Items.Move(wizardHat, Player.Backpack.Serial, 0)
            Misc.Pause(2000)
            Player.EquipItem(wizardHat)
            Misc.Pause(600)
            
else:
    Player.HeadMessage(33,'No wizard hat found.')
