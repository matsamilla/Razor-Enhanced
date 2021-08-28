delayTime = 600

# add (Name, PlayerSerial, MountSerial, True/False) to list 
#   True if you want toon to DISMOUNT + ALL KILL + TARGET LAST
dismountList = [ 
#   (PlayerName, PlayerSerial, MountSerial, True/False)
    ("MGD" , 0x0000B71C , 0x003FAA39 , True ), 
    ("Moltar" , 0x003C518F , 0x0007E386 , True ), 
    ("EmGD" , 0x00255122 , 0x00215F22 , False),
    ("UselessGuy" , 0x0022FE20 , 0x0006EB2A , False ),
    ("Matsa" , 0x000470E6 , 0x0000 , False ),
    ("Matsa-" , 0x001DF0B7 , 0x0028E693 , False ),
    ("Thicc" , 0x0016218A , 0x0001E6B3 , False),
    ("MatsaAxa", 0x0000 , 0x00285C67 , False),
    ("Nalfein" , 0x000B519E , 0x00823AEA , False ),
    ("MatsaMilla" , 0x0002DC9C , 0x0007A37B , False ),
    ("useless", 0x000AE1A2 , 0x000803D8 , False),
] 
    
    
def dismount(mountSerial, attack):
    if Player.Mount:
        if attack:
            lastTarget = Mobiles.FindBySerial( Target.GetLast() )
            if lastTarget:
                if lastTarget != Player.Serial:
                    if Player.DistanceTo(lastTarget) < 12:
                        Mobiles.UseMobile(Player.Serial)
                        Misc.Pause(100)
                        Player.ChatSay(33, 'All Kill')
                        Target.WaitForTarget(1500)
                        Target.TargetExecute(lastTarget)
    
        else:
            Mobiles.UseMobile(Player.Serial)
            Misc.Pause(120)
            mount = Mobiles.FindBySerial(mountSerial)
            if mount:
                if mount.Body == 0x0317:
                    Misc.WaitForContext(mount, 1500)
                    Misc.Pause(150)
                    if Player.Visible:
                        Misc.ContextReply(mountSerial, "Open Backpack")
                    else:
                        Misc.ContextReply(mountSerial, "Open Backpack")
    
    elif mountSerial != None:
        mount = Mobiles.FindBySerial(mountSerial)
        while Player.DistanceTo(mount) > 1:
            if Timer.Check('MountTimer') == False:
                Player.ChatSay(66, mount.Name + ' Come')
                Timer.Create('MountTimer', 500)
            Misc.Pause(50)
        Mobiles.UseMobile(mountSerial)

        
for d in dismountList: 
    if Player.Serial == d[1]:
        dismount(d[2], d[3])
        break

