def getByItemID(itemid):
    """find an item id in backpack"""
    for item in Player.Backpack.Contains:
        if item.ItemID == int(itemid,16):
            return item
        else:
            Misc.NoOperation()
    Misc.SendMessage('No item found: ' + itemid)

def equipBowInPack():
    #Get hatchet Item Object
    handsOccupied = 'occupied'
    if not Player.GetItemOnLayer('LeftHand') is None:
        handsOccupied = 'occupied'
        bow = getByItemID('0x13B2')
    else:
        handsOccupied = 'unoccupied'
        bow = getByItemID('0x13B2')
    
    #Check lefthand for occupancy
    #   and equip or unequip-equip accordingly
    if handsOccupied == 'unoccupied':
        Player.EquipItem(bow)
        Misc.Pause(500)
    elif handsOccupied == 'occupied':
        Player.UnEquipItemByLayer('LeftHand')
        Misc.Pause(1000)
        Player.EquipItem(bow)
        Misc.Pause(600)
    else:
        Misc.SendMessage('Hands Check gone awry.')
    

equipBowInPack()