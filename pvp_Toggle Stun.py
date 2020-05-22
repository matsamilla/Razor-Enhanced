Journal.Clear()
Player.WeaponStunSA( )
Misc.Pause(120)
if Journal.Search("You get yourself ready to stun your opponent."):
    Player.HeadMessage(33, "Stun: ON")

if Journal.Search("You decide to not try to stun anyone."):
    Player.HeadMessage(33, "Stun: OFF")
    
if Journal.Search("You are not skilled enough to stun your opponent."):
    Player.HeadMessage(33, "NO STUN")