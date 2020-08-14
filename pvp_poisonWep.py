if Player.GetItemOnLayer("RightHand"):
    item = Player.GetItemOnLayer("RightHand")
elif Player.GetItemOnLayer("LeftHand"):
    item = Player.GetItemOnLayer("LeftHand")
else:
    Misc.SendMessage("No Weapon in Hand",48)

Items.WaitForProps(item,2000)
charges = Items.GetPropValue(item,"Charges")
if charges > 0:
    Player.HeadMessage(78,"{} poison charges".format(int(charges)))
if charges < 1:
    Player.HeadMessage(48,"Repoisoning, {} potions left".format(int(Items.BackpackCount(0x0F0A))))
    pot = Items.FindByID(0x0F0A,-1,Player.Backpack.Serial)
    if pot:
        Player.UseSkill("Poisoning")
        Target.WaitForTarget(2000)
        Target.TargetExecute(pot)
        Target.WaitForTarget(2000)
        Target.TargetExecute(item)
        Player.HeadMessage(48,"{} potions left".format(int(Items.BackpackCount(0x0F0A))))
    else:
        Misc.SendMessage("No Poison Pots",48)
