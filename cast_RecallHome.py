# Recall Home by MatsaMilla
# version 2.1 - overhead message for using charges, and remaining charges
#
# Enter in player name (case sensitive!), runebook and runeNumber (posotion of rune in book, 1-16)

# True = Mage will not open book, home rune set to default
targetBook = True

if Player.Name == "MetaMilla":
    runebook = 0x43286FAE
    runeNumber = 1
    
elif Player.Name == "MGD":
    runebook = 0x402F6431
    runeNumber = 1
    
elif Player.Name == "UhOh":
    runebook = 0x40c0aa9a
    runeNumber = 2
    
elif Player.Name == "EmGD":
    runebook = 0x42FAD098
    runeNumber = 11
    
elif Player.Name == "Mirunn":
    runebook = 0x4701FFAE
    runeNumber = 1
    
elif Player.Name == "Nalfein":
    runebook = 0x423A667B
    runeNumber = 1
    
elif Player.Name == "MGDexxer":
    runebook = 0x423AE870
    runeNumber = 1
    
elif Player.Name == "Vierna DoUrden":
    runebook = 0x423AE2DE
    runeNumber = 1
    
elif Player.Name == "Thicc":
    runebook = 0x411AC13E
    runeNumber = 1
    
elif Player.Name == "UselessGuy":
    runebook = 0x40E104BB
    runeNumber = 2
    
elif Player.Name == "MatsaMilla":
    runebook = 0x41DB0F60
    runeNumber = 1
    
elif Player.Name == "Matsa":
    runebook = 0x423949E3
    runeNumber = 1
    
elif Player.Name == "Matsa-":
    runebook = 0x40788ED9
    runeNumber = 1
    
elif Player.Name == "MatsaAxa":
    runebook = 0x411C1DCD
    runeNumber = 1
    
elif Player.Name == "Poinsettia":
    runebook = 0x4114C90D
    runeNumber = 1
    
elif Player.Name == "MatsaMaga":
    runebook = 0x42106027
    runeNumber = 6
    
elif Player.Name == "Hydragea":
    runebook = 0x4239C87F
    runeNumber = 1
    
#***************************************************************#
    
def recallMagery(book, rune):
    if targetBook:
        Spells.CastMagery('Recall')
        Target.WaitForTarget(1500,False)
        Target.TargetExecute(book)
        
    else:
        rune = rune -1
        rune = 5 + (6 * rune)
        if Gumps.CurrentGump() != 1431013363:
            Items.UseItem(book)
        Gumps.WaitForGump(1431013363, 1000)
        Gumps.SendAction(1431013363, rune)
    
def recallCharge(book, rune):
    rune = rune -1
    rune = 2 + (6 * rune)
    if Gumps.CurrentGump() != 1431013363:
        Items.UseItem(book)
        Misc.Pause(100)
    Gumps.WaitForGump(1431013363, 1000)
    Gumps.SendAction(1431013363, rune)
    Items.WaitForProps(book,500)
    charges = Items.GetPropValue(book,'Charges')
    Player.HeadMessage(66, str(int(charges)) + ' charges left' )
    
def FindItem( itemID, container, color = -1, ignoreContainer = [] ):
    '''
    Searches through the container for the item IDs specified and returns the first one found
    Also searches through any subcontainers, which Misc.FindByID() does not
    '''

    ignoreColor = False
    if color == -1:
        ignoreColor = True

    if isinstance( itemID, int ):
        foundItem = next( ( item for item in container.Contains if ( item.ItemID == itemID and ( ignoreColor or item.Hue == color ) ) ), None )
    elif isinstance( itemID, list ):
        foundItem = next( ( item for item in container.Contains if ( item.ItemID in itemID and ( ignoreColor or item.Hue == color ) ) ), None )
    else:
        raise ValueError( 'Unknown argument type for itemID passed to FindItem().', itemID, container )

    if foundItem != None:
        return foundItem

    subcontainers = [ item for item in container.Contains if ( item.IsContainer and not item.Serial in ignoreContainer ) ]
    for subcontainer in subcontainers:
        foundItem = FindItem( itemID, subcontainer, color, ignoreContainer )
        if foundItem != None:
            return foundItem
            
def checkRegs():
    if (FindItem(0x0F7A , Player.Backpack) and FindItem(0x0F86 , Player.Backpack) and FindItem(0x0F7B , Player.Backpack) ):
        return True
    else:
        return False

    
if runebook != None:
    if Player.GetRealSkillValue('Magery') > 50 and checkRegs():
        recallMagery(runebook, runeNumber)
    else:
        Player.HeadMessage(66,"-Using Charge-")
        recallCharge(runebook, runeNumber)
else:
    Player.HeadMessage(33,'No Runebook Set')
