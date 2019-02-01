from System.Collections.Generic import List
switch = List[int]([4])

butlerID = 0x0029C3D1 #add your butler serial here

###########################################################
# Edit this section if you dont run other per-player macro#
###########################################################
regs = 100 # default reg count if not profile
armor = 0 # default armor, 0=no 1=yes
bandies = 120 # default bandage count
arrows = 0
bolts = 0
############################################################

#moss
if Misc.CheckSharedValue('moss'):
    moss6 = Misc.ReadSharedValue('moss')
else: 
    moss6 = regs
#ash count
if Misc.CheckSharedValue('ash'):
    ash7 = Misc.ReadSharedValue('ash')
else: 
    ash7 = regs   
# root count
if Misc.CheckSharedValue('root'):
    root8 = Misc.ReadSharedValue('root')
else: 
    root8 = regs
# pearl count
if Misc.CheckSharedValue('pearl'):
    pearl9 = Misc.ReadSharedValue('pearl')
else: 
    pearl9 = regs
#nightshade count
if Misc.CheckSharedValue('shade'):
    shade10 = Misc.ReadSharedValue('shade')
else: 
    shade10 = regs
# Ginseng count
if Misc.CheckSharedValue('ginseng'):
    ginseng11 = Misc.ReadSharedValue('moss')
else: 
    ginseng11 = regs 
# Garlic Count   
if Misc.CheckSharedValue('garlic'):
    garlic12 = Misc.ReadSharedValue('garlic')
else: 
    garlic12 = regs 
# Silk Count   
if Misc.CheckSharedValue('silk'):
    silk13 = Misc.ReadSharedValue('silk')
else: 
    silk13 = regs
# Armor
if Misc.CheckSharedValue('armor'):
    armorS = Misc.ReadSharedValue('armor')
    cap0 = armorS
    gorget1 = armorS
    sleeves2 = armorS
    gloves3 = armorS
    tunic4 = armorS
    legs5 = armorS
else:
    cap0 = armor
    gorget1 = armor
    sleeves2 = armor
    gloves3 = armor
    tunic4 = armor
    legs5 = armor
# Explode Pots Count
if Misc.CheckSharedValue('exp'):
    exp14 = Misc.ReadSharedValue('exp')
else: 
    exp14 = 0
# Strength Pots Count
if Misc.CheckSharedValue('str'):
    str15 = Misc.ReadSharedValue('str')
else: 
    str15 = 0
# Refresh Pots Count
if Misc.CheckSharedValue('refresh'):
    refresh16 = Misc.ReadSharedValue('refresh')
else: 
    refresh16 = 0
# Agility Pots Count    
if Misc.CheckSharedValue('agil'):
    agi17 = Misc.ReadSharedValue('agil')
else: 
    agi17 = 0
# Heal Pots Count    
if Misc.CheckSharedValue('heal'):
    heal18 = Misc.ReadSharedValue('heal')
else: 
    heal18 = 0
# Cure Pots Count    
if Misc.CheckSharedValue('heal'):
    cure19 = Misc.ReadSharedValue('heal')
else: 
    cure19 = 0
# Bandages Pots Count    
if Misc.CheckSharedValue('bandies'):
    bandages20 = Misc.ReadSharedValue('bandies')
else: 
    bandages20 = bandies
# Arrows
if Misc.CheckSharedValue('arrows'):
    arrows24 = Misc.ReadSharedValue('arrows')
else: 
    arrows24 = arrows    
# Bolts
if Misc.CheckSharedValue('bolts'):
    bolts25 = Misc.ReadSharedValue('bolts')
else: 
    bolts25 = bolts

def butler():
    #################### Armor #######################################
    textid = List[int]([0])
    text = List[str]([str(cap0)])
    Mobiles.UseMobile(butlerID)
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    textid = List[int]([1])
    text = List[str]([str(gorget1)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    textid = List[int]([2])
    text = List[str]([str(sleeves2)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    textid = List[int]([3])
    text = List[str]([str(gloves3)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    textid = List[int]([4])
    text = List[str]([str(tunic4)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    textid = List[int]([5])
    text = List[str]([str(legs5)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    #################### REGS #######################################
    # Moss
    textid = List[int]([6])
    text = List[str]([str(moss6)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    #Ash
    textid = List[int]([7])
    text = List[str]([str(ash7)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    #Root
    textid = List[int]([8])
    text = List[str]([str(root8)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    #Pearl
    textid = List[int]([9])
    text = List[str]([str(pearl9)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    #Nightshade
    textid = List[int]([10])
    text = List[str]([str(shade10)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    #Ginseng
    textid = List[int]([11])
    text = List[str]([str(ginseng11)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    #garlic
    textid = List[int]([12])
    text = List[str]([str(garlic12)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    #SpidersSilk
    textid = List[int]([13])
    text = List[str]([str(silk13)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    #################### Potions ###################################
    #explode
    textid = List[int]([14])
    text = List[str]([str(exp14)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    #Strength
    textid = List[int]([15])
    text = List[str]([str(str15)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    #Refresh
    textid = List[int]([16])
    text = List[str]([str(refresh16)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    #Agility
    textid = List[int]([17])
    text = List[str]([str(agi17)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    #Heal
    textid = List[int]([18])
    text = List[str]([str(heal18)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    #Cure
    textid = List[int]([19])
    text = List[str]([str(cure19)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    #################### Bandages ###################################
    textid = List[int]([20])
    text = List[str]([str(bandages20)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    textid = List[int]([24])
    text = List[str]([str(arrows24)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 3, switch, textid, text)
    #################### Arrows/Bolts ###############################
    textid = List[int]([25])
    text = List[str]([str(bolts25)])
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, 6, switch, textid, text)

butler()
