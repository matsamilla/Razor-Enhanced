# ButlerHelper by Spatchel & Matsamilla
# use with ButlerProfiles.py for best results, update butlerID with butler serial below

# Last updated 6/2/22

###########################################################
# Add your butlers serial below                           #
###########################################################

butlerID = 0x0029C3D1 #add your butler serial here

###########################################################
# Option to equip armor, bag regs & bag pots below        #
###########################################################

from System.Collections.Generic import List
import sys
# 4 = equip armor, 5 = bag regs, 6 = bag pots (switch = List[int]([0,4,5,6]) would do all
switch = List[int]([0,4])

###########################################################
# If you dont run ButlerProfiles.py, this will load       #
###########################################################
regs = 30 # default reg count if not profile
armor = 0 # default armor, 0=no 1=yes
cap = 0 # cap in default profile,  0=no 1=yes
bandies = 0 # default bandage count
arrows = 0
bolts = 0
cure = 10
heal = 10
refresh = 10

######## NO TOUCHY BELOW THIS #############################

butler = Mobiles.FindBySerial(butlerID)
randomPause = 150
player_bag = Items.FindBySerial(Player.Backpack.Serial)

if butler == None:
    Player.HeadMessage(33, 'Butler not found, stoppling')
    sys.exit()
while Player.DistanceTo(butler) > 2.5:
    if Timer.Check('butler') == False:
        Mobiles.Message(butler,33, 'Come closer to restock.')
        Timer.Create('butler',2500)

#moss count
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
    elif Player.CheckLayer('Helm'):
        cap0 = 0
    else:
        cap0 = 0
    gorget1 = armorS
    sleeves2 = armorS
    gloves3 = armorS
    if Player.CheckLayer("InnerTorso"):
        tunic4 = 0
    else:
        tunic4 = armorS
    if Player.CheckLayer("Pants"):
        legs5 = 0
    else:
        legs5 = armorS
else:
    if cap:
        cap0 = armor
    elif Player.CheckLayer('Helm'):
        cap0 = 0
    else:
        cap0 = 0
    gorget1 = armor
    sleeves2 = armor
    gloves3 = armor
    if Player.CheckLayer("InnerTorso"):
        tunic4 = 0
    else:
        tunic4 = armorS
    if Player.CheckLayer("Pants"):
        legs5 = 0
    else:
        legs5 = armorS
    
# Agility Pots Count    
if Misc.CheckSharedValue('agil'):
    agiImput = Misc.ReadSharedValue('agil')
else: 
    agiImput = 5
# Cure Pots Count    
if Misc.CheckSharedValue('cure'):
    cureImput = Misc.ReadSharedValue('cure')
else: 
    cureImput = 5
# Explode Pots Count
if Misc.CheckSharedValue('exp'):
    expImput = Misc.ReadSharedValue('exp')
else: 
    expImput = 0
# Heal Pots Count    
if Misc.CheckSharedValue('heal'):
    healImput = Misc.ReadSharedValue('heal')
else: 
    healImput = 5
# Deadlypoison Pots Count    
if Misc.CheckSharedValue('deadlypoison'):
    dpImput = Misc.ReadSharedValue('deadlypoison')
else: 
    dpImput = 0
# Refresh Pots Count
if Misc.CheckSharedValue('refresh'):
    refreshImput = Misc.ReadSharedValue('refresh')
else: 
    refreshImput = 5
# Strength Pots Count
if Misc.CheckSharedValue('str'):
    strImput = Misc.ReadSharedValue('str')
else: 
    strImput = 5
# Bandages Count    
if Misc.CheckSharedValue('bandies'):
    bandages21 = Misc.ReadSharedValue('bandies')
else: 
    bandages21 = bandies
# Arrows
if Misc.CheckSharedValue('arrows'):
    arrows25 = Misc.ReadSharedValue('arrows')
else: 
    arrows25 = arrows    
# Bolts
if Misc.CheckSharedValue('bolts'):
    bolts26 = Misc.ReadSharedValue('bolts')
else: 
    bolts26 = bolts

def dumpBottles():
    for i in player_bag.Contains:
        if i.ItemID == 0x0F0E:
            Items.Move(i, butlerID, 0)
            Misc.Pause(600)
def butler():
    global saveSwitch
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
    # Cure 
    textid = List[int]([14])
    text = List[str]([str(cureImput)])
    saveProfile(textid, text)

    # Agility
    textid = List[int]([15])
    text = List[str]([str(agiImput)])
    saveProfile(textid, text)

    #Strength
    textid = List[int]([16])
    text = List[str]([str(strImput)])
    saveProfile(textid, text)
    
    #Deadlypoison 
    textid = List[int]([17])
    text = List[str]([str(dpImput)])
    saveProfile(textid, text)

    #Heal
    textid = List[int]([19])
    text = List[str]([str(healImput)])
    saveProfile(textid, text)

    #Refresh
    textid = List[int]([18])
    text = List[str]([str(refreshImput)])
    saveProfile(textid, text)
  
    #Explode
    textid = List[int]([20])
    text = List[str]([str(expImput)])
    saveProfile(textid, text)
    
    #################### Bandages ###################################
    textid = List[int]([21])
    text = List[str]([str(bandages21)])
    saveProfile(textid, text)
    
    #################### Petals #####################################
    textid = List[int]([23])
    text = List[str]([str(0)])
    saveProfile(textid, text)
    
    textid = List[int]([25])
    text = List[str]([str(arrows25)])
    saveProfile(textid, text)
    
    #################### Arrows/Bolts ###############################
    textid = List[int]([26])
    text = List[str]([str(bolts26)])
    saveProfile(textid, text)

    Gumps.WaitForGump(989312372, 2000)
    #Gumps.SendAction(989312372, withdrawSwitch)
    Gumps.SendAdvancedAction(989312372, withdrawSwitch, switch)
    
def saveProfile(textid, text):
    if Gumps.CurrentGump() != 989312372:
        tempGump = Gumps.CurrentGump()
        Gumps.CloseGump(tempGump)
        Mobiles.UseMobile(butlerID)
    Gumps.WaitForGump(989312372, 2000)
    Gumps.SendAdvancedAction(989312372, saveSwitch, switch, textid, text)
    Misc.Pause(randomPause)

dumpBottles()
butler()
