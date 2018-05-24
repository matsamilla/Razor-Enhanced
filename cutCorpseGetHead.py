#standard imports
import sys
from System.Collections.Generic import List

#global types
#generic
self_pack = Player.Backpack.Serial

headList = List[int]((0x1CE1))

def getHead():
    headFilter = Items.Filter()
    headFilter.Enabled = True
    headFilter.OnGround = True
    headFilter.Movable = True
    headFilter.Graphics = headList
    headFilter.RangeMax = 2
    
    heads = Items.ApplyFilter(headFilter)
    for head in heads:
        if 'head' in head:
            Misc.SendMessage(head.Name)
            Items.Move(head, self_pack, 0)
            Misc.Pause(700)
            
getHead() 