#standard import
import sys

#globals
ingotType = 0x1BF2
tinkerToolsType = 0x1EBC

lockpickType = 0x14FC
heatingstandType = 0x1849
scaleType = 0x1852
spyglassType = 0x14F5
countDropped = 0

skillValue = 'Tinkering'

def getByItemID(itemid, source):
    """find an item id in backpack"""
    for item in Items.FindBySerial(source).Contains:
        if item.ItemID == itemid:
            return item
        else:
            Misc.NoOperation()
            
def countByItemID(itemid):
    # Count the number of items found in backpack by the ItemID
    count = 0
    for item in Player.Backpack.Contains:
        if item.ItemID == itemid:
            count = count + 1
        else:
            Misc.NoOperation()
    Misc.SendMessage('%i items found' % (count))
    return count

def trainTinkering():
    while Player.GetSkillValue(skillValue) < 30:
        Misc.SendMessage('Train tinkering to atleast 30 from a vendor')
        sys.exit()
    while Player.GetSkillValue(skillValue) >= 30 and Player.GetSkillValue(skillValue) < 48:
        if Player.Weight >= Player.MaxWeight:
            dropCrafts()
        if Player.Visible == True:
            hideNotHidden()
        if Gumps.HasGump():
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 0)
        tinkerTools = getByItemID(tinkerToolsType, Player.Backpack.Serial)
        Items.UseItem(tinkerTools)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 29)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 23)
        Gumps.WaitForGump(949095101, 4000)
    while Player.GetSkillValue(skillValue) >= 48 and Player.GetSkillValue(skillValue) < 65:
        if Player.Weight >= Player.MaxWeight:
            dropCrafts()
        if Player.Visible == True:
            hideNotHidden()
        if Gumps.HasGump():
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 0)
        ingots = getByItemID(ingotType, Player.Backpack.Serial)
        if ingots.Amount < 4:
            dropCrafts()
            sys.exit()
        tinkerTools = getByItemID(tinkerToolsType, Player.Backpack.Serial)
        Items.UseItem(tinkerTools)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 121)
        Gumps.WaitForGump(949095101, 4000)
    while Player.GetSkillValue(skillValue) >= 65 and Player.GetSkillValue(skillValue) < 90:
        #This one we want to rotate between lockpick, heating stand, scale, and spyglass
        #Lockpicks
        if Player.Weight >= Player.MaxWeight:
            dropCrafts()
        if Player.Visible == True:
            hideNotHidden()
        if Gumps.HasGump():
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 0)
        ingots = getByItemID(ingotType, Player.Backpack.Serial)
        if ingots.Amount < 4:
            dropCrafts()
            sys.exit()
        tinkerTools = getByItemID(tinkerToolsType, Player.Backpack.Serial)
        if Gumps.HasGump():
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 0)
        Items.UseItem(tinkerTools)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 8)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 121)
        Gumps.WaitForGump(949095101, 4000)
        #Heating Stand
        if Player.Weight >= Player.MaxWeight:
            dropCrafts()
        if Player.Visible == True:
            hideNotHidden()
        if Gumps.HasGump():
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 0)
        ingots = getByItemID(ingotType, Player.Backpack.Serial)
        if ingots.Amount < 4:
            dropCrafts()
            sys.exit()
        tinkerTools = getByItemID(tinkerToolsType, Player.Backpack.Serial)
        Items.UseItem(tinkerTools)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 29)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 51)
        Misc.Pause(2000)
        #Scale
        if Player.Weight >= Player.MaxWeight:
            dropCrafts()
        if Player.Visible == True:
            hideNotHidden()
        if Gumps.HasGump():
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 0)
        ingots = getByItemID(ingotType, Player.Backpack.Serial)
        if ingots.Amount < 4:
            dropCrafts()
            sys.exit()
        tinkerTools = getByItemID(tinkerToolsType, Player.Backpack.Serial)
        Items.UseItem(tinkerTools)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 29)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 16)
        Gumps.WaitForGump(949095101, 4000)
        #Spyglass
        if Player.Weight >= Player.MaxWeight:
            dropCrafts()
        if Player.Visible == True:
            hideNotHidden()
        if Gumps.HasGump():
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 0)
        ingots = getByItemID(ingotType, Player.Backpack.Serial)
        if ingots.Amount < 4:
            dropCrafts()
            sys.exit()
        tinkerTools = getByItemID(tinkerToolsType, Player.Backpack.Serial)
        Items.UseItem(tinkerTools)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 29)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 37)
        Gumps.WaitForGump(949095101, 4000)
    while Player.GetSkillValue(skillValue) >= 90 and Player.GetSkillValue(skillValue) < 100:
        #This one we want to rotate between heating stand, scale, and spyglass
        #Heating Stand
        if Player.Weight >= Player.MaxWeight:
            dropCrafts()
        if Player.Visible == True:
            hideNotHidden()
        if Gumps.HasGump():
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 0)
        ingots = getByItemID(ingotType, Player.Backpack.Serial)
        if ingots.Amount < 4:
            dropCrafts()
            sys.exit()
        tinkerTools = getByItemID(tinkerToolsType, Player.Backpack.Serial)
        Items.UseItem(tinkerTools)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 29)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 51)
        Gumps.WaitForGump(949095101, 4000)
        #Scale
        if Player.Weight >= Player.MaxWeight:
            dropCrafts()
        if Player.Visible == True:
            hideNotHidden()
        if Gumps.HasGump():
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 0)
        ingots = getByItemID(ingotType, Player.Backpack.Serial)
        if ingots.Amount < 4:
            dropCrafts()
            sys.exit()
        tinkerTools = getByItemID(tinkerToolsType, Player.Backpack.Serial)
        Items.UseItem(tinkerTools)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 29)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 16)
        Gumps.WaitForGump(949095101, 4000)
        #Spyglass
        if Player.Weight >= Player.MaxWeight:
            dropCrafts()
        if Player.Visible == True:
            hideNotHidden()
        if Gumps.HasGump():
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 0)
        ingots = getByItemID(ingotType, Player.Backpack.Serial)
        if ingots.Amount < 4:
            dropCrafts()
            sys.exit()
        tinkerTools = getByItemID(tinkerToolsType, Player.Backpack.Serial)
        Items.UseItem(tinkerTools)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 29)
        Gumps.WaitForGump(949095101, 4000)
        Gumps.SendAction(949095101, 37)
        Gumps.WaitForGump(949095101, 4000)
    if Player.GetSkillValue(skillValue) == 100:
        Misc.SendMessage('GM Tinkering!')
        sys.exit
        
    dropCrafts()
        
def dropCrafts():
    # Get Counts
    countLockpick = countByItemID(lockpickType)
    countHeatingstand = countByItemID(heatingstandType)
    countScale = countByItemID(scaleType)
    countSpyglass = countByItemID(spyglassType)
    # Get Dropping
    dropAndMove(countLockpick, lockpickType)
    dropAndMove(countHeatingstand, heatingstandType)
    dropAndMove(countScale, scaleType)
    dropAndMove(countSpyglass, spyglassType)
    
            
def dropAndMove(count, itemType):
    global countDropped
    for i in range(count):
        item = getByItemID(itemType, Player.Backpack.Serial)
        Items.MoveOnGround(item, -1, Player.Position.X - 1, Player.Position.Y, Player.Position.Z)
        countDropped = countDropped + 1
        Misc.Pause(600)
        #if weve dropped up to 18 on one tile, move along
        if countDropped == 20:
            countDropped = 0
            Player.Run('West')
            Player.UseSkill('Hiding')
            
def hideNotHidden():
    while Player.Visible == True:
        Player.UseSkill('Hiding')
        Misc.Pause(6000)
    
trainTinkering()