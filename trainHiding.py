
def trainHiding():
    while Player.GetSkillValue('Hiding') < 100:
        Player.UseSkill('Hiding')
        Misc.Pause(600)
        Player.Run('West')
        Player.Run('West')
        Player.Run('West')
        Player.Run('West')
        Player.Run('West')
        Misc.Pause(10500)
        Player.UseSkill('Hiding')
        Misc.Pause(600)
        Player.Run('East')
        Player.Run('East')
        Player.Run('East')
        Player.Run('East')
        Player.Run('East')
        Misc.Pause(10500)
        
trainHiding()