targetMobile = 0x0002CF77

def trainEvalInt():
    while Player.GetSkillValue('EvalInt') < 100:
        Player.UseSkill('EvalInt')
        Target.WaitForTarget(7000,True)
        Target.TargetExecute(targetMobile)
        Misc.Pause(1000)
    
trainEvalInt()