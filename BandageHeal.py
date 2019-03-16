# Bandage Heals by MatsaMilla
# Hopefully improved bandage timer

import sys

banTime = 0
msgcolor = 76

#pause for skill check at login
Misc.Pause(5000)

    
if Player.GetRealSkillValue("Healing") < 80:
    Misc.SendMessage('No Healing, stopping script')
    Misc.Pause(100)
    sys.exit()

Journal.Clear()

def bandageTimer():
    Journal.Clear()
    banTime = 0
    while Timer.Check("bandies") == True:
        banTime = banTime + 1
        Misc.SendMessage(banTime, msgcolor)
        Misc.Pause(1000)
        
        if Journal.Search("finish applying"):
            Journal.Clear()
            Timer.Create("bandies", 1)

def bandageSelf():
    if Journal.Search("finish applying") or Timer.Check("bandies") == False:
        Journal.Clear()
        #Misc.Pause (500)
        Items.UseItemByID(0x0E21, 0)
        Target.WaitForTarget(1500, False)
        Target.Self()
        Misc.Pause (500)
        if Journal.Search("You begin applying the bandages"):
            Journal.Clear()
            Timer.Create("bandies", 15000)
            bandageTimer()
        else:
            Journal.Clear()
            bandageSelf()
        
while True:
    while Player.IsGhost:
        Misc.Pause(50)
        Misc.NoOperation()
    while Player.Hits == Player.HitsMax and not Player.Poisoned:
        Misc.Pause(50)
        Misc.NoOperation()
        
    if Journal.Search("You begin applying the bandages"):
        Journal.Clear()
        Timer.Create("bandies", 15000)
        bandageTimer()
    
    #bandage
    if Items.BackpackCount(0x0E21 ,-1):
        if Player.Visible == True and Player.Hits < Player.HitsMax or Player.Poisoned: 
            bandageSelf()
                
    elif Timer.Check("ohno") == False:
        Player.HeadMessage(33, "Out of bandages!")
        Timer.Create("ohno", 8000)
        Misc.Pause(50)

