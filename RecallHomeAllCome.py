Target.ClearLast()
Player.ChatSay (45, "All Come")
Spells.CastMagery('Recall')
Misc.Pause(400)
Player.ChatSay (45, "All Come")
Target.WaitForTarget(3000,False)
Target.TargetExecute(0x40CFD073)
# Change serial above to your runebook
