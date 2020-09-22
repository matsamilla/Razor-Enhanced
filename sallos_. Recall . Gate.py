# Sallos . recall and . gate commands
# By MatsaMilla, Version 1.2 9/21/20

runebookDelay = 600

if Player.GetRealSkillValue('Magery') > 35:
    mageRecall = True
else:
    mageRecall = False
    Misc.SendMessage('Recalling by Charges')
    
def makeRunebookList( ):
    sortedRuneList = []
    for i in Player.Backpack.Contains:
        if i.ItemID == 0x22C5:
            # opens runebook
            Items.UseItem( i )
            Misc.Pause(120)
            if Journal.Search('You must wait'):
                Misc.SendMessage('trying runebook again')
                Items.UseItem( i )
            Gumps.WaitForGump( 1431013363, 5000 )
            
            bookSerial = i.Serial
            runeNames = []
            lineList = Gumps.LastGumpGetLineList()

            # Remove the default 3 lines from the top of the list
            lineList = lineList[ 3 : ]

            # Remove the items before the names of the runes
            endIndexOfDropAndDefault = 0
            for i in range( 0, len( lineList ) ):
                if lineList[ i ] == 'Set default' or lineList[ i ] == 'Drop rune':
                    endIndexOfDropAndDefault += 1
                else:
                    break

            # Add two for the charge count and max charge numbers
            endIndexOfDropAndDefault += 2
            runeNames = lineList[ endIndexOfDropAndDefault : ( endIndexOfDropAndDefault + 16 ) ]
            runeNames = [ name for name in runeNames if name != 'Empty' ]
            mageRecall = 5
            chargeRecall = 2
            gate = 6
            for x in runeNames:
                sortedRuneList.append( (bookSerial, x.lower(), mageRecall , chargeRecall , gate) )
                mageRecall = mageRecall + 6
                chargeRecall = chargeRecall + 6
                gate = gate + 6
            Gumps.CloseGump(1431013363)
            Misc.Pause(runebookDelay)
    Misc.SendMessage('Runebooks Updated', 66)
    return sortedRuneList

def recall( str ):
    for f in runeNames:
        if str == f[1]:
            Items.UseItem(f[0])
            Gumps.WaitForGump(1431013363, 1000)
            Gumps.SendAction(1431013363, f[2])
            Misc.SendMessage('Recalling to ' + str,11)    
        
def chargeRecall( str ):
    for f in runeNames:
        if str == f[1]:
            Items.UseItem(f[0])
            Gumps.WaitForGump(1431013363, 1000)
            Gumps.SendAction(1431013363, f[3])
            Misc.SendMessage('Recalling to ' + str,11)

            
def gate( str ):
    for f in runeNames:
        if str == f[1]:
            Items.UseItem(f[0])
            Gumps.WaitForGump(1431013363, 1000)
            Gumps.SendAction(1431013363, f[4])
            Misc.SendMessage('Gating ' + str,11)
            
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
        
def parseJournal (str):
    # Fetch the Journal entries (oldest to newest)
    regularText = Journal.GetTextBySerial(Player.Serial)
    
    # Reverse the Journal entries so that we read from newest to oldest
    regularText.Reverse()

    # Read back until the item ID was started to see if it succeeded
    for line in regularText[ 0 : len( regularText ) ]:
        #if line == str:
        if str in line:
            line = line.split(str + ' ', 1)[1]
            Journal.Clear()
            return line

playerSerialCheck = Misc.ReadSharedValue('playerSerial')

runeNames = Misc.ReadSharedValue('runeNames'+str(Player.Serial))
if runeNames == 0:
    Misc.SendMessage('Reading Runebooks, please wait', 33)
    runeNames = makeRunebookList()
    Misc.Pause(500)
    Misc.SetSharedValue('runeNames'+str(Player.Serial), runeNames)
else:
     Misc.SendMessage('Runes Still In Memory', 66)

Journal.Clear()

while True:
    if Journal.SearchByName(". recall", Player.Name):
        if mageRecall and checkRegs():
            recallLocation = parseJournal('. recall')
            recall(recallLocation.lower())
            Misc.NoOperation()
        else:
            recallLocation = parseJournal('. recall')
            chargeRecall(recallLocation.lower())
            Misc.NoOperation()
        Journal.Clear()
    elif Journal.SearchByName(". gate", Player.Name):
        gateLocation = parseJournal('. gate')
        gate(gateLocation.lower())
        Journal.Clear()
    Misc.Pause(50)
