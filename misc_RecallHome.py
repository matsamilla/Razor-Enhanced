msgcolor = 62
openRunebookPause = 150

Target.ClearLastandQueue()
# mage toon
if Player.Name == "ToonName":
    Spells.CastMagery('Recall')
    Target.WaitForTarget(1500,False)
    Target.TargetExecute(0x43286FAE) # Change to serialID of your recall book
# Non Mage Toon
elif Player.Name == "ToonName":
    # Record opening book and recalling home then place here:
