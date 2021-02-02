# XP tracker by SilentNox, imporoved by MatsaMilla
#   Version 2.6: Fixed error with rogue while using tooltips
    
# Tracks XP of talisman, or meta pet, just start it up 
# and leave talisman / meta stone gump open

# Displays XP gained every 10 seconds, total every 60s & grand total

# true if using tooltips (works better)
toolTipsOn = True

# True = will track XP only while running the script
# False = will track XP since Enhanced, if you stop/restart script it will still track starting xp
trackOnScript = False

# put name in here if you never want to track (maxxed talismans) and will only open tali gump
noTrackList = ['mgdexxer', 'viernadourden', 'metamilla']

    
minxp = 0
currentxp = 0
counter = 0
name = Player.Name.lower().replace(' ', '')

def setupToolTips():
    global startingxp
    global temp
    global currentxp
    temp = Items.GetPropStringByIndex(Talli, propLine)
    if temp == 'MAX':
        Misc.SendMessage('Talisman Maxxed, stopping', 33)
        Stop
    else:
        temp = temp.split(": ", 1)[1]
        temp = temp.split("/", 1)[0]
    
    if hasInt(temp):
        currentxp = int(temp)
    else:
        setup()
        
    if trackOnScript:
        startingxp = currentxp
        Misc.SendMessage('Starting XP: ' + startingxp, 33)
    else:
        if Misc.CheckSharedValue( pname + 'xp' ):
            startingxp = Misc.ReadSharedValue( pname + 'xp' )
            Misc.SendMessage('Starting XP: ' + str(startingxp) , 33)
            Misc.Pause(200)
            gainedXP = currentxp - startingxp
            if gainedXP > 0:
                Player.HeadMessage(66,'XP since run: ' + str(gainedXP))
            elif gainedXP == 0:
                Misc.NoOperation()
            else:
                Player.HeadMessage(44, 'You leveled up!' )
                Player.ChatSay(66, '[e woohoo')
                Misc.RemoveSharedValue( pname + 'xp' )
                setup() 
        else:
            startingxp = currentxp
            Misc.SetSharedValue( pname + 'xp', startingxp )
            Misc.SendMessage('Starting XP: ' + str(startingxp) , 33)
            
def talismanXpToolTips():
    global counter
    global currentxp
    global minxp
    

    Misc.Pause(10000)
    temp = Items.GetPropStringByIndex(Talli, propLine)
    if temp == 'MAX':
        Misc.SendMessage('Talisman Maxxed, stopping', 33)
        Stop
    else:
        temp = temp.split(": ", 1)[1]
        temp = temp.split("/", 1)[0]

    if hasInt(temp):
        newxp = int(temp)
    else:
        newxp = currentxp
    
    difference = newxp - currentxp
    Misc.Pause(120)
    if difference > 0:
        Player.HeadMessage(54, '+' + str(difference) + ' xp')
        currentxp = newxp
    elif difference == 0:
            Misc.NoOperation()
    else:
        Player.HeadMessage(44, 'You leveled up!' )
        Misc.Pause(200)
        Player.ChatSay(66, '[e woohoo')
        Misc.RemoveSharedValue( pname + 'xp' )
        #startingxp = 0
        Misc.SetSharedValue( pname + 'xp', 0 )
        #Misc.SendMessage('Starting XP: ' + str(startingxp) , 33)
        Misc.Pause(10000)
    
    minxp = difference + minxp 
    counter = counter + 1
    if counter >= 6:
        overallxp = currentxp - startingxp
        if minxp > 0:
            Player.HeadMessage(54, '+' + str(minxp) + ' xp last 60s')
            Misc.Pause(200)
        
        if overallxp > 0:
            Player.HeadMessage(44, str(overallxp) + 'xp total.')
        elif overallxp == 0:
            Misc.NoOperation()
        else:
            Player.HeadMessage(44, 'You leveled up!' )
            Player.ChatSay(66, '[e woohoo')
            Misc.RemoveSharedValue( pname + 'xp' )
            setup() 
        counter = 0
        minxp = 0
    Misc.Pause(50)

def hasInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
        
def talismanXp():
    global counter
    global currentxp
    global minxp
    
    if Gumps.CurrentGump() == gumpid: 
        Misc.Pause(10000)
        temp = Gumps.LastGumpGetLine(gumpLine)
        temp = temp.split("/", 1)[0]
        if hasInt(temp):
            newxp = int(temp)
        else:
            newxp = currentxp
        
        difference = newxp - currentxp
        Misc.Pause(120)
        if difference > 0:
            Player.HeadMessage(54, '+' + str(difference) + ' xp')
            currentxp = newxp
        elif difference == 0:
                Misc.NoOperation()
        else:
            Player.HeadMessage(44, 'You leveled up!' )
            Player.ChatSay(66, '[e woohoo')
            Misc.RemoveSharedValue( pname + 'xp' )
            setup() 
        
        minxp = difference + minxp 
        counter = counter + 1
        if counter >= 6:
            overallxp = currentxp - startingxp
            if minxp > 0:
                Player.HeadMessage(54, '+' + str(minxp) + ' xp last 60s')
                Misc.Pause(200)
            
            if overallxp > 0:
                Player.HeadMessage(44, str(overallxp) + 'xp total.')
            elif overallxp == 0:
                Misc.NoOperation()
            else:
                Player.HeadMessage(44, 'You leveled up!' )
                Player.ChatSay(66, '[e woohoo')
                Misc.RemoveSharedValue( pname + 'xp' )
                setup() 
            counter = 0
            minxp = 0
    else:
        tempGump = Gumps.CurrentGump()
        Gumps.CloseGump(tempGump)
    Misc.Pause(50)
    

def setup():
    global startingxp
    global temp
    global currentxp
    
    Gumps.WaitForGump(gumpid, 10000)
    temp = Gumps.LastGumpGetLine(gumpLine)
    if temp == 'MAX':
        Misc.SendMessage('Talisman Maxxed, stopping', 33)
        Stop
    
    temp = temp.split("/", 1)[0]
    
    #Misc.SendMessage(str(temp))
    
    if hasInt(temp):
        currentxp = int(temp)
        #Misc.SendMessage('OK')
    else:
        Misc.Pause(600)
        Misc.SendMessage('retrying read')
        setup()
        
    if trackOnScript:
        startingxp = currentxp
        Misc.SendMessage('Starting XP: ' + str(startingxp), 33)
    else:
        if Misc.CheckSharedValue( pname + 'xp' ):
            startingxp = Misc.ReadSharedValue( pname + 'xp' )
            Misc.SendMessage('Starting XP: ' + str(startingxp) , 33)
            Misc.Pause(200)
            gainedXP = currentxp - startingxp
            if gainedXP > 0:
                Player.HeadMessage(66,'XP since run: ' + str(gainedXP))
            elif gainedXP == 0:
                Misc.NoOperation()
            else:
                Player.HeadMessage(44, 'You leveled up!' )
                Player.ChatSay(66, '[e woohoo')
                Misc.RemoveSharedValue( pname + 'xp' )
                setup() 
        else:
            startingxp = currentxp
            Misc.SetSharedValue( pname + 'xp', startingxp )
            Misc.SendMessage('Starting XP: ' + str(startingxp) , 33)

Misc.Pause(200)
pname = Player.Name.lower().replace(' ', '')
    
Talli = Player.GetItemOnLayer('Talisman')
if Talli:
    Tallyserial = Items.FindBySerial(Talli.Serial)
        Tallyserial = Items.FindBySerial(Talli.Serial)
    if Talli.Hue == 0x078c:
        propLine = 6
    else:
        propLine = 5
    gumpLine = 4
    gumpid = 463091633
else:
    Talli = Items.FindByID( 0x3679  , -1 , Player.Backpack.Serial)
    if Talli:
        Items.UseItem(Talli)
        Misc.Pause(600)
        Tallyserial = Items.FindBySerial(Talli.Serial)
        gumpLine = 4
        gumpid = 3527528070
        Misc.SendMessage('Using Meta Stone', 33)
    else:
        Misc.SendMessage('Talisman Not Found, Stopping', 33)
        Stop
        
        #setup()

try:
    if toolTipsOn:
        if Talli.ItemID == 0x3679:
            setup()
            while True:
                talismanXp()
        else:
            setupToolTips()
            if pname in noTrackList:
                Items.UseItem(Tallyserial)
                Misc.Pause(200)
                Stop
            while True:
                talismanXpToolTips()
    else:
        Items.UseItem(Tallyserial)
        Misc.Pause(200)
        if pname in noTrackList:
            Stop
        setup()
        while True:
            talismanXp()
except:
  print("An exception occurred")
