# This script will run UNTIL you stop it. If you hotkey it, think of it as an on/off switch.
# Add the serials of pets you want to heal to the petList
from System.Collections.Generic import List
from System import Byte
import sys

#Pet list you can add to it by putting the mobileID number in the list. 
petList = [
# PetList
 0x00120786, # Meta Dragon
 0x0005D79D, # night llama
 0x00049A23, # Water Wyrm
 0x0016D74B, # Death Beetle
]


petfilter = Mobiles.Filter()
petfilter.Enabled = True
petfilter.RangeMax = 15
petfilter.IsHuman = False
petfilter.IsGhost = False
petfilter.Serials = List[int] (petList)

while Player.IsGhost == False: 
    
    petList = Mobiles.ApplyFilter(petfilter)   
    for g in petList:
        g = Mobiles.Select(petList, 'Weakest')
        
        #bandage        
        #check health level if in range one of guilded meta pet heals with bandages.          
        if g.Hits < 23 and Player.InRangeMobile(g, 1):
            if Journal.Search("finish applying") or Timer.Check("bandies") == False: 
                if Target.HasTarget( ) == False:
                    Items.UseItemByID(0x0E21, -1)
                    Target.WaitForTarget(1500, True)
                    Target.TargetExecute(g)
                    Misc.Pause (500)
                    Journal.Clear()
                    Timer.Create("bandies", 10000)
                    break
        
        if Journal.Search("too far away"):
            Journal.Clear()
        elif Journal.Search("stay close enough"):
            Player.HeadMessage(95, "You moved")
            Journal.Clear()

Target.ClearLastandQueue()
Target.Cancel() 

