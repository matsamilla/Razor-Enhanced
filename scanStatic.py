RaggioScansione = 15
TreeStaticID = [3221, 3222, 3225, 3227, 3228, 3229, 3210, 3238, 3240, 3242, 3243, 3267, 3268, 3272, 3273, 3274, 3275, 3276, 3277, 3280, 3283, 3286, 3288, 3290, 3293, 3296, 3299, 3302, 3320, 3323, 3326, 3329, 3365, 3367, 3381, 3383, 3384, 3394, 3395, 3417, 3440, 3461, 3476, 3478, 3480, 3482, 3484, 3486, 3488, 3490, 3492, 3496]



# Variabili Sistema
from System.Collections.Generic import List
tileinfo = List[Statics.TileInfo]
treeposx = []
treeposy = []
treeposz = []
treegfx = []
treenumber = 0
blockcount = 0
lastrune = 5
onloop = True

def ScanStatic( ): 
    global treenumber
    Misc.SendMessage("--> Inizio Scansione Tile", 77)
    minx = Player.Position.X - RaggioScansione
    maxx = Player.Position.X + RaggioScansione
    miny = Player.Position.Y - RaggioScansione
    maxy = Player.Position.Y + RaggioScansione

    while miny <= maxy:
        while minx <= maxx:
            tileinfo = Statics.GetStaticsTileInfo(minx, miny, Player.Map)
            if tileinfo.Count > 0:
                for tile in tileinfo:
                    for staticid in TreeStaticID:
                        if staticid == tile.StaticID:
                            Misc.SendMessage('--> Albero X: %i - Y: %i - Z: %i' % (minx, miny, tile.StaticZ), 66)
                            treeposx.Add(minx)
                            treeposy.Add(miny)
                            treeposz.Add(tile.StaticZ)
                            treegfx.Add(tile.StaticID)
            else:
                Misc.NoOperation()
            minx = minx + 1
        minx = Player.Position.X - RaggioScansione            
        miny = miny + 1
    treenumber = treeposx.Count    
    Misc.SendMessage('--> Totale Alberi: %i' % (treenumber), 77)
    
ScanStatic()