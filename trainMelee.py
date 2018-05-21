import sys

skill = 'Lumberjacking'

def trainMelee(skill):
    while True:
        if Player.GetSkillValue(skill) > 99.9:
            Player.SetWarMode(False)
            sys.exit()
            
trainMelee(skill)