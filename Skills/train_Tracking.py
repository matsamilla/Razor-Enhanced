while Player.GetRealSkillValue('Tracking') < 100:
    Player.UseSkill("Tracking")
    Gumps.WaitForGump(2976808305, 10000)
    Gumps.SendAction(2976808305, 4)
    Misc.Pause(500)
    Gumps.CloseGump(993494147)
    Misc.Pause(10500)
