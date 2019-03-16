# Treasure Map Puller by MatsaMilla
# SHOULD pull gold first and palce in beetle
# keeps recalls, gate & lvl 8 summoning scrolls no matter what
# you will have to re-assign bags every time you close Razor... fault of the program.

dragTime = 1000
msgColor = 68
self = Mobiles.FindBySerial(Player.Serial)

# *** Replace with beetle serial if you have one *** 
beetle = 0x0006EB2A

# *** False if you don not have beetle *** 
beetleBag = True

# True if you want to keep scrolls
sortScrolls = False

#check for reg bag
if Misc.CheckSharedValue('regBag'):
    regBag = Misc.ReadSharedValue('regBag')
    if Items.FindBySerial(regBag):
        Misc.NoOperation()
    else:
        regBag = Target.PromptTarget('Select Bag for Regs')
        Misc.SetSharedValue('regBag', regBag)
else:
    regBag = Target.PromptTarget('Select Bag for Regs')
    Misc.SetSharedValue('regBag', regBag)
#check for wep bag
if Misc.CheckSharedValue('wepBag'):
    wepBag = Misc.ReadSharedValue('wepBag')
    if Items.FindBySerial(wepBag):
        Misc.NoOperation()
    else:
        wepBag = Target.PromptTarget('Select Bag for Weapons')
        Misc.SetSharedValue('wepBag', wepBag)
else:
    wepBag = Target.PromptTarget('Select Bag for Weapons')
    Misc.SetSharedValue('wepBag', wepBag)
#check for armor bag    
if Misc.CheckSharedValue('armorBag'):
    armorBag = Misc.ReadSharedValue('armorBag')
    if Items.FindBySerial(armorBag):
        Misc.NoOperation()
    else:
        armorBag = Target.PromptTarget('Select Bag for Armor')
        Misc.SetSharedValue('armorBag', armorBag)
else:
    armorBag = Target.PromptTarget('Select Bag for Armor')
    Misc.SetSharedValue('armorBag', armorBag)
#check for gem bag    
if Misc.CheckSharedValue('gemBag'):
    gemBag = Misc.ReadSharedValue('gemBag')
    if Items.FindBySerial(gemBag):
        Misc.NoOperation()
    else:
        gemBag = Target.PromptTarget('Select Bag for Gems')
        Misc.SetSharedValue('gemBag', gemBag)
else:
    gemBag = Target.PromptTarget('Select Bag for Gems')
    Misc.SetSharedValue('gemBag', gemBag)
#check for scroll bag
if sortScrolls:
    if Misc.CheckSharedValue('scrollBag'):
        scrollBag = Misc.ReadSharedValue('scrollBag')
        if Items.FindBySerial(scrollBag):
            Misc.NoOperation()
        else:
            scrollBag = Target.PromptTarget('Select Bag for Scrolls')
            Misc.SetSharedValue('scrollBag', scrollBag)
    else:
        scrollBag = Target.PromptTarget('Select Bag for Scrolls')
        Misc.SetSharedValue('scrollBag', scrollBag)
#check for corpse bag    
if Misc.CheckSharedValue('trashCan'):
    trashCan = Misc.ReadSharedValue('trashCan')
    if Items.FindBySerial(trashCan):
        Misc.NoOperation()
    else:
        trashCan = Target.PromptTarget('Select Corpse to dump on')
        Misc.SetSharedValue('trashCan', trashCan)
else:
    trashCan = Target.PromptTarget('Select Corpse to dump on')
    Misc.SetSharedValue('trashCan', trashCan)
#trashCan = Target.PromptTarget('Select Corpse to dump on')
chest = Target.PromptTarget('Select Treasure Chest')



#loot includes gate, recall & lvl 8 summoning scrolls
loot = [0x2260,0x1f4c,0x1f60,0x1f66,0x1f68,0x1f69,0x1f6a,0x1f6b,0x1f6c]

gold = [0xeed]
gems = [0xf16,0xf15,0xf19,0xf25,0xf21,0xf10,0xf26,0xf2d,0xf13]
wands = [0xdf5,0xdf3,0xdf4,0xdf2]
boneArmor = [0x1450,0x1f0b,0x1452,0x144f,0x1451,0x144e]
regs= [0xf7a,0xf7b,0xf86,0xf84,0xf85,0xf88,0xf8d,0xf8c]

weps = [0xf62,0x1403,0xe87,0x1405,0x1401,0xf52,0x13b0,0xdf0,0x1439,0x1407,0xe89,0x143d,0x13b4,0xe81,0x13f8,
0xf5c,0x143b,0x13b9,0xf61,0x1441,0x13b6,0xec4,0x13f6,0xf5e,0x13ff,0xec3,0xf43,0xf45,0xf4d,0xf4b,0x143e,
0x13fb,0x1443,0xf47,0xf49,0xe85,0xe86,0x13fd,0xf50,0x13b2,]

armor = [0x1b72,0x1b73,0x1b7b,0x1b74,0x1b79,0x1b7a,0x1b76,0x1408,0x1410,0x1411,0x1412,0x1413,0x1414,0x1415,
0x140a,0x140c,0x140e,0x13bb,0x13be,0x13bf,0x13ee,0x13eb,0x13ec,0x13f0,0x13da,0x13db,0x13d5,0x13d6,0x13dc,
0x13c6,0x13cd,0x13cc,0x13cb,0x13c7,0x1db9,0x1c04,0x1c0c,0x1c02,0x1c00,0x1c08,0x1c06,0x1c0a,]

scrolls = [0x1f2d,0x1f2e,0x1f2f,0x1f30,0x1f31,0x1f32,0x1f33,0x1f34,0x1f35,0x1f36,0x1f37,0x1f38,0x1f39,
0x1f3a,0x1f3b,0x1f3c,0x1f3d,0x1f3e,0x1f3f,0x1f40,0x1f41,0x1f42,0x1f43,0x1f44,0x1f45,0x1f46,0x1f47,0x1f48,
0x1f49,0x1f4a,0x1f4b,0x1f4d,0x1f4e,0x1f4f,0x1f50,0x1f51,0x1f52,0x1f53,0x1f54,0x1f55,0x1f56,0x1f57,0x1f58,
0x1f59,0x1f5a,0x1f5b,0x1f5c,0x1f5d,0x1f5e,0x1f5f,0x1f60,0x1f61,0x1f62,0x1f63,0x1f64,0x1f65,0x1f66,0x1f67,
0x1f68,0x1f69,0x1f6a,0x1f6b,0x1f6c]

trash = [0x171c,0x1717,0x1718,0x1544,0x1540,0x1713,0x1715,0x1714,0x1716,0x1717,0x1718,0x1719,0x171a,0x171b,
0x171c,0x2306,0x13f6,0xec4,0x1716,0x171c,0xe81,0xe86,]

mapChest = Items.FindBySerial(chest)
Items.UseItem(mapChest)
Misc.Pause(dragTime)
#Items.WaitForContents(mapChest, 50)
Misc.Pause(dragTime)

def checkDistance():
    #Timer.Create('Distance', 5000)
    while mapChest.DistanceTo(self) > 2:
        Misc.NoOperation()
        if not Timer.Check('Distance'):
            Player.HeadMessage(msgColor, 'Too Far Away')
            Timer.Create('Distance', 2500)


def checkWeight():
    if Player.Weight >= Player.MaxWeight:
        Player.ChatSay(msgColor, 'I am Overweight, stopping')
        Stop            
            
#moves gold to beetle
if beetleBag:
    for s in mapChest.Contains:
        checkDistance()
        if s.ItemID in gold:
            if Player.Mount:
                Mobiles.UseMobile(Player.Serial)
                Misc.Pause(dragTime)
            Items.Move(s, beetle, 0)
            Misc.Pause(dragTime)
            if not Player.Mount:
                Mobiles.UseMobile(beetle)
                Misc.Pause(dragTime)

for e in mapChest.Contains :
    checkDistance()
    checkWeight()
    if e.ItemID in gold:
        Items.Move(e, Player.Backpack.Serial, 0)
        Misc.Pause(dragTime)
    elif e.ItemID in gems:
        Items.Move(e, gemBag, 0)
        Misc.Pause(dragTime)
                
for i in mapChest.Contains :
    checkDistance()
    checkWeight()
    if i.ItemID in loot:
        Items.Move(i, Player.Backpack.Serial, 0)
        Misc.Pause(dragTime)
    elif i.ItemID in boneArmor:
        Items.Move(i, armorBag, 0)
        Misc.Pause(dragTime)
    elif i.ItemID in regs:
        Items.Move(i, regBag, 0)
        Misc.Pause(dragTime)
    elif i.ItemID in weps:
        Items.Move(i, wepBag, 0)
        Misc.Pause(dragTime)
    elif i.ItemID in armor:
        Items.Move(i, armorBag, 0)
        Misc.Pause(dragTime)
    elif i.ItemID in wands:
        Items.Move(i, Player.Backpack.Serial, 0)
        Misc.Pause(dragTime)
    elif sortScrolls:
        if i.ItemID in scrolls:
            Items.Move(i, scrollBag, 0)
            Misc.Pause(dragTime)
#    elif i.ItemID in trash:
#        Items.Move(i, trashCan, 0)
#        Misc.Pause(dragTime)

for t in mapChest.Contains :
    checkDistance()
    checkWeight()
    if t.ItemID in scrolls:
        Items.Move(t, trashCan, 0)
        Misc.Pause(dragTime)
    elif t.ItemID in trash:
        Items.Move(t, trashCan, 0)
        Misc.Pause(dragTime)
        
Player.HeadMessage(msgColor, 'All Done')        