# Mount/Dismount/Attack script by MatsaMilla
# last updated 5/14/20

self = Player.Serial
dragTime = 600

# I use this for tamers, will All Kill & target last target when you dismount
# then call pet to you until close enough to mount again.
dismountAttackList = [ "Toon Name 1", "Toon Name 4" ] # good for tamers

# I use this for toons with beetles & toons with stealth
dismountOnly = [ "Toon Name 2" , "Toon Name 3"  ]

if Player.Name == "Toon Name 1":
    mountID = MountSerial
    
elif Player.Name == "Toon Name 2":
    mountID = MountSerial
    
elif Player.Name == "Toon Name 3":
    mountID = MountSerial
    
elif Player.Name == "Toon Name 4":
    mountID = MountSerial


def dismount():
    if Player.Mount:
        Mobiles.UseMobile(self)
        Misc.Pause(100)
        mount = Mobiles.FindBySerial(mountID)
        if mount.Body == 0x0317: #mountID != None:
            Misc.WaitForContext(mountID, 1500)
            Misc.ContextReply(mountID, "Open Backpack")
    
    elif mountID != None:
        Mobiles.UseMobile(mountID)
        
        
def dismountAttack():
    attackMount = Mobiles.FindBySerial(mountID)
    if Player.Mount:
        Mobiles.UseMobile(self)
        Misc.Pause(100)
        Player.ChatSay(33, 'All Kill')
        Target.WaitForTarget(1500)
        Target.Last()
    else:
        while Player.DistanceTo(attackMount) > 1:
            if Timer.Check('MountTimer') == False:
                Player.ChatSay(66, 'All Come')
                Timer.Create('MountTimer', 500)
            Misc.Pause(50)
        Mobiles.UseMobile(mountID)
        
        
if Player.Name in dismountAttackList: 
    dismountAttack()
    
elif Player.Name in dismountOnly:
    dismount()
