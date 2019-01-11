from System.Collections.Generic import List
from System import Byte
import sys

tfilter = Mobiles.Filter()
tfilter.Enabled = True
tfilter.RangeMin = 0
tfilter.RangeMax = 9
tfilter.IsHuman = False
tfilter.IsGhost = False
tfilter.Notorieties = List[Byte](bytes([3,4,5]))
tfilter.Friend = False
  
def provoTwoNearest() :
    Journal.Clear()
    provo1 = provo2 =  0
    provoshit = []
    instruments = [0xe9e, 0x2805, 0xe9c, 0xeb3, 0xeb1, 0x0eb2] #no tamborine(0x0E9D), my *newbied* one
    msgColour = 55

    enemies = Mobiles.ApplyFilter(tfilter)
    Mobiles.Select(enemies,'Hostile')
    if len(enemies) <= 1:
        Player.HeadMessage(msgColour, 'Not enough monsters detected')
        return False
    if len(enemies) >= 2:
        
        Target.ClearLastandQueue()
        Target.Cancel()
        
        #makes list with [Serial, DistanceTo]
        for enemy in enemies:
            provoshit.append([enemy.Serial, Player.DistanceTo(enemy)])
        
        #sorts list according to distance
        provoshit.sort(key=lambda x: x[1])
            
        #sets provo targets from list, pause is necessary    
        provo1 = provoshit[0][0]
        Misc.Pause(50)
        provoshit.pop(0)
        provo2 = provoshit[0][0]
        
        Player.UseSkill("Provocation")
        Misc.Pause(100)
        
        #skill timer not up
        if Journal.Search("You must wait"):
            Player.HeadMessage(msgColour, "Try Again, skill timer")
            Journal.Clear()
            return False
        
        #instrument check
        if Journal.Search("What instrument shall you play?"):
            for i in Player.Backpack.Contains:
                if i.ItemID in instruments:
                    Target.TargetExecute(i)
                    Player.HeadMessage(msgColour, "Instrument Found")
                    Journal.Clear()
                    Misc.Pause(200)
                    break
        
        #setlast target to show what you are provoing
        Target.SetLast(provo1)
        Target.WaitForTarget(2000 , True)
        Target.TargetExecute(provo1)
        Target.SetLast(provo2)
        Target.WaitForTarget(2000, True)
        Target.TargetExecute(provo2)
            
        return True
        
    else:
        Player.HeadMessage(msgColour, 'Something Happend')
        return False

provoTwoNearest()  
