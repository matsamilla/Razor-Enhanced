# in dress agent create one that is your player name
# without spaces and all lowercase.
# Example: "Player Name" needs to be playername
msgcolor = 62
dresslist = Player.Name.lower().replace(' ', '')

#Player.HeadMessage(msgcolor, "Dressing")
Dress.ChangeList(dresslist)
Dress.DressFStart()