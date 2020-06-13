poisPot = Items.FindByID(0x0F0A,-1,Player.Backpack.Serial)
if poisPot:
    Player.UseSkill("Poisoning")
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(poisPot.Serial)
    righthand = Player.GetItemOnLayer('RightHand')
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(righthand.Serial)