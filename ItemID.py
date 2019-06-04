# Item ID by MatsaMilla
Misc.SendMessage('Starting ItemID', 33)
skillTimer = 0
dragTime = 600
msgColor = 45

# Serial of your trash can
trashCan = 0x43595297

sellBag = Target.PromptTarget('Select Sell to NPC Bag')
keepBag = Target.PromptTarget('Select Good Stuff Bag')
idStuff = Target.PromptTarget('Select container to ID stuff in')

slashProps = ['Invulnerability','Exceptional','Power']
subSlashProps = ['Indestructable','Supremely Accurate','Exceedingly Accurate','Eminently Accurate']
keepProps = ['Vanquishing','Silver','Undead','Snake','Lizardman','Dragon','Reptile','Terathan','Scorpion',
'Spider','Orc Slaying','Ogre','Water','Earth','Elemental','Flame','Vacuum','Repond','Fey','Gargoyle',
'Daemon','Exorcism','Poison']

idItems = [0x1b72,0x1b73,0x1b7b,0x1b74,0x1b79,0x1b7a,0x1b76,0x1408,0x1410,0x1411,0x1412,0x1413,0x1414,0x1415,
0x140a,0x140c,0x140e,0x13bb,0x13be,0x13bf,0x13ee,0x13eb,0x13ec,0x13f0,0x13da,0x13db,0x13d5,0x13d6,0x13dc,
0x13c6,0x13cd,0x13cc,0x13cb,0x13c7,0x1db9,0x1c04,0x1c0c,0x1c02,0x1c00,0x1c08,0x1c06,0x1c0a,0xf62,0x1403,0xe87,0x1405,0x1401,0xf52,0x13b0,0xdf0,0x1439,0x1407,0xe89,
0x143d,0x13b4,0xe81,0x13f8,0xf5c,0x143b,0x13b9,0xf61,0x1441,0x13b6,0xec4,0x13f6,0xf5e,0x13ff,0xec3,0xf43,
0xf45,0xf4d,0xf4b,0x143e,0x13fb,0x1443,0xf47,0xf49,0xe85,0xe86,0x13fd,0xf50,0x13b2,]

#armor = [0x1b72,0x1b73,0x1b7b,0x1b74,0x1b79,0x1b7a,0x1b76,0x1408,0x1410,0x1411,0x1412,0x1413,0x1414,0x1415,0x140a,0x140c,0x140e,0x13bb,0x13be,0x13bf,0x13ee,0x13eb,0x13ec,0x13f0,0x13da,0x13db,0x13d5,0x13d6,0x13dc,0x13c6,0x13cd,0x13cc,0x13cb,0x13c7,0x1db9,0x1c04,0x1c0c,0x1c02,0x1c00,0x1c08,0x1c06,0x1c0a]
boneArmor = [0x1450,0x1f0b,0x1452,0x144f,0x1451,0x144e]
#weps = [0xf62,0x1403,0xe87,0x1405,0x1401,0xf52,0x13b0,0xdf0,0x1439,0x1407,0xe89,0x143d,0x13b4,0xe81,0x13f8,0xf5c,0x143b,0x13b9,0xf61,0x1441,0x13b6,0xec4,0x13f6,0xf5e,0x13ff,0xec3,0xf43,0xf45,0xf4d,0xf4b,0x143e,0x13fb,0x1443,0xf47,0xf49,0xe85,0xe86,0x13fd,0xf50,0x13b2,]


idContainer = Items.FindBySerial(idStuff)
Items.UseItem(idContainer)
Misc.Pause(dragTime)
Items.UseItem(keepBag)
Misc.Pause(dragTime)
Items.UseItem(sellBag)
Misc.Pause(dragTime)
Items.WaitForContents(idContainer, 50)
Misc.Pause(50)

def checkWeight():
    if Player.Weight >= Player.MaxWeight:
        Player.HeadMessage(msgColor, 'Go Sell this shit')
        Stop

for i in idContainer.Contains:
    if i.ItemID in idItems:
        checkWeight()
        Journal.Clear()
        Player.UseSkill('Item ID')
        Target.WaitForTarget(1500)
        Target.TargetExecute(i.Serial)
        Misc.Pause(dragTime)
        Items.SingleClick(i)
        if any(Journal.Search(keep) for keep in keepProps):
            #** Good Stuff Move **
            Items.Move(i, keepBag, 0)
            Misc.Pause(dragTime)
        elif any(Journal.Search(slash) for slash in slashProps):
            if any(Journal.Search(sub) for sub in subSlashProps):
                #** Good Stuff Move **
                Items.Move(i, keepBag, 0)
                Misc.Pause(dragTime)
            else:
                #** Sell Stuff Move **
                Items.Move(i, sellBag, 0)
                Misc.Pause(dragTime)
        else:
            #** Sell Stuff Move **
            Items.Move(i, sellBag, 0)
            Misc.Pause(dragTime)
            #Player.HeadMessage(msgColor, 'Meh')
        #Misc.Pause(skillTimer)
    elif i.ItemID in boneArmor:
        checkWeight()
        Journal.Clear()
        Player.UseSkill('Item ID')
        Target.WaitForTarget(1500)
        Target.TargetExecute(i.Serial)
        Misc.Pause(dragTime)
        Items.SingleClick(i)
        if any(Journal.Search(keep) for keep in keepProps):
            #** Good Stuff Move **
            Items.Move(i, keepBag, 0)
            Misc.Pause(dragTime)
        elif any(Journal.Search(slash) for slash in slashProps):
            if any(Journal.Search(sub) for sub in subSlashProps):
                #** Good Stuff Move **
                Items.Move(i, keepBag, 0)
                Misc.Pause(dragTime)
            else:
                #** Sell Stuff Move **
                Items.Move(i, trashCan, 0)
                Misc.Pause(dragTime)
        else:
            #** Sell Stuff Move **
            Items.Move(i, trashCan, 0)
            Misc.Pause(dragTime)
Player.HeadMessage(msgColor, 'Chest Cleared')
