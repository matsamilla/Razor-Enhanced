# Sort selected runebook alphabetically
# By MatsaMilla
# must have ToolTips enabled
# don't have any other runes in back, bag them before starting

runebook = Items.FindBySerial(Target.PromptTarget('target book'))
runelist = []

def GetNamesOfRunesInBook( runebook ):
    Items.UseItem( runebook )

    # Pause here since the next part goes pretty quick
    Misc.Pause( 600 )

    Gumps.WaitForGump( 1431013363, 5000 )
    while Gumps.CurrentGump() != 1431013363:
        Player.HeadMessage( 33, 'Too far from runebook to copy, please move closer.' )
        Misc.Pause( 1000 )
        Items.UseItem( runebook )
        Gumps.WaitForGump( 1431013363, 5000 )

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

    return runeNames
    
def GetNumberOfRunesInBook( runebook ):
    return len( GetNamesOfRunesInBook( runebook ) )

def dropRunes():
    numberOfRunesInBook = GetNumberOfRunesInBook( runebook ) +1
    Items.UseItem(runebook)
    for i in range( 0 , numberOfRunesInBook):
        # drop runebook runes
        #Items.UseItem(runebook)
        Gumps.WaitForGump(1431013363, 1000)
        Gumps.SendAction(1431013363, 3)
        Misc.Pause(600)
    
    Gumps.WaitForGump(1431013363, 1000)
    Gumps.SendAction(1431013363, 0)
    
def getSortKey(list):
    return list[0]
    
def compileRunes():
    for i in Player.Backpack.Contains:
        if i.ItemID == 0x1F14:
            Items.WaitForProps(i, 1000)
            runeName = Items.GetPropStringByIndex(i, 0)
            if runeName:
                #Misc.SendMessage(runeName)
                runelist.append((runeName,i.Serial))
        #Misc.Pause(200)
    #Misc.SendMessage('____', 33)
    runelist.sort(key=getSortKey)
    
    for l in runelist:
        Items.Move(l[1], runebook.Serial, 0)
        #Misc.SendMessage(l[0])
        Misc.Pause(600)

dropRunes()       
compileRunes()
