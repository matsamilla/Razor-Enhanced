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
 0x000743AD, # Water Dragon
 0x00049A23, # Water Wyrm
 0x000743AD, # Water Dragon
 0x0016D74B, # Death Beetle
 0x0008461B, # Lara Fox Meta
 0x000190EB, # Thomas Spider
]

hp = {
1: 'going down',
2: 'going down',
3: 'at 12%',
4: 'at 16%',
5: 'at 20%',
6: 'at 24%',    
7: 'at 28%',
8: 'at 32%',
9: 'at 36%',
10: 'at 40%',
11: 'at 44%',
12: 'at 48%',
13: 'at 52%',
14: 'at 56%',
15: 'at 60%',
16: 'at 64%',
17: 'at 68%',
18: 'at 72%',
19: 'at 76%',
20: 'at 80%',
21: 'at 84%',
22: 'at 88%',
23: 'at 92%',
24: 'at 96%',
25: 'at 100%',
}    

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
        elif g.Hits < 23 and Player.InRangeMobile(g, 1):
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

