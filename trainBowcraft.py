import sys

typeBow = 
typeXBow = 
typeHXBow = 
fletchingTool = 
countBowDropped = 0

def getByItemID(itemid):
    # Find an item id in backpack and return the item object
    for item in Player.Backpack.Contains:
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
    
def percentCompletion(numerator, divisor):
    # Display how far along we are with regards to using all boards
    Misc.SendMessage(str(round(numerator / divisor * 100,2)) + '%% Count:%i/%i' % (numerator, divisor))
    
def fletch(bowType):
    # Main fletching logic
    while Player.Weight < 410:
        # Get fletching tools in backpack
        fletching = getByItemID(fletchingTool)
        Items.UseItemByID(fletching.ItemID, 0x0000)
        if bowType = 'bow':
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 15)
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 16)
            Misc.Pause(1000)
            Gumps.WaitForGump(949095101, 10000)
            boardsCurrent = float(boards.Amount)
            percentCompletion(boardsCurrent, boardsTotal)
            if boards.Amount <= 8:
                break
        elif bowType = 'xbow':
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 15)
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 16)
            Misc.Pause(1000)
            Gumps.WaitForGump(949095101, 10000)
            boardsCurrent = float(boards.Amount)
            percentCompletion(boardsCurrent, boardsTotal)
            if boards.Amount <= 9:
                break
        elif bowType = 'hxbow':
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 15)
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 16)
            Misc.Pause(1000)
            Gumps.WaitForGump(949095101, 10000)
            boardsCurrent = float(boards.Amount)
            percentCompletion(boardsCurrent, boardsTotal)
            if boards.Amount <= 10:
                break
        else:
            Misc.NoOperation()
            
def dropAndMoveNorth(bowType):
    if bowType = 'bow':
        count = countByItemID(typeBow)
        for i in range(count):
            item = getByItemID(typeBow)
            Items.MoveOnGround(item, 1, Player.Position.X, Player.Position.Y - 1, Player.Position.Z)
            countBowDropped = countBowDropped + 1
            Misc.Pause(600)
            #if weve dropped up to 18 on one tile, move along
            if countBowDropped == 18:
                countBowDropped = 0
                Player.Run('North')
    elif bowType = 'xbow':
        count = countByItemID(typeXBow)
        for i in range(count):
            item = getByItemID(typeXBow)
            Items.MoveOnGround(item, 1, Player.Position.X, Player.Position.Y - 1, Player.Position.Z)
            countBowDropped = countBowDropped + 1
            Misc.Pause(600)
            #if weve dropped up to 18 on one tile, move along
            if countBowDropped == 18:
                countBowDropped = 0
                Player.Run('North')
    elif bowType = 'hxbow':
        count = countByItemID(typeHXBow)
        for i in range(count):
            item = getByItemID(typeHXBow)
            Items.MoveOnGround(item, 1, Player.Position.X, Player.Position.Y - 1, Player.Position.Z)
            countBowDropped = countBowDropped + 1
            Misc.Pause(600)
            #if weve dropped up to 18 on one tile, move along
            if countBowDropped == 18:
                countBowDropped = 0
                Player.Run('North')

def trainBowcraft():
    countBowDropped = 0
    boards = getByItemID('0x1BD7')
    boardsTotal = float(boards.Amount)
    boardsCurrent = float(boards.Amount)
    # Skill values based on UOForever gains
    # Craft Heavy X-bows from 80-100
    while Player.GetSkillValue('Fletching') < 100 and Player.GetSkillValue('Fletching') >= 80:
        while boards.Amount > 10 : # switch out for board count
            percentCompletion(boardsCurrent, boardsTotal)
            fletch('hxbow')
             # Drop bows to ground since we're overweight
            dropAndMoveNorth('bow')
    # Craft X-bows from 60-80
    while Player.GetSkillValue('Fletching') < 80 and Player.GetSkillValue('Fletching') >= 60:
        while boards.Amount > 10 : # switch out for board count
            percentCompletion(boardsCurrent, boardsTotal)
            fletch('hxbow')
             # Drop bows to ground since we're overweight
            dropAndMoveNorth('xbow')
    # Craft bows from 40-60
    while Player.GetSkillValue('Fletching') < 60 and Player.GetSkillValue('Fletching') >= 40:
        while boards.Amount > 10 : # switch out for board count
            percentCompletion(boardsCurrent, boardsTotal)
            fletch('hxbow')
            # Drop bows to ground since we're overweight
            dropAndMoveNorth('hxbow')
    # Exit macro; tell user to get trained
    while Player.GetSkillValue('Fletching') < 40:
        Misc.SendMessage('Go buy fletching from a trainer up to atleast 40')
        sys.exit
        
    # Upon completion of using all boards, or reaching level 100 drop all remaining bows.
    cleanup = True
    while cleanup:
        dropAndMoveNorth('bow')
        dropAndMoveNorth('xbow')
        dropandMoveNorth('hxbow')
    
trainBowcraft()