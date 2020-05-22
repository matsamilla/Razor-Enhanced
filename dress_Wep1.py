# in dress agent create one that is your player name
# without spaces and a 1 at the end.
# Example: "Player Name" needs to be playername1

msgcolor = 62
wep1 = Player.Name.lower().replace(' ', '') + '1'

Player.HeadMessage(msgcolor, "Weapon 1")
Dress.ChangeList(wep1)
Dress.DressFStart()
