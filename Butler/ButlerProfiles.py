from System.Collections.Generic import List
# you need to set the shared values of the following categories:
# moss, ash, root, pearl, shade, ginseng, garlic, silk
# armor (0 = no, 1 = yes)
# POTS: exp, str, refresh, agil, heal, cure
# bandages, arrows, bolts
# see examples below

#makes player name lowercase with no spaces.... if name of toon is Matsa Milla, makes it matsamilla
name = Player.Name.lower().replace(' ', '')

if name == 'playername1': #Replace playername1 with toon name, no caps or spaces
    Misc.SetSharedValue('moss', 75)
    Misc.SetSharedValue('ash', 75)
    Misc.SetSharedValue('root', 75)
    Misc.SetSharedValue('pearl', 75)
    Misc.SetSharedValue('shade', 75)
    Misc.SetSharedValue('ginseng', 75)
    Misc.SetSharedValue('garlic', 75)
    Misc.SetSharedValue('silk', 75)
    Misc.SetSharedValue('bandies', 100)
    Misc.SetSharedValue('exp', 0)
    Misc.SetSharedValue('str', 10)
    Misc.SetSharedValue('refresh', 10)
    Misc.SetSharedValue('agil', 10)
    Misc.SetSharedValue('heal', 10)
    Misc.SetSharedValue('cure', 10)
    Misc.SetSharedValue('armor', 0)
    Misc.SetSharedValue('arrows', 0)
    Misc.SetSharedValue('bolts', 0)  
elif name == 'playername2': #Replace playername2 with toon name, no caps or spaces
    Misc.SetSharedValue('moss', 0)
    Misc.SetSharedValue('ash', 0)
    Misc.SetSharedValue('root', 0)
    Misc.SetSharedValue('pearl', 0)
    Misc.SetSharedValue('shade', 0)
    Misc.SetSharedValue('ginseng', 0)
    Misc.SetSharedValue('garlic', 0)
    Misc.SetSharedValue('silk', 0)
    Misc.SetSharedValue('bandies', 100)
    Misc.SetSharedValue('exp', 25)
    Misc.SetSharedValue('str', 10)
    Misc.SetSharedValue('refresh', 30)
    Misc.SetSharedValue('agil', 10)
    Misc.SetSharedValue('heal', 20)
    Misc.SetSharedValue('cure', 15)
    Misc.SetSharedValue('arrows', 0)
    Misc.SetSharedValue('bolts', 0)  
    Misc.SetSharedValue('armor', 0)   
        
Misc.ScriptRun('ButlerHelper.py')
