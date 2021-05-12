# This will use a moongate within 2 tiles, and accept the gump if there is one.
# By MatsaMilla, updated 4/25/20

# must import list to use it in the filters
from System.Collections.Generic import List 

# Items filter for finding moongate
gate = Items.Filter()
gate.Enabled = True
gate.OnGround = True
gate.Movable = False
gate.RangeMax = 1
gate.Graphics = List[int]( [ 0x0F6C ] )
moongate = Items.ApplyFilter(gate)

# if a moongate is found, continue
if moongate:
    # select the nearest item from list
    m = Items.Select( moongate , 'Nearest' )
    
    # Double click on the moongate found 
    Items.UseItem(m) 
    # wait for gump pop up
    Gumps.WaitForGump(3716879466, 1500)
    # click yes
    Gumps.SendAction(3716879466, 1)
else:
    # if not gates in range send message
    Misc.SendMessage('No Gate In Range',33)
