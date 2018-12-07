Target.ClearLastandQueue()
Target.Cancel()
Spells.Interrupt()
Misc.Pause(600)
if not Target.HasTarget():
    if Player.Poisoned:
        Spells.CastMagery('Cure')
        Target.SelfQueued()
    else:
        Spells.CastMagery('Greater Heal')
        Target.SelfQueued()
