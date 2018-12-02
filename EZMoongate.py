#moongate clicker

from System.Collections.Generic import List 

# Filters
gate = Items.Filter()
gate.Enabled = True
gate.OnGround = True
gate.Movable = False
gate.RangeMax = 2
moongate = Items.ApplyFilter(gate)

for m in moongate: # Look for items in filter
    if m.ItemID == 0x0F6C: # Return true if found a moongate = 0x0F6C
        Items.UseItem(m) # Double click on the moongate found 
