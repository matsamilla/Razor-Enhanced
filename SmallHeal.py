if not Target.HasTarget():
    if Player.Poisoned:
        Spells.CastMagery('Cure')
        Target.WaitForTarget(1500)
        Target.Self()
    else:
        Spells.CastMagery('Heal')
        Target.WaitForTarget(1500)
        Target.Self()
     
