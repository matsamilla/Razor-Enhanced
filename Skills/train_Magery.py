# Trains Magery to GM
# Change resistTrain to True if you are training resist and/or
#   don't want to take damage
# False will make it cast dmg spells on yourself, which use less regs.
#    but require someone healing you, or you to have healing.
# By MatsaMilla

resistTrain = True
# ------------------------------------
self = Player.Serial
pearl = 0x0F7A
root = 0x0F86
shade = 0x0F88
silk = 0x0F8D
moss = 0x0F7B
ginseng = 0x0F85
garlic = 0x0F84
ash = 0x0F8C

def trainMageryNoResist():
    while Player.Hits < 45:
        Misc.Pause(100)
    
    if Player.GetRealSkillValue('Magery') < 35:
        Misc.SendMessage('Go buy Magery skill!!')
        Stop
    elif Player.GetRealSkillValue('Magery') < 65:
        Spells.CastMagery('Mind Blast')
        Target.WaitForTarget(2500)
        Target.TargetExecute(self)
        Misc.Pause(2500)
    elif Player.GetRealSkillValue('Magery') < 85:
        Spells.CastMagery('Energy Bolt')
        Target.WaitForTarget(2500)
        Target.TargetExecute(self)
        Misc.Pause(2500)
    elif Player.GetRealSkillValue('Magery') < 100:
        Spells.CastMagery("Flamestrike")
        Target.WaitForTarget(2500)
        Target.TargetExecute(self)
        Misc.Pause(2500)
    
    if Player.Mana < 40:
        Player.UseSkill('Meditation')
        while Player.Mana < Player.ManaMax:
            if (not Player.BuffsExist('Meditation') and not Timer.Check('skillTimer')):
                Player.UseSkill('Meditation')
                Timer.Create('skilltimer', 11000)
            Misc.Pause(100)
    

def trainMage():
    if Player.GetRealSkillValue('Magery') < 35:
        Misc.SendMessage('Go buy Magery skill!!')
        Stop
    elif Player.GetRealSkillValue('Magery') < 55:
        Spells.CastMagery('Mana Drain')
        Target.WaitForTarget(2500)
        Target.TargetExecute(self)
        Misc.Pause(2500)
    elif Player.GetRealSkillValue('Magery') < 75:
        Spells.CastMagery('Invisibility')
        Target.WaitForTarget(2500)
        Target.TargetExecute(self)
        Misc.Pause(2500)
    elif Player.GetRealSkillValue('Magery') < 100:
        Spells.CastMagery('Mana Vampire')
        Target.WaitForTarget(2500)
        Target.TargetExecute(self)
        Misc.Pause(2500)
    if Player.Mana < 40:
        Player.UseSkill('Meditation')
        while Player.Mana < Player.ManaMax:
            if (not Player.BuffsExist('Meditation') and not Timer.Check('skillTimer')):
                Player.UseSkill('Meditation')
                Timer.Create('skilltimer', 11000)
            Misc.Pause(100)
            
def checkRegs():
    if Items.BackpackCount(pearl, -1) < 2:
        Misc.SendMessage('Low on Pearl!')
        Stop
    elif Items.BackpackCount(root, -1) < 2:
        Misc.SendMessage('Low on Root!')
        Stop
    elif Items.BackpackCount(shade, -1) < 2:
        Misc.SendMessage('Low on Shade!')
        Stop
    elif Items.BackpackCount(silk, -1) < 2:
        Misc.SendMessage('Low on Silk!')
        Stop
    elif Items.BackpackCount(garlic, -1) < 2:
        Misc.SendMessage('Low on Garlic!')
        Stop
    elif Items.BackpackCount(ash, -1) < 2:
        Misc.SendMessage('Low on Ash!')
        Stop
    elif Items.BackpackCount(silk, -1) < 2:
        Misc.SendMessage('Low on Silk!')
        Stop
    elif Items.BackpackCount(ginseng, -1) < 2:
        Misc.SendMessage('Low on Ginseng!')
        Stop

Journal.Clear()
while Player.GetRealSkillValue('Magery')  < 100:
    if resistTrain:
        trainMage()
    else:       
        trainMageryNoResist()
    checkRegs()
    
Player.ChatSay(33, 'GM Magery')
