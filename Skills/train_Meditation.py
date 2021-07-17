# train meditation to GM by Mastamilla
# purchase magical wizard hat from mage shop 
# start with wizard hat in backpack

wizardHat = Items.FindByID( 0x1718 , -1 , Player.Backpack.Serial )

while Player.GetRealSkillValue("Meditation") < 100:
    if Player.Mana == Player.ManaMax:
        Items.Move(wizardHat, Player.Backpack.Serial, 0)
        Misc.Pause(600)
        Player.EquipItem(wizardHat)
        Misc.Pause(600)
