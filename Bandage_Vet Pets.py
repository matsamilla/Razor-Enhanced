# Pet Vet by Matsamilla, updated 6/21/20
# This script relys on Bandage_Timer.py, if you do not have it, it will not work
# Add the serials of pets you want to heal to the petList
from System.Collections.Generic import List
from System import Byte
import sys

#Pet list you can add to it by putting the pets Serial number in the list. 
petList = [
# PetList
 0x00120786,# Winged Snek
 0x003FAA39,# Kuzco
 0x00049A23,# Water Wyrm
 0x0016D74B,# Pacha
 0x001BF91B # Matsa- Mare
]

# quits if you have less than 80 HP
if Player.GetRealSkillValue('Veterinary') < 80:
    Stop

petfilter = Mobiles.Filter()
petfilter.Enabled = True
petfilter.RangeMax = 1
petfilter.IsHuman = False
petfilter.IsGhost = False
petfilter.Serials = List[int] (petList)

while Player.IsGhost == False: 
    
    if not Misc.ScriptStatus('Bandage_Timer.py'):
        Misc.ScriptRun('Bandage_Timer.py')
    
    petList = Mobiles.ApplyFilter(petfilter) 
            
    for g in petList:
        g = Mobiles.Select(petList, 'Weakest')
        
        #bandage        
        #check health level if in range one of guilded meta pet heals with bandages.          
        if g.Hits < 23 and Player.InRangeMobile(g, 1):
            if Misc.ReadSharedValue('bandageDone') == True:
                if Target.HasTarget( ) == False:
                    Items.UseItemByID(0x0E21, -1)
                    Target.WaitForTarget(1500, True)
                    Target.TargetExecute(g)
                    Misc.Pause (500)
                    break
    Misc.Pause(50)
