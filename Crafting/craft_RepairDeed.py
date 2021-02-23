# Place blank scrolls in pack, have only how many you want to make (or can hold) on you.
# Target a container you want to transfer them into after it makes them.

# uncomment the type you would like to make
deedtype = 'smith'
#deedtype = 'tailor'
#deedtype = 'carp'
#deedtype = 'fletch'

hammerID = 0x13E3
tongID = 0x0FBB
scrollID = 0x0EF3
fletchID = 0x1022
sawID = 0x1034
backpack = Player.Backpack.Serial

def repairDeed(type):
    
    hammer = Items.FindByID(hammerID, -1, backpack)
    tong = Items.FindByID(tongID, -1, backpack)
    scrolls = Items.FindByID(scrollID,-1, backpack)
    sewKit = Items.FindByID(0x0F9D,-1, backpack) 
    fletch = Items.FindByID(fletchID,-1, backpack) 
    saw = Items.FindByID(sawID,-1, backpack) 
    scrolls = Items.FindByID(scrollID,-1, backpack)
    
    if type == 'smith':
        Misc.SendMessage('Crafting Smith Repair Deeds')
        if tong:
            tool = tong
        elif hammer:
            tool = hammer
        else:
            Misc.SendMessage('No Tools')
    elif type == 'tailor':
        Misc.SendMessage('Crafting Tailor Repair Deeds')
        if sewKit:
            tool = sewKit
        else:
            Misc.SendMessage('No Tools')
    elif type == 'carp':
        Misc.SendMessage('Crafting Carp Repair Deeds')
        if saw:
            tool = saw
        else:
            Misc.SendMessage('No Tools')
    elif type == 'fletch':
        Misc.SendMessage('Crafting Fletch Repair Deeds')
        if fletch:
            tool = fletch
        else:
            Misc.SendMessage('No Tools')

    
    while scrolls:
        if not Gumps.HasGump():      
            Items.UseItem(tool)
        Gumps.WaitForGump(949095101, 50)
        Gumps.SendAction(949095101, 42)
        Target.WaitForTarget(1000, False)
        Target.TargetExecute(scrolls)
        Misc.Pause(100)
        scrolls = Items.FindByID(scrollID,-1, backpack)


def moveScrolls():
    if Target.HasTarget():
        Target.Cancel()
        
    repairDeeds = Items.FindByID(0x14F0, 0x01bc, backpack)
    if repairDeeds:
        Player.HeadMessage(66, 'Target Container to Move deeds to')
        deedContainer = Target.PromptTarget()
        while repairDeeds:
            Items.Move(repairDeeds,deedContainer,0)
            Misc.Pause(600)
            repairDeeds = Items.FindByID(0x14F0, 0x01bc, backpack)
            
    
repairDeed(deedtype)
moveScrolls()
