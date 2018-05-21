itemToID = 0x41470B9F

while True:
    Player.UseSkill('Item ID')
    Target.WaitForTarget(2000,True)
    Target.TargetExecute(itemToID)
    Misc.Pause(1000)