# Version 2.0 - updated 12/30/20
# recharges blaze pouches in pack. MUST HAVE TOOL TIPS ENABLED
# By MatsaMilla

for i in Player.Backpack.Contains:
    if i.ItemID == 0x0E79 and i.Hue == 0x0489:
        Items.WaitForProps( i , 1000 )
        charges = Items.GetPropValue(i,"Charges")
        if charges:
            if charges < 30:
                while charges < 30:
                    Spells.CastMagery('Magic Trap')
                    Target.WaitForTarget(10000, False)
                    Target.TargetExecute(i)
                    Misc.Pause(800)
                    Items.WaitForProps( i , 1000 )
                    charges = Items.GetPropValue(i,"Charges")
                    if Player.Mana < 20:
                        Player.UseSkill("Meditation")
                        while Player.Mana < Player.ManaMax:
                            Misc.Pause(100)
        

# blazePouch = Items.FindBySerial( Target.PromptTarget('Target Pouch') )
# trapcharges = 1

# Journal.Clear()
# while trapcharges < 30:
   # Spells.CastMagery('Magic Trap')
   # Target.WaitForTarget(10000, False)
   # Target.TargetExecute(blazePouch)
   # Misc.Pause(800)
   # Misc.SendMessage(trapcharges)
   # trapcharges = trapcharges +1
   
   # if Journal.Search('This pouch can only hold 30 charges.'):
       # Stop
   
   # if Player.Mana < 20:
       # Player.UseSkill("Meditation")
       # while Player.Mana < Player.ManaMax:
           # Misc.Pause(100)
