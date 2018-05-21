targetMobile = 0x0002CF77

def trainAnatomy():
    while Player.GetSkillValue('Anatomy') < 100:
        Player.UseSkill('Anatomy')
        Target.WaitForTarget(7000,True)
        Target.TargetExecute(targetMobile)
        Misc.Pause(4000)
    
trainAnatomy()