if Player.Poisoned:
    Spells.CastMagery('Cure')
    Target.SelfQueued()
else:
    Spells.CastMagery('Greater Heal')
    Target.SelfQueued()