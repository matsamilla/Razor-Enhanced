#Make Last Blacksmithing

craftType = 0x1413
craftToolType = 0x13E3

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

def trainBlacksmith():
    while Player.GetSkillValue('Blacksmith') < 105:
        if Player.Visible:
            Player.UseSkill('Hiding')
        bsTool = getByItemID(craftToolType, Player.Backpack.Serial)
        Items.UseItem(bsTool)
        Gumps.WaitForGump(949095101, 2500)
        Gumps.SendAction(949095101, 21)
        
        if Player.Weight > Player.MaxWeight:
            craftTypeCount = countByItemID(craftType)
            while craftTypeCount != 0:
                bsTool = getByItemID(craftToolType, Player.Backpack.Serial)
                gorget = getByItemID(craftType, Player.Backpack.Serial)
                
                Items.UseItem(bsTool)
                Misc.Pause(600)
                Gumps.WaitForGump(949095101, 10000)
                Gumps.SendAction(949095101, 14)
                Target.WaitForTarget(10000, False)
                Target.TargetExecute(gorget)
                Misc.Pause(600)
                craftTypeCount = countByItemID(craftType)
            
    
trainBlacksmith()


