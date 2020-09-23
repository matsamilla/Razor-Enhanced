# Target Aquire by MatsaMilla
from System.Collections.Generic import List
from System import Byte
import sys
# range at which target will aquire
targetRange = 12

# filter
def find(notoriety):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = targetRange
    fil.IsHuman = True
    fil.IsGhost = False
    fil.Friend = False
    fil.Notorieties = List[Byte](bytes([notoriety]))
    list = Mobiles.ApplyFilter(fil)

    return list

# Possible Selections:
# 1 blue, 2 green, 3 grey, 4 grey(agro), 5 orange, 6 red, 7 invul
# Random, Nearest,Farthest, Weakest, Strongest, Next

# if your toon is blue, green, or gray
if (Player.Notoriety == 1 or Player.Notoriety == 2 or Player.Notoriety == 3):
    orangeMobile = Mobiles.Select(find(5),'Nearest')
    redMobile = Mobiles.Select(find(6),'Nearest')
    greyMobile = Mobiles.Select(find(3),'Nearest')
    if orangeMobile:
        Misc.SendMessage('Changing last target to ' + orangeMobile.Name)
        Target.SetLast(orangeMobile)
        Target.TargetExecute(orangeMobile)
    elif redMobile:
        Misc.SendMessage('Changing last target to ' + redMobile.Name)
        Target.SetLast(redMobile)
        Target.TargetExecute(redMobile)
    elif greyMobile:
        Misc.SendMessage('Changing last target to ' + greyMobile.Name)
        Target.SetLast(greyMobile)
        Target.TargetExecute(greyMobile)

# if your toon is red
elif Player.Notoriety == 6:
    blueMobile = Mobiles.Select(find(1),'Nearest')
    if blueMobile:
        Misc.SendMessage('Changing last target to ' + blueMobile.Name)
        Target.SetLast(blueMobile)
        Target.TargetExecute(blueMobile)
    elif orangeMobile:
        Misc.SendMessage('Changing last target to ' + orangeMobile.Name)
        Target.SetLast(orangeMobile)
        Target.TargetExecute(orangeMobile)
    elif redMobile:
        Misc.SendMessage('Changing last target to ' + redMobile.Name)
        Target.SetLast(redMobile)
        Target.TargetExecute(redMobile)
    elif greyMobile:
        Misc.SendMessage('Changing last target to ' + greyMobile.Name)
        Target.SetLast(greyMobile)
        Target.TargetExecute(greyMobile)
