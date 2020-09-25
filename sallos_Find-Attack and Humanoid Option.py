# Target Closest, Attack and Humanoid only options by Prioriety
#   aka sallos target find
# by MatsaMilla & contributions by Trick Tickler
from System.Collections.Generic import List
from System import Byte
import sys

# true to attack on execution
attack = True

# true for humanoid only
humanoid = False

# range at which target will aquire
targetRange = 12

# filter
def find(notoriety):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = targetRange
    if humanoid:
        fil.IsHuman = True
    fil.IsGhost = False
    fil.Friend = False
    fil.Notorieties = List[Byte](bytes(notoriety))
    list = Mobiles.ApplyFilter(fil)

    return list

# Possible Selections:
# 1 blue, 2 green, 3 grey, 4 grey(agro), 5 orange, 6 red, 7 invul
# Random, Nearest,Farthest, Weakest, Strongest, Next

# if your toon is blue, green, or gray or militia
if (Player.Notoriety == 1 or Player.Notoriety == 2 or Player.Notoriety == 3):
    greyMobile = Mobiles.Select(find([3,4]),'Nearest')
    orangeMobile = Mobiles.Select(find([5]),'Nearest')
    redMobile = Mobiles.Select(find([6]),'Nearest')
    if orangeMobile:
        Misc.SendMessage('Changing last target to ' + orangeMobile.Name)
        Target.SetLast(orangeMobile)
        if attack:
            Player.Attack(orangeMobile)
    elif redMobile:
        Misc.SendMessage('Changing last target to ' + redMobile.Name)
        Target.SetLast(redMobile)
        if attack:
            Player.Attack(redMobile)
    elif greyMobile:
        Misc.SendMessage('Changing last target to ' + greyMobile.Name)
        Target.SetLast(greyMobile)
        if attack:
            Player.Attack(greyMobile)

# if your toon is red
elif Player.Notoriety == 6:
    blueMobile = Mobiles.Select(find([1]),'Nearest')
    greyMobile = Mobiles.Select(find([3,4]),'Nearest')
    orangeMobile = Mobiles.Select(find([5]),'Nearest')
    redMobile = Mobiles.Select(find([6]),'Nearest')
    if blueMobile:
        Misc.SendMessage('Changing last target to ' + blueMobile.Name)
        Target.SetLast(blueMobile)
        if attack:
            Player.Attack(blueMobile)
    elif greyMobile:
        Misc.SendMessage('Changing last target to ' + greyMobile.Name)
        Target.SetLast(greyMobile)
        if attack:
            Player.Attack(greyMobile)
    elif orangeMobile:
        Misc.SendMessage('Changing last target to ' + orangeMobile.Name)
        Target.SetLast(orangeMobile)
        if attack:
            Player.Attack(orangeMobile)
    elif redMobile:
        Misc.SendMessage('Changing last target to ' + redMobile.Name)
        Target.SetLast(redMobile)
        if attack:
            Player.Attack(redMobile)