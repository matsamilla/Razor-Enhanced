if Player.Poisoned:
    Spells.CastMagery('Cure')
    Target.SelfQueued()
else:
    Spells.CastMagery('Heal')
    Target.SelfQueued() 
