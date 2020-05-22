# recharges blaze pouches
# target pouch, it'll trap till full.
# By MatsaMilla

trapcharges = 1

blazePouch = Target.PromptTarget('Target Pouch')

Journal.Clear()
while trapcharges < 30:
    Spells.CastMagery('Magic Trap')
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(blazePouch)
    Misc.Pause(800)
    Misc.SendMessage(trapcharges)
    trapcharges = trapcharges +1
    
    if Journal.Search('This pouch can only hold 30 charges.'):
        Stop
    
    if Player.Mana < 20:
        Player.UseSkill("Meditation")
        while Player.Mana < Player.ManaMax:
            Misc.Pause(100)
    