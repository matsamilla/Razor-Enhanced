# By Spatchel & Matsamilla
# Last updated by Matsamilla to work with leather dye tubs 6/15/20

from System.Collections.Generic import List
# 4 = equip armor, 5 = bag regs, 6 = bag pots
switch = List[int]([0,4])
player_bag = Items.FindBySerial(Player.Backpack.Serial)

butlerID = 0x0029C3D1 #add your butler serial here

###########################################################
# Edit this section if you dont run other per-player macro#
###########################################################
regs = 50 # default reg count if not profile
armor = 0 # default armor, 0=no 1=yes
cap = False # false for never cap, ever ever
bandies = 120 # default bandage count
arrows = 0
bolts = 0
############################################################
randomPause = 150

saveSwitch = 3
withdrawSwitch = 6
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
    ginseng11 = Misc.ReadSharedValue('ginseng')
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
    if cap:
        cap0 = armorS
    else:
        cap0 = 0
    gorget1 = armorS
    sleeves2 = armorS
    gloves3 = armorS
    tunic4 = armorS
    legs5 = armorS
else:
    if cap:
        cap0 = armor
    else:
        cap0 = 0
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
if Misc.CheckSharedValue('cure'):
    cure19 = Misc.ReadSharedValue('cure')
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

def dumpBottles():
    for i in player_bag.Contains:
        if i.ItemID == 0x0F0E:
            Items.Move(i, butlerID, 0)
            Misc.Pause(600)
def saveProfile(textid, text):
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, saveSwitch, switch, textid, text) #change 3 to 5 w/ tub
    Misc.Pause(randomPause)
    
def butler():
    Mobiles.UseMobile(butlerID)
    Gumps.WaitForGump(989312372, 2000)
    if Gumps.LastGumpTextExist( 'Remove Leather Tub?' ):
        Misc.SendMessage('Leather Tub Detected')
        saveSwitch = 5
        withdrawSwitch = 8
    else:
        saveSwitch = 3
        withdrawSwitch = 6
    
    #################### Armor #######################################
    textid = List[int]([0])
    text = List[str]([str(cap0)])
    saveProfile(textid, text)

    textid = List[int]([1])
    text = List[str]([str(gorget1)])
    saveProfile(textid, text)
    
    textid = List[int]([2])
    text = List[str]([str(sleeves2)])
    saveProfile(textid, text)
    
    textid = List[int]([3])
    text = List[str]([str(gloves3)])
    saveProfile(textid, text)
    
    textid = List[int]([4])
    text = List[str]([str(tunic4)])
    saveProfile(textid, text)
    
    textid = List[int]([5])
    text = List[str]([str(legs5)])
    saveProfile(textid, text)
    
    #################### REGS #######################################
    # Moss
    textid = List[int]([6])
    text = List[str]([str(moss6)])
    saveProfile(textid, text)
    
    #Ash
    textid = List[int]([7])
    text = List[str]([str(ash7)])
    saveProfile(textid, text)
    
    #Root
    textid = List[int]([8])
    text = List[str]([str(root8)])
    saveProfile(textid, text)
    
    #Pearl
    textid = List[int]([9])
    text = List[str]([str(pearl9)])
    saveProfile(textid, text)
    
    #Nightshade
    textid = List[int]([10])
    text = List[str]([str(shade10)])
    saveProfile(textid, text)
    
    #Ginseng
    textid = List[int]([11])
    text = List[str]([str(ginseng11)])
    saveProfile(textid, text)
    
    #garlic
    textid = List[int]([12])
    text = List[str]([str(garlic12)])
    saveProfile(textid, text)
    
    #SpidersSilk
    textid = List[int]([13])
    text = List[str]([str(silk13)])
    saveProfile(textid, text)
    
    #################### Potions ###################################
    #explode
    textid = List[int]([14])
    text = List[str]([str(exp14)])
    saveProfile(textid, text)
    
    #Strength
    textid = List[int]([15])
    text = List[str]([str(str15)])
    saveProfile(textid, text)
    
    #Refresh
    textid = List[int]([16])
    text = List[str]([str(refresh16)])
    saveProfile(textid, text)
    
    #Agility
    textid = List[int]([17])
    text = List[str]([str(agi17)])
    saveProfile(textid, text)
    
    #Heal
    textid = List[int]([18])
    text = List[str]([str(heal18)])
    saveProfile(textid, text)
    
    #Cure
    textid = List[int]([19])
    text = List[str]([str(cure19)])
    saveProfile(textid, text)
    
    #################### Bandages ###################################
    textid = List[int]([20])
    text = List[str]([str(bandages20)])
    saveProfile(textid, text)
    
    #################### Petals #####################################
    textid = List[int]([23])
    text = List[str]([str(0)])
    saveProfile(textid, text)
    
    textid = List[int]([24])
    text = List[str]([str(arrows24)])
    saveProfile(textid, text)
    
    #################### Arrows/Bolts ###############################
    textid = List[int]([25])
    text = List[str]([str(bolts25)])
    saveProfile(textid, text)

    Gumps.WaitForGump(989312372, 2000)
    #Gumps.SendAction(989312372, 6)
    Gumps.SendAdvancedAction(989312372, withdrawSwitch, switch) #change to 8 w/ tub

dumpBottles()
butler()
