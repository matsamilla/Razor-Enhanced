# ID Wand by MatsaMilla
# equips and uses Greater Heal wand, then unequips after

#[equip idwand


wandType = "identification"
wands = [0xdf5,0xdf3,0xdf4,0xdf2]
msgColor = 33
dragTime = 600
import sys

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
        charges = Items.GetPropValue(wand,"Charges")
        
        if any( wandType in s for s in propList ):
            Player.HeadMessage(78,"{} charges".format(int(charges)))
            #Misc.SendMessage(wandType + " found")
            
            Player.EquipItem( wand )
            Misc.Pause( dragTime )
            Items.UseItem( wand )
            Target.WaitForTarget( 2500 )
            while Target.HasTarget():
                Misc.Pause( 50 )
            Misc.Pause( dragTime )
            Player.UnEquipItemByLayer('RightHand')
            sys.exit()
                
    Player.HeadMessage( msgColor, "No wands found!" )
    
def checkHands(wandType):
    leftHand = Player.GetItemOnLayer('LeftHand')
    rightHand = Player.GetItemOnLayer('RightHand')
    if leftHand:
        Misc.SendMessage('lefthand')
        Player.UnEquipItemByLayer('LeftHand')
        Misc.Pause( dragTime )
        return False
    if rightHand:
        if rightHand.ItemID in wands:
            Items.WaitForProps(rightHand,500)
            propList = Items.GetPropStringList( rightHand )
            charges = Items.GetPropValue(rightHand,"Charges")
            if any( wandType in s for s in propList ):
                Player.HeadMessage(78,"{} charges".format(int(charges)))
                Items.UseItem( rightHand )
                Target.WaitForTarget( 2500 )
                while Target.HasTarget():
                    Misc.Pause( 50 )
                Misc.Pause( dragTime )
                Player.UnEquipItemByLayer('RightHand')
                return True
        else:
            Player.UnEquipItemByLayer('RightHand')
            Misc.Pause( dragTime )
            return False
        

if checkHands(wandType):
    Misc.NoOperation()
else:
    findAndEquipWand (wandType)
