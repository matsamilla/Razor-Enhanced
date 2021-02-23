# Target Closest, Attack and DROP Target on nearest target
#   aka sallos target aquire
# by MatsaMilla & contributions by Trick Tickler
from System.Collections.Generic import List
from System import Byte
import sys

# true to attack, false will only set as last target
attack = True

# true to send target message to party
sendMessage = True

# true to display target overhead & over mobile
displayTarget = False

# range at which target will aquire
targetRange = 12

# filter
def find(notoriety):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = targetRange
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
    greyMobile = Mobiles.Select(find([3,4]),'Nearest',)
    orangeMobile = Mobiles.Select(find([5]),'Nearest')
    redMobile = Mobiles.Select(find([6]),'Nearest')
    if orangeMobile:
        if sendMessage:
            Player.ChatParty('Changing last target to ' + orangeMobile.Name)
        Target.SetLast(orangeMobile)
        if attack:
            Player.Attack(orangeMobile)
        if displayTarget:
            Player.HeadMessage(47, "Target: " + orangeMobile.Name)
            Mobiles.Message(orangeMobile, 15, "*Target*")
    elif redMobile:
        if sendMessage:
            Player.ChatParty('Changing last target to ' + redMobile.Name)
        Target.SetLast(redMobile)
        if attack:
            Player.Attack(redMobile)
        if displayTarget:
            Player.HeadMessage(33, "Target: " + redMobile.Name)
            Mobiles.Message(redMobile, 15, "*Target*")
    elif greyMobile:
        if sendMessage:
            Player.ChatParty('Changing last target to ' + greyMobile.Name)
        Target.SetLast(greyMobile)
        if attack:
            Player.Attack(greyMobile)
        if greyMobile:
            Player.HeadMessage(902, "Target: " + greyMobile.Name)
            Mobiles.Message(greyMobile, 15, "*Target*")
    else:
        Misc.SendMessage('No Targets', 33)

# if your toon is red
elif Player.Notoriety == 6:
    blueMobile = Mobiles.Select(find([1]),'Nearest')
    greyMobile = Mobiles.Select(find([3,4]),'Nearest')
    orangeMobile = Mobiles.Select(find([5]),'Nearest')
    redMobile = Mobiles.Select(find([6]),'Nearest')
    if blueMobile:
        if sendMessage:
            Player.ChatParty('Changing last target to ' + blueMobile.Name)
        Target.SetLast(blueMobile)
        if attack:
            Player.Attack(blueMobile)
        if displayTarget:
            Player.HeadMessage(1266, "Target: " + blueMobile.Name)
            Mobiles.Message(blueMobile, 15, "*Target*")
    elif greyMobile:
        if sendMessage:
            Player.ChatParty('Changing last target to ' + greyMobile.Name)
        Target.SetLast(greyMobile)
        if attack:
            Player.Attack(greyMobile)
        if displayTarget:
            Player.HeadMessage(902, "Target: " + greyMobile.Name)
            Mobiles.Message(greyMobile, 15, "*Target*")
    elif orangeMobile:
        if sendMessage:
            Player.ChatParty('Changing last target to ' + orangeMobile.Name)
        Target.SetLast(orangeMobile)
        if attack:
            Player.Attack(orangeMobile)
        if displayTarget:
            Player.HeadMessage(47, "Target: " + orangeMobile.Name)
            Mobiles.Message(orangeMobile, 15, "*Target*")
    elif redMobile:
        if sendMessage:
            Player.ChatParty('Changing last target to ' + redMobile.Name)
        Target.SetLast(redMobile)
        if attack:
            Player.Attack(redMobile)
        if displayTarget:
            Player.HeadMessage(33, "Target: " + redMobile.Name)
            Mobiles.Message(redMobile, 15, "*Target*")
    else:
        Misc.SendMessage('No Targets', 33)
