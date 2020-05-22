# in dress agent create one that is your player name
# without spaces and a 2 at the end.
# Example: "Player Name" needs to be playername2

msgcolor = 62
wep2 = Player.Name.lower().replace(' ', '') + '2'

Player.HeadMessage(msgcolor, "Weapon 2")
Dress.ChangeList(wep2)
Dress.DressFStart()
