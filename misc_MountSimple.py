# Simple mount macro by MatsaMilla
# must set mount every time Enhanced is opened, on each toon on account if needed

if Misc.CheckSharedValue('mount'+ str(Player.Serial)):
    mountSerial = Misc.ReadSharedValue('mount'+ str(Player.Serial))
else:
    mountSerial = None
    
if Player.Mount:
    Mobiles.UseMobile(Player.Serial)
else:
    if mountSerial != None:
        mount = Mobiles.FindBySerial(mountSerial)
        while Player.DistanceTo(mount) > 1:
            if Timer.Check('MountTimer') == False:
                Player.ChatSay(66, mount.Name + ' Come')
                Timer.Create('MountTimer', 500)
            Misc.Pause(50)
        Mobiles.UseMobile(mount)
    else:
        Player.HeadMessage(66,"Target Mount")
        mountSerial = Target.PromptTarget("Target Mount",33)
        mount = Mobiles.FindBySerial( mountSerial )
        Misc.SetSharedValue('mount'+ str(Player.Serial),mountSerial)
        while Player.DistanceTo(mount) > 1:
            if Timer.Check('MountTimer') == False:
                Player.ChatSay(66, mount.Name + ' Come')
                Timer.Create('MountTimer', 500)
            Misc.Pause(50)
        Mobiles.UseMobile(mount)
