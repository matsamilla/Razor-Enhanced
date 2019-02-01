from System.Collections.Generic import List
# you need to set the shared values of the following categories:
# moss, ash, root, pearl, shade, ginseng, garlic, silk
# armor (0 = no, 1 = yes)
# POTS: exp, str, refresh, agil, heal, cure
# bandages, arrows, bolts
# see examples below

####### RESTOCK BUTLER ##################
#backpack = Player.Backpack.Serial
#Mobiles.UseMobile(0x0029C3D1)
#Gumps.WaitForGump(989312372, 10000)
#Gumps.SendAction(989312372, 5)
#Target.WaitForTarget(10000, False)
#Target.TargetExecute(backpack)
#Gumps.WaitForGump(989312372, 10000)
#Gumps.CloseGump(989312372)
#Misc.Pause(1000)
##########################################

#makes lower case & no spaces for character name
name = Player.Name.lower().replace(' ', '')

#name must be all lowercase with no spaces
if name == 'NameOfToon1':
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
elif name == 'NameOfToon2':
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
    
    
Misc.ScriptRun('ButlerHelper.py')
