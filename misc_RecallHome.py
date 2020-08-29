msgcolor = 62
openRunebookPause = 150

Target.ClearLastandQueue()
# mage toon
if Player.Name == "ToonName":
    Spells.CastMagery('Recall')
    Target.WaitForTarget(1500,False)
    Target.TargetExecute(0x43286FAE)
# Non Mage Toon
elif Player.Name == "ToonName":
    Items.UseItem(0x423A667B)
    Misc.Pause(openRunebookPause)
    Gumps.WaitForGump(1431013363, 10000)
    Gumps.SendAction(1431013363, 2)