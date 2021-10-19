################## Constants #################

tongs = 0x0FBB
sewingkit=0x0F9D
regs = [0x0F7A, 0x0F86, 0x0F7B, 0x0F8C, 0x0F84, 0x0F85, 0x0F8D, 0x0F88]
rune = [6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96] #only works with gate
book = [0,1,2,3,4,5,6]
deedstorag= 0x4079777D
deedstosort = 0x41B89F04
deedmodel = 0x14EF
deedcolor = 0x044e
garbagecontainer =0x403C2A3E
smithgarbotxt = 'smithgarbo'


invasion = False

invasion2 = False



##################Variables #################

smithbodbag = 0x41B89F04 #commpdity deed box at home to dump shit in
tailorbodbag = 0x40349B3A #commodity deed box to dump shit.

botname = Player.Name
pname = Player.Name.lower().replace(' ', '')
if pname == 'knightbot':   #1
    glow = False
    NPC = 0x00198AD9
    if glow == True:
        tailornpc =  0x0002B253      
        tailorrune = 3
    else:
        tailorrune = 6
        tailornpc = 0x00008CCD
    book[0] = 0x434717C5

elif pname == 'fisheye': #2
    book[0] = 0x423D325C
    glow = False
    NPC = 0x00198AD9
    if glow == True:  
        tailornpc =  0x0002B253       
        tailorrune = 3
    else:
        tailorrune = 6
        tailornpc = 0x00008CCD
        
elif pname == 'crystalmetheny': #3
    book[0] = 0x423D3CC0
    glow = False
    NPC = 0x00198AD9
    if glow == True: 
        tailornpc =  0x0002B253        
        tailorrune = 3
    else:
        tailorrune = 6
        tailornpc = 0x00008CCD  
        
elif pname == 'louzar': #4
    book[0] = 0x423D4195
    glow = False
    NPC = 0x00198AD9
    if glow == True:  
        tailornpc =  0x0002B253       
        tailorrune = 3
    else:
        tailorrune = 6
        tailornpc = 0x00008CCD    

elif pname == 'wendywacko': #5
    book[0] = 0x423D4783
    glow = False
    NPC = 0x00198AD9
    if glow == True:  
        tailornpc =  0x0002B253       
        tailorrune = 3
    else:
        tailorrune = 6
        tailornpc = 0x00008CCD  
        
elif pname == 'terrybull': #6
    book[0] = 0x423D2CF6
    glow = False
    NPC = 0x00198AD9
    if glow == True:  
        tailornpc =  0x0002B253       
        tailorrune = 3
    else:
        tailorrune = 6
        tailornpc = 0x00008CCD  
elif pname == 'aimbotexe': #7
    book[0] = 0x43466393
    glow = False
    NPC = 0x00198AD9
    if glow == True:  
        tailornpc =  0x000610FA       
        tailorrune = 3
    else:
        tailorrune = 6
        tailornpc = 0x00008CCD  
elif pname == 'ctrlaltdel': #8
    book[0] = 0x423D3136
    glow = False
    NPC = 0x00198AD9
    if glow == True:  
        tailornpc =  0x000610FA       
        tailorrune = 3
    else:
        tailorrune = 6
        tailornpc = 0x00008CCD  

elif pname == 'kitkatkattle': #9
    book[0] = 0x423D25EC
    glow = False
    NPC = 0x00198AD9
    if glow == True:  
        tailornpc =  0x0002B253       
        tailorrune = 3
    else:
        tailorrune = 6
        tailornpc = 0x00008CCD

elif pname == 'bodybuilder': #10
    book[0] = 0x423D2FE5
    glow = False
    NPC = 0x00198AD9
    if glow == True:  
        tailornpc =  0x0002B253       
        tailorrune = 3
    else:
        tailorrune = 6
        tailornpc = 0x00008CCD

elif pname == 'bodgod': #11
    book[0] = 0x423D358F
    glow = False
    NPC = 0x00198AD9
    if glow == True:  
        tailornpc =  0x0002B253       
        tailorrune = 3
    else:
        tailorrune = 6
        tailornpc = 0x00008CCD    

elif pname == 'rambod':   #12
    book[0] = 0x423D2EE9
    glow = False
    NPC = 0x00198AD9
    if glow == True:  
        tailornpc =  0x0002B253       
        tailorrune = 3
    else:
        tailorrune = 6
        tailornpc = 0x00008CCD  
elif pname == 'wyrmtwig': #13
    book[0] = 0x423D4A9B
    glow = False
    NPC = 0x00198AD9
    if glow == True:  
        tailornpc =  0x0002B253       
        tailorrune = 3
    else:
        tailorrune = 6
        tailornpc = 0x00008CCD  
elif pname == 'saltsniffer': #14
    book[0] = 0x423D40A6
    glow = False
    NPC = 0x00198AD9
    if glow == True:  
        tailornpc =  0x0002B253       
        tailorrune = 3
    else:
        tailorrune = 6
        tailornpc = 0x00008CCD  
elif pname == 'nightbod': #15
    book[0] = 0x423D3D78
    glow = False
    NPC = 0x00198AD9
    if glow == True:  
        tailornpc =  0x0002B253       
        tailorrune = 3
    else:
        tailorrune = 6
        tailornpc = 0x00008CCD  
elif pname == 'blackfox': #16
    book[0] = 0x423D3679
    glow = False
    NPC = 0x00198AD9
    if glow == True:  
        tailornpc =  0x0002B253       
        tailorrune = 3
    else:
        tailorrune = 6
        tailornpc = 0x00008CCD  



        
def worldSave():
    if Journal.SearchByType('The world will save in 1 minute.', 'Regular' ):
        Misc.SendMessage('Pausing for world save', 33)
        while not Journal.SearchByType('World save complete.', 'Regular'):
            Misc.Pause(500)
        Misc.Pause(2500)
        Misc.SendMessage('Continuing run', 33)
        Journal.Clear()       
    
def webhook(msg):
    URI = 'https://discordapp.com/api/webhooks/654131394854781018/KySfeUnLjoFmqfmf154_1V22nxkzGnDmOP6-j8Kj__Ei8boMeHwzir6irC57rIY65_6q'
    alert = msg
    report = "content="+ alert
    PARAMETERS=report
    from System.Net import WebRequest
    request = WebRequest.Create(URI)
    request.ContentType = "application/x-www-form-urlencoded"
    request.Method = "POST"
    from System.Text import Encoding
    bytes = Encoding.ASCII.GetBytes(PARAMETERS)
    request.ContentLength = bytes.Length
    reqStream = request.GetRequestStream()
    reqStream.Write(bytes, 0, bytes.Length)
    reqStream.Close()
    response = request.GetResponse()
    from System.IO import StreamReader
    result = StreamReader(response.GetResponseStream()).ReadToEnd().replace('\r', '\n')        
    
def recall(book, rune):
    mana(30)
    worldSave()
    caststr()
    rune = 5+6*rune
    currentlocation = Player.Position
    Misc.Pause( 750 )
    Items.UseItem(book)
    Misc.Pause( 500 )
    Gumps.WaitForGump( 1431013363, 5000 )
    Misc.Pause( 500 )
    Gumps.SendAction( 1431013363, rune )       
    Misc.Pause( 500 )
    Misc.Pause(1500)
        
def mana(mana_req):
    if Player.Mana < mana_req:
        Player.UseSkill( 'Meditation' )
        while Player.Mana < ( Player.ManaMax ):
            Misc.Pause( 50 )
def castincog():
    if Player.BuffsExist('Incognito'):
        Player.HeadMessage(54,'incog already on')
    else:
        Spells.CastMagery( 'Incognito' )
        Misc.Pause(1500)
        
def gohome():
    if str(Player.Position) == '(6215, 3410, 35)':
        webhook('home already')
        return  
    recall(book[0],0)
    Misc.Pause(500)
    Player.Walk("North")
    Player.Walk("North")
    Player.Walk("North")

    Misc.Pause(2000)
    if str(Player.Position) != '(6215, 3410, 35)':
        webhook("failed to go home")    
        gohome()        
    else:
        webhook("I am at home")        
        
def caststr():
    if Player.Weight > 375 and not Player.BuffsExist( 'Strength' ):
            Spells.CastMagery( 'Strength' )
            Target.WaitForTarget( 10000, False )
            Target.Self()
            Misc.Pause( 1000 ) 

       
def comparetolist(bod, input):
    filepath = 'C:/Users/Jason/PycharmProjects/BodBot/' + input + ".txt"
    f = open(filepath, 'r')        
    allinlist = f.readlines()
    f.close()
  
    #Player.HeadMessage(54, str(len(allinlist)))
    for i in range(0, len(allinlist)):
        #Player.HeadMessage(54, str(allinlist[i]))
        #Player.HeadMessage(54, str(getstringofbod(0x44D90146)))
        if getstringofbod(bod) == allinlist[i]:
            Player.HeadMessage(54, "Match found from list")
            return True
        else:
            Misc.Pause(5)
    return False
                    
def getstringofbod(bod):
        result= ""
        bodList = Items.GetPropStringList(bod)
        for i in range(0, len(bodList)):
            result = result + bodList[i]
            
        result = result.replace("[","")
        result = result.replace("]","")
        result = result.replace(" deedBlessed<BASEFONT COLOR=#585868> Hue: 1102 <BASEFONT COLOR=#FFFFFF>Weight: 1 stone","")
        result = result.replace("bulk orderAll items must be","")
        result = result.replace(".All items must be made with","")
        result = result.replace(".amount to make:","")
        result = result.replace("a bulk order","")
        
        result = result + '\n'
        return result
        
  
def checkgarbo(bod):
    if comparetolist(bod, smithgarbotxt ):
        Player.HeadMessage(54, "Sending to garbage")
        Items.Move(bod, garbagecontainer, 0)
        return True
    else:
        return False       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
            
def regcount():
    webhook('Pearl: ' + str(Items.BackpackCount(0x0F7A,0)) +'/Root: ' + str(Items.BackpackCount(0x0F86,0)) + '/Moss: ' + str(Items.BackpackCount(0x0F7B,0)) + '/Sulf: ' + str(Items.BackpackCount(0x0F8C,0)) + '/Gar: ' + str(Items.BackpackCount(0x0F84,0)) + '/Gin: ' + str(Items.BackpackCount(0x0F85
    ,0))+'/Silk: ' + str(Items.BackpackCount(0x0F8D,0)) + '/Shade: ' + str(Items.BackpackCount(0x0F88,0))            )
     
def checkregs():
    #if Items.BackpackCount(0x0F7A,0) <50 or Items.BackpackCount(0x0F86,0) <50 or Items.BackpackCount(0x0F7B,0) < 50 orItems.BackpackCount(0x0F8C,0) < 50 or Items.BackpackCount(0x0F84,0) <50 or Items.BackpackCount(0x0F85,0)<50 or Items.BackpackCount(0x0F8D,0) <50 orItems.BackpackCount(0x0F88,0):
     for reg in regs:
         if Items.BackpackCount(reg,0)<50:
            restock() 

def restock():
    webhook('Need Regs')
    recall(book[0], 1) 
    Misc.Pause(1500)
    Mobiles.UseMobile(0x000E0470)
    Misc.Pause(1000)
    Gumps.WaitForGump(989312372, 10000)
    Gumps.SendAction(989312372, 4)
    Gumps.WaitForGump(989312372, 10000)
    Gumps.SendAction(989312372, 8)
    Misc.Pause(1000)
    regcount()
    Misc.Pause(1000) 
 
def smithbodready():
    Journal.Clear()
    Misc.Pause(1000)
    Misc.WaitForContext(0x000BB73D, 10000)
    Misc.ContextReply(0x000BB73D, 1)
    Misc.Pause(1000)
    if Journal.Search("can get"):
        Player.HeadMessage(54, "can get an order") 
        Misc.Pause(1000)
        return True
    else:
        webhook(botname + ' ended up at smith bod before its read')
        return False


def invasionsmithbods():
    Misc.Pause(1000)
    abortcounter = 0
    webhook('Getting smith Bod')   
    Items.UseItem(0x4083A7E1)
    Misc.Pause(1000)
    Spells.CastMagery("Recall")
    Target.WaitForTarget(10000, False)
    Misc.Pause(600)
    Target.TargetExecute(0x459A5682)
    Misc.Pause(15000)
    Misc.Pause(2000)
    Misc.Resync()
    Player.Walk("North")
    #Player.Walk("North")
    #Misc.Resync()
    #Journal.Clear()
    Misc.Pause(3000)
    Misc.WaitForContext(0x00029397, 10000)
    Misc.Pause(1000)
    Misc.ContextReply(0x00029397, 1)
    Misc.Pause(1000)
    if Journal.Search("can get"):
        Player.HeadMessage(54, "can get an order") 
        Misc.Pause(1000)
        smithrdy = True
    else:
        webhook(botname + ' ended up at smith bod before its read')
        smithrdy = False
    
    
    if smithrdy:
        while not Gumps.HasGump():
            abordcounter = abortcounter +1
            if abortcounter > 25:
                gohome()
            if Items.FindByID(tongs, -1, Player.Backpack.Serial):
                Misc.WaitForContext(0x00029397, 10000) #sell 
                Misc.ContextReply(0x00029397, 3)
            else:
                Misc.WaitForContext(0x00029397, 10000)
                Misc.ContextReply(0x00029397, 2)
                Misc.Pause(1000)
        while Items.FindByID(tongs, -1, Player.Backpack.Serial):
            Misc.WaitForContext(0x00029397, 10000) #sell 
            Misc.ContextReply(0x00029397, 3)
                
        Gumps.WaitForGump(3188567326, 2000)
        Gumps.SendAction(3188567326, 1)
        Gumps.WaitForGump(2611865322, 2000)
        Gumps.SendAction(2611865322, 1)        
        
def invasionsmithbods2():
    Misc.Pause(1000)
    abortcounter = 0
    webhook('Getting smith Bod')   
    Items.UseItem(0x4083A7E1)
    Misc.Pause(1000)
    Spells.CastMagery("Recall")
    Target.WaitForTarget(10000, False)
    Misc.Pause(600)
    Target.TargetExecute(0x419BD34E)
    Misc.Pause(15000)


    Misc.WaitForContext(0x000013B7, 10000)
    Misc.Pause(1000)
    Misc.ContextReply(0x000013B7, 1)
    Misc.Pause(1000)
    if Journal.Search("can get"):
        Player.HeadMessage(54, "can get an order") 
        Misc.Pause(1000)
        smithrdy = True
    else:
        webhook(botname + ' ended up at smith bod before its read')
        smithrdy = False
    
    
    if smithrdy:
        while not Gumps.HasGump():
            abordcounter = abortcounter +1
            if abortcounter > 25:
                gohome()
            if Items.FindByID(tongs, -1, Player.Backpack.Serial):
                Misc.WaitForContext(0x000013B7, 10000) #sell 
                Misc.ContextReply(0x000013B7, 3)
            else:
                Misc.WaitForContext(0x000013B7, 10000)
                Misc.ContextReply(0x000013B7, 2)
                Misc.Pause(1000)
        while Items.FindByID(tongs, -1, Player.Backpack.Serial):
            Misc.WaitForContext(0x000013B7, 10000) #sell 
            Misc.ContextReply(0x000013B7, 3)
                
        Gumps.WaitForGump(3188567326, 2000)
        Gumps.SendAction(3188567326, 1)
        Gumps.WaitForGump(2611865322, 2000)
        Gumps.SendAction(2611865322, 1)                 
def smithbods():
    abortcounter = 0
    webhook('Getting smith Bod')   
    recall(book[0],2)
    if smithbodready():
        while not Gumps.HasGump():
            abordcounter = abortcounter +1
            if abortcounter > 25:
                gohome()
            if Items.FindByID(tongs, -1, Player.Backpack.Serial):
                Misc.WaitForContext(0x000BB73D, 10000) #sell 
                Misc.ContextReply(0x000BB73D, 3)
            else:
                Misc.WaitForContext(0x000BB73D, 10000)
                Misc.ContextReply(0x000BB73D, 2)
                Misc.Pause(1000)
        while Items.FindByID(tongs, -1, Player.Backpack.Serial):
            Misc.WaitForContext(0x000BB73D, 10000) #sell 
            Misc.ContextReply(0x000BB73D, 3)
                
        Gumps.WaitForGump(3188567326, 2000)
        Gumps.SendAction(3188567326, 1)
        Gumps.WaitForGump(2611865322, 2000)
        Gumps.SendAction(2611865322, 1)

def tailorbodready():
    Journal.Clear()
    Misc.Pause(500)
    Misc.WaitForContext(tailornpc, 10000)
    Misc.ContextReply(tailornpc, 1)
    Misc.Pause(1000)
    if Journal.Search("can get"):
        Player.HeadMessage(54, "can get an order") 
        Misc.Pause(1000)
        return True
    else:
        webhook(botname + ' ended up at tailor bod before its read')
        return False   

def tailorbods():
    webhook('Getting Tailor Bod')
    abortcounter = 0
    recall(book[0],tailorrune)   
    
    if tailorbodready():
        while not Gumps.HasGump():
            abordcounter = abortcounter + 1
            if abortcounter > 25:
                gohome()
            if Items.FindByID(sewingkit, -1, Player.Backpack.Serial):
                Misc.WaitForContext(tailornpc, 10000)
                Misc.ContextReply(tailornpc, 3)
                Misc.Pause(750)
            else:
                Misc.WaitForContext(tailornpc, 10000)
                Misc.ContextReply(tailornpc, 2)
                Misc.Pause(1000)
        while Items.FindByID(sewingkit, -1, Player.Backpack.Serial):
            Misc.WaitForContext(tailornpc, 10000)
            Misc.ContextReply(tailornpc, 3)
            Misc.Pause(100)   
        
        Gumps.WaitForGump(3188567326, 2000)
        Gumps.SendAction(3188567326, 1)
        Gumps.WaitForGump(2611865322, 2000)
        Gumps.SendAction(2611865322, 1)
        Misc.Pause(2000)


def discordbod(bod):
        result = ''
        bodList = Items.GetPropStringList(bod)
        for i in range(0, len(bodList)):
            #if i > (z -1):
                result = result + bodList[i]

        result = result.replace("bulk orderAll items must be",'')
        result = result.replace('.amount to make','')
        result = result.replace(': 0','')
        result = result.replace('.All items must be made with','')
        result = result.replace('<BASEFONT COLOR=#204018>Hue: Rusty Green (1155)<BASEFONT COLOR=#FFFFFF>Weight: 1','')
        result = result.replace('a bulk order deedBlessed stonelarge','')
        result = result.replace('a bulk order deedBlessed<BASEFONT COLOR=#606070> Hue: 1102 <BASEFONT COLOR=#FFFFFF>Weight: 1 stonesmall ','')
        result = result.replace('a bulk order deedBlessed<BASEFONT COLOR=#606070> Hue: 1102 <BASEFONT COLOR=#FFFFFF>Weight: 1 stonelarge','')
        result = result.replace('a bulk order deedBlessed stonesmall ','')
        
        webhook(result)
   
    
def unload():    
    gohome()
    Misc.Pause(1000)

    while Items.FindByID(0x14EF, 0x0483, Player.Backpack.Serial): #tailor bods
        currenttarget = Items.FindByID(0x14EF, 0x0483, Player.Backpack.Serial)
        Items.Move(currenttarget, tailorbodbag, -1) 
        Misc.Pause(1000)   
    while Items.FindByID(0x14EF, 0x044E, Player.Backpack.Serial): #smith bods
        currenttarget = Items.FindByID(0x14EF, 0x044E, Player.Backpack.Serial)
        if checkgarbo(currenttarget):
            Player.HeadMessage(54, "garbage")
            Misc.Pause(500)
        else:
            Items.Move(currenttarget, smithbodbag, 0)
        Misc.Pause(1000)           
 
def writetime(text):
    f = open('C:/Users/Jason/PycharmProjects/BodBot/MastBodStatus.txt', 'w')        
    f.write(str(text))
    f.close()
    
def readtime(file):
    f = open('C:/Users/Jason/PycharmProjects/BodBot/MastBodStatus.txt', 'r')
    x = f.read()
    return x    
    
    
    
    
    
restock()

Misc.Pause(3000)   
if BuyAgent.Status( ) == False:
    Player.HeadMessage(54, "Starting buy agent")
    BuyAgent.Enable()
Misc.Pause(500)
if SellAgent.Status( ) == False:
    Player.HeadMessage(54, "Starting sell agent")
    SellAgent.Enable()
    Misc.Pause(1000)

writetime('start')

temp = botname + " is getting bods"
webhook(temp)    
checkregs()
if invasion:
    invasionsmithbods()
elif invasion2:
    invasionsmithbods2()
else:
    smithbods()
tailorbods()
Misc.Pause(2000)
unload()
Misc.Pause(2000)
writetime('done')


