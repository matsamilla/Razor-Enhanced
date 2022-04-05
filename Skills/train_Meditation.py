# train meditation to GM by Mastamilla
# purchase magical wizard hat from mage shop


#check backpack for wizard hat
wizardHat = Items.FindByID( 0x1718 , -1 , Player.Backpack.Serial )

# not in pack? Check head layer
if not wizardHat:
    wizardHat = Player.GetItemOnLayer('Head')
    
# hat found
if wizardHat:
    #loop until GM
    while Player.GetRealSkillValue("Meditation") < 100:
        if Player.Mana >= Player.ManaMax:
            Items.Move(wizardHat, Player.Backpack.Serial, 0)
            Misc.Pause(2000)
            Player.EquipItem(wizardHat)
            Misc.Pause(600)

# no hat found            
else:
    Player.HeadMessage(33,'No wizard hat found.')
