# Recall Home by MatsaMilla
# Insert name without spaces and all lowercase.
# Example: "Player Name" needs to be "playername"

msgcolor = 62
openRunebookPause = 150
pname = Player.Name.lower().replace(' ', '')

Target.ClearLastandQueue()
# mage toon (name no spaces all lowercase)
if pname == "toonname":
    Spells.CastMagery('Recall')
    Target.WaitForTarget(1500,False)
    Target.TargetExecute(0x43286FAE) # Change to serialID of your recall book
# Non Mage Toon (name no spaces all lowercase)
elif pname == "toonname2":
    # Record opening book and recalling home in new script, then copy/paste here:
# mage toon (name no spaces all lowercase)
elif pname == "toonname3":
    Spells.CastMagery('Recall')
    Target.WaitForTarget(1500,False)
    Target.TargetExecute(0x43286FAE) # Change to serialID of your recall book

# to add more, copy-paste one of the elif's (mage or non mage) below last.
