TreeStaticID = [3221, 3222, 3225, 3227, 3228, 3229, 3210, 3238, 3240, 3242, 3243, 3267, 3268, 3272, 3273, 3274, 3275, 3276, 3277, 3280, 3283, 3286, 3288, 3290, 3293, 3296, 3299, 3302, 3320, 3323, 3326, 3329, 3365, 3367, 3381, 3383, 3384, 3394, 3395, 3417, 3440, 3461, 3476, 3478, 3480, 3482, 3484, 3486, 3488, 3490, 3492, 3496]

def cutInfront():
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
                Misc.SendMessage('Cutting Tree (X: %i, Y: %i, Z: %i, ID: %s)' % (tileX, tileY, tile.StaticZ, tile.StaticID), 66)
            else:
                Misc.SendMessage('No Tree')
    else:
        Misc.NoOperation()
        
cutInfront()