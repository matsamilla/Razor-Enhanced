wands = [0xdf5,0xdf3,0xdf4,0xdf2]
wandType = "lightning"
msgColor = 33
dragTime = 600

def getWands( itemID , container = Player.Backpack  ):
    '''
    Recursively looks through backpack for any wands in the wands list
    Returns a list with wand serials
    '''
    
    # Create the list
    wandList = []
    
    if isinstance( itemID, int ):

        # add wand serials to list
        for item in container.Contains:
            if item.ItemID == itemID:
                wandList.append(item.Serial)

    elif isinstance( itemID, list ):
        # add wand serials to list
        for item in container.Contains:
            if item.ItemID in itemID:
                wandList.append(item.Serial)
    else:
        raise ValueError( 'Unknown argument type for itemID passed to FindItem().', itemID, container )

    subcontainers = [ item for item in container.Contains if item.IsContainer ]

    # Iterate through each item in the given list
    for subcontainer in subcontainers:
        wandsInSubContainer = getWands( itemID, subcontainer )
        for i in wandsInSubContainer:
            wandList.append(i)

    return wandList
    
def findAndEquipWand (wandType):
    wandsInPack = getWands( wands )
    for i in wandsInPack:
        wand = Items.FindBySerial(i)
        Items.WaitForProps( wand, 500 )
        propList = Items.GetPropStringList( wand )
        
        if any( wandType in s for s in propList ):
            #Misc.SendMessage(wandType + " found")
            if Player.CheckLayer('LeftHand'):
                Player.UnEquipItemByLayer('LeftHand')
                Misc.Pause( dragTime )
            elif Player.CheckLayer('RightHand'):
                Player.UnEquipItemByLayer('RightHand')
                Misc.Pause( dragTime )
            Player.EquipItem( wand )
            Misc.Pause( dragTime )
            Items.UseItem( wand )
                
    Player.HeadMessage( msgColor, "No wands found!" )
    
findAndEquipWand (wandType)
