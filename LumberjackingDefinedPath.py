import sys
sys.path.append(r'E:\Program Files (x86)\RazorEnhanced\Scripts')

TreeStaticID = [3221, 3222, 3225, 3227, 3228, 3229, 3210, 3238, 3240, 3242, 3243, 3267, 3268, 3272, 3273, 3274, 3275, 3276, 3277, 3280, 3283, 3286, 3288, 3290, 3293, 3296, 3299, 3302, 3320, 3323, 3326, 3329, 3365, 3367, 3381, 3383, 3384, 3394, 3395, 3417, 3440, 3461, 3476, 3478, 3480, 3482, 3484, 3486, 3488, 3490, 3492, 3496]

def getPath():
    """Assign the direction and action"""
    from actionsFile import actions
    return actions
    
def getHatchet():
    """find a hatchet item id in backpack"""
    for hatchet in Player.Backpack.Contains:
        if hatchet.ItemID == int('0x0F43',16):
            return hatchet
        else:
            Misc.NoOperation()
    Misc.SendMessage('No Hatchets Found')

def equipHatchet():
    """Handle equipping of the hatchet"""
    
    #Get hatchet Item Object
    handsOccupied = 'occupied'
    if not Player.GetItemOnLayer('LeftHand') is None:
        handsOccupied = 'occupied'
        hatchet = getHatchet()
    else:
        handsOccupied = 'unoccupied'
        hatchet = getHatchet()
    
    #Check lefthand for occupancy
    #   and equip or unequip-equip accordingly
    if handsOccupied == 'unoccupied':
        Player.EquipItem(hatchet)
        Misc.Pause(500)
    elif handsOccupied == 'occupied':
        Player.UnEquipItemByLayer('LeftHand')
        Misc.Pause(1000)
        Player.EquipItem(hatchet)
        Misc.Pause(600)
    else:
        Misc.SendMessage('Hands Check gone awry.')
        
    return hatchet
    
def analyzeTileForTree():
    """Get player position and direction. Check for graphic in front for targetting"""
    playerPos = Player.Position
    playerX = Player.Position.X
    playerY = Player.Position.Y
    playerZ = Player.Position.Z
    direction = Player.Direction

    if direction == 'Up':
        tileX = playerX - 1
        tileY = playerY - 1
        tileZ = playerZ
    elif direction == 'North':
        tileX = playerX
        tileY = playerY - 1
        tileZ = playerZ
    elif direction == 'Right':
        tileX = playerX + 1
        tileY = playerY - 1
        tileZ = playerZ
    elif direction == 'East':
        tileX = playerX + 1
        tileY = playerY
        tileZ = playerZ
    elif direction == 'Down':
        tileX = playerX + 1
        tileY = playerY + 1
        tileZ = playerZ
    elif direction == 'South':
        tileX = playerX
        tileY = playerY + 1
        tileZ = playerZ
    elif direction == 'Left':
        tileX = playerX - 1
        tileY = playerY + 1
        tileZ = playerZ
    elif direction == 'West':
        tileX = playerX - 1
        tileY = playerY
        tileZ = playerZ
        
    Misc.SendMessage('Tile: (X:%i, Y:%i, Z:%i, Facing:%s)' % (tileX, tileY, tileZ, direction))
        
    tileinfo = Statics.GetStaticsTileInfo(tileX, tileY, Player.Map)
    if tileinfo.Count > 0:
        for tile in tileinfo:
            if tile.StaticID in TreeStaticID:
                Misc.SendMessage('Tree (X: %i, Y: %i, Z: %i, ID: %s)' % (tileX, tileY, tile.StaticZ, tile.StaticID), 66)
                return tileX, tileY, tile.StaticZ, tile.StaticID, True
            else:
                Misc.SendMessage('No Tree')
                return None, None, None, None, False
    else:
        Misc.NoOperation()
    
def ChopChopChop():
    """handle the lumberjacking"""
    Misc.SendMessage('entered ChopChopChop')
    
    #Validate Hatchet is equipped. If not, equip hatchet.
    hatchet = equipHatchet()
    
    #Iterate for 6 times, use a rand-between
    Misc.Pause(600)
    for iter in range(0, 6):
        # Get the XYZ and GFX infront of where youre facing.
        x, y, z, gfx, tree = analyzeTileForTree()
        
        #Use equipped Items
        if tree:
            Items.UseItem(hatchet)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(x, y, z, gfx)
            Misc.Pause(4000)
        else:
            break
            
def moveHandler(path):
    """handle all movement actions"""
    Misc.SendMessage(path[0] + ',' + path[1])
    moved = False
    while not moved:
        moved = Player.Run(path[0])
        Misc.Pause(200)
    

def Pathing():
    """Main pathing handler"""
    #Get the path list
    Paths = getPath()
    
    #Iterate through path list and make decisions!
    for path in Paths:
        if path[1] == 'PlayMacro':
            ChopChopChop()
        elif path[1] == 'move':
            moveHandler(path)

Pathing()
