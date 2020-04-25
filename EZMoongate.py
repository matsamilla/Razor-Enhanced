# This will use a moongate within 2 tiles, and accept the gump if there is one.
# By MatsaMilla, updated 4/25/20

from System.Collections.Generic import List 

# Filters
gate = Items.Filter()
gate.Enabled = True
gate.OnGround = True
gate.Movable = False
gate.RangeMax = 2
gate.Graphics = List[int]( [ 0x0F6C ] )
moongate = Items.ApplyFilter(gate)

if moongate:
    m = Items.Select( moongate , 'Nearest' )
    Items.UseItem(m) # Double click on the moongate found 
    Gumps.WaitForGump(3716879466, 1500)
    Gumps.SendAction(3716879466, 1)
else:
    Misc.SendMessage('No Gate In Range',33)
