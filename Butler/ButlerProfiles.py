# ButlerProfiles.py by MatsaMilla - 2 part script, part 1 is ButlerHelper.py

# You need to set up a "profile" for each toon based on name
# see examples below
# Note - armor (0 = no, 1 = yes) (all but cap)
#        cap (0 = no, 1 = yes)   (cap only)
# If upgrading, add this line to your profiles to take a cap: Misc.SetSharedValue('cap', 1)

#makes player name lowercase with no spaces.... if name of toon is Matsa Milla, makes it matsamilla
name = Player.Name.lower().replace(' ', '')

if name == 'matsamilla': #Replace matsamilla with toon name, no caps or spaces
    Misc.SendMessage('Loading: ' + name)
    Misc.SetSharedValue('moss', 75)
    Misc.SetSharedValue('ash', 75)
    Misc.SetSharedValue('root', 75)
    Misc.SetSharedValue('pearl', 75)
    Misc.SetSharedValue('shade', 75)
    Misc.SetSharedValue('ginseng', 75)
    Misc.SetSharedValue('garlic', 75)
    Misc.SetSharedValue('silk', 75)
    Misc.SetSharedValue('bandies', 50)
    Misc.SetSharedValue('exp', 10)
    Misc.SetSharedValue('str', 10)
    Misc.SetSharedValue('refresh', 20)
    Misc.SetSharedValue('agil', 10)
    Misc.SetSharedValue('heal', 15)
    Misc.SetSharedValue('cure', 10)
    Misc.SetSharedValue('arrows', 0)
    Misc.SetSharedValue('bolts', 0)  
    Misc.SetSharedValue('armor', 1)
    Misc.SetSharedValue('cap', 1)
#******************
# copy, paste and edit as many as this next section as you need for toons
elif name == 'playername': #Replace playername with toon name, no caps or spaces
    Misc.SendMessage('Loading: ' + name)
    Misc.SetSharedValue('moss', 0)
    Misc.SetSharedValue('ash', 0)
    Misc.SetSharedValue('root', 0)
    Misc.SetSharedValue('pearl', 0)
    Misc.SetSharedValue('shade', 0)
    Misc.SetSharedValue('ginseng', 0)
    Misc.SetSharedValue('garlic', 0)
    Misc.SetSharedValue('silk', 0)
    Misc.SetSharedValue('bandies', 100)
    Misc.SetSharedValue('exp', 0)
    Misc.SetSharedValue('str', 10)
    Misc.SetSharedValue('refresh', 20)
    Misc.SetSharedValue('agil', 10)
    Misc.SetSharedValue('heal', 10)
    Misc.SetSharedValue('cure', 10)
    Misc.SetSharedValue('arrows', 0)
    Misc.SetSharedValue('bolts', 0)  
    Misc.SetSharedValue('armor', 0)   
    Misc.SetSharedValue('cap', 0)
    
#******************

Misc.ScriptRun('ButlerHelper.py')
