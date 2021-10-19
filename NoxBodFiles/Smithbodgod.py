
restockchest = 0x448B879A
garbagecontainer = 0x467098AD
smithgarbotxt="smithgarbo" #text file containing all the smith garbage data
bodstorage = 0x43A2140A
fullbodz = 0x448B879A #storage for bods ready to be turned in
frombook = 0x4BAB2CC4

#####COLORS######
iron=0x0000
dc=0x0415
shadow=0x0455
copper =0x045f
bronze=0x06d8
gold=0x06b7
aggy=0x097e
ver=0x07d2
val=0x0544

##### CONSTANTS #####
tinktool = 0x1EB8
ingotmodel = 0x1BF2
hammermodel = 0x13E3
deedmodel = 0x14EF
deedcolor = 0x044e


def worldSave():
    if Journal.SearchByType('The world will save in 1 minute.', 'Regular' ):
        Misc.SendMessage('Pausing for world save', 33)
        while not Journal.SearchByType('World save complete.', 'Regular'):
            Misc.Pause(500)
        Misc.Pause(2500)
        Misc.SendMessage('Continuing run', 33)
        Journal.Clear()  
        
def checktools():
    if Items.BackpackCount(tinktool , -1) < 3:
        Misc.SendMessage('Out of Tink Tools',33)
        craftTink()
    Misc.Pause(1000)    
    if Items.BackpackCount(hammermodel , -1) < 3:
        Misc.SendMessage('Out of hammers',33)
        craftsmithtool()
        
def craftTink():    
    UseTinkTool = Items.FindByID(tinktool, -1, Player.Backpack.Serial)
    Items.UseItem(UseTinkTool.Serial)
    Gumps.WaitForGump(949095101, 1500)
    Gumps.SendAction(949095101, 8)
    Gumps.WaitForGump(949095101, 1500)
    Gumps.SendAction(949095101, 23)
    Misc.Pause(2000)
        
        
def craftsmithtool():
    UseTinkTool = Items.FindByID(tinktool, -1, Player.Backpack.Serial)
    Items.UseItem(UseTinkTool.Serial)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 8)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 93)
    Gumps.WaitForGump(949095101, 10000)
    Misc.Pause(2000)
    Gumps.SendAction(949095101, 0) 
 
def unstock():
    Player.HeadMessage(54, "Unstocking")
    while Items.FindByID(ingotmodel,-1, Player.Backpack.Serial):
        moveitem = Items.FindByID(ingotmodel,-1, Player.Backpack.Serial)
        Items.Move(moveitem, restockchest, 0)
        Misc.Pause(750)
    stock(iron, 20)   

def stock(color,qtyreq):
    Player.HeadMessage(54, "Checking ingot stock")
    inbag = Items.BackpackCount(ingotmodel, color)
    if inbag < qtyreq:
        Items.UseItem(restockchest)
        Misc.Pause(750)
        instock = Items.ContainerCount(restockchest,ingotmodel,color) #how many of that ingot do we have in stock
        if instock >= qtyreq:
            qty = qtyreq-inbag
            moveitem = Items.FindByID(ingotmodel,color, restockchest)
            Items.Move(moveitem, Player.Backpack.Serial, qty)
            return True
        elif instock <= qtyreq:
            Player.HeadMessage(54, "Not enough of that ingot color sorry")
            return False
            
                
        
def craftinglogic(bod):
    
    #Legend
    #bodarray = [first menue, second menue, total qty, menue for color, actual color, exeptional(t/f), full? (t/f), use special hammer)
    
    
    bodarray = [0,0,0,0,0,0,0,0]
    tempx = Items.GetPropStringList(bod)
    
    #Trim string list a bit
    x = ""
    for i in range(0, len(tempx)):
        x = x + tempx[i]            
        x = x.replace("<BASEFONT COLOR=#585868> Hue: 1102 <BASEFONT COLOR=#FFFFFF>","")

    
    
    Player.HeadMessage(54, str(x))
    
######## shields ################    
    if "buckler" in str(x):
        prop1 = 36
        prop2 = 2
    if "bronze shield" in str(x):
        prop1 = 36
        prop2 = 9
    if "heater shield" in str(x):
        prop1 = 36
        prop2 = 16
    if "metal shield" in str(x):
        prop1 = 36
        prop2 = 23
    if "metal kite shield" in str(x):
        prop1 = 36
        prop2 = 30
    if "tear kite shield" in str(x):
        prop1 = 36
        prop2 = 37
######## helmets ################    
    if "bascinet" in str(x):
        prop1 = 29
        prop2 = 2

    if "helmet" in str(x):
        if "close" in str(x):
            prop1 = 29
            prop2 = 9
        else:
            prop1 = 29
            prop2 = 16
    if "norse helm" in str(x):
        prop1 = 29
        prop2 = 23
    if "plate helm" in str(x):
        prop1 = 29
        prop2 = 30
                                      
######## ringmail ################    
    if "ringmail gloves" in str(x):
        prop1 = 8
        prop2 = 2
    if "ringmail leggings" in str(x):
        prop1 = 8
        prop2 = 9
    if "ringmail sleeves" in str(x):
        prop1 = 8
        prop2 = 16
    if "ringmail tunic" in str(x):
        prop1 = 8
        prop2 = 23
    if "ringmail tunic" in str(x):
        prop1 = 8
        prop2 = 23        
######## chain ################    
    if "chainmail coif" in str(x):
        prop1 = 15
        prop2 = 2
    if "chainmail leggings" in str(x):
        prop1 = 15
        prop2 = 9
    if "chainmail tunic" in str(x):
        prop1 = 15
        prop2 = 16
######## plate ################    
    if "platemail arms" in str(x):
        prop1 = 22
        prop2 = 2
    if "platemail gloves" in str(x):
        prop1 = 22
        prop2 = 9
    if "platemail gorget" in str(x):
        prop1 = 22
        prop2 = 16
    if "platemail legs" in str(x):
        prop1 = 22
        prop2 = 23
    if "platemail tunic" in str(x):
        prop1 = 22
        prop2 = 30
    if "female plate" in str(x):
        prop1 = 22
        prop2 = 37
######QTY#######        
    if "amount to make: 20" in x:
        prop3 = 20
    if "amount to make: 15" in x:
        prop3 = 15
    if "amount to make: 10" in x:
        prop3 = 10
        
######color#######         
    if "All items must be made with valorite ingots." in x:
        prop4 = 62
        prop5 = val
    if "All items must be made with verite ingots." in x:
        prop4 = 55
        prop5 = ver
    if "All items must be made with agapite ingots." in x:
        prop4 = 48
        prop5 = aggy
    if "All items must be made with gold ingots." in x:
        prop4 = 41
        prop5 = gold
    if "All items must be made with bronze ingots." in x:
        prop4 = 34
        prop5 = bronze
    if "All items must be made with copper ingots." in x:
        prop4 = 27
        prop5 = copper
    if "All items must be made with shadow iron ingots." in x:
        prop4 = 20
        prop5 = shadow
    if "All items must be made with dull copper ingots." in x:
        prop4 = 13
        prop5 = dc
    if "All items must be made with iron ingots." in x:
        prop4 = 6
        prop5 = iron
    if "All items must be exceptional." in x:
        prop6 = True
    Player.HeadMessage(54, str(prop3))    
    if str(x).count(str(prop3)) > 1:
        prop7 = True #True = bod is full
    else:
        prop7 = False
    if "Large" in x:
        prop8 = True
    else:
        prop8 = False


        
    bodarray[0]= prop1 #first menue option
    bodarray[1] = prop2 #second menue option
    bodarray[2] = prop3 #Req Qty
    bodarray[3] = prop4 #Menue for color
    bodarray[4] = prop5 #color idtag
    bodarray[5] = prop6 #Exceptional ? T/F 
    bodarray[6] = prop7 # Full? T/F
    bodarray[7] = prop8 #Lbod? T/F
    #prop8 = need hammer? 
    return bodarray    


    
def bagindexing():
    inventory = []
    for item in Player.Backpack.Contains: 
        inventory.append(item.Serial)
        Misc.Pause(15)
    return inventory    

def findnewitem(inv): #works but the string is weird if you print it. 
        for item in Player.Backpack.Contains:
            if item.Serial not in inv:
                return item.Serial
                

def setingotcolor(craftcolor):
    Misc.Pause(500)
    UseTool = Items.FindByID(hammermodel, -1, Player.Backpack.Serial) 
    Items.UseItem(UseTool.Serial)
    Misc.Pause(500)
    Player.HeadMessage(54, "setting crafting ingot type") 
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 7)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, craftcolor) 
    Misc.Pause(1000)
 
                
def craftitems(bod):
    logicarray = craftinglogic(bod) #prime
    Player.HeadMessage(54, "starting to craft")
    setingotcolor(logicarray[3])
    Player.HeadMessage(54, "is it full?" + str(logicarray[6]))
    while logicarray[6] == False:
        worldSave()
        checktools()
        if stock(logicarray[4],100) is False: #stocks 100 of ingot color if it fails it stores bod
            sortbod(bod)
            return
        Misc.Pause(1000)    
        inventory = bagindexing()
        Misc.Pause(1000)        
                        
        UseTool = Items.FindByID(hammermodel, -1, Player.Backpack.Serial) 
        Items.UseItem(UseTool.Serial)

        Misc.Pause(250)
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, logicarray[0])
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, logicarray[1])
        Misc.Pause(2000)  
        item = findnewitem(inventory)
        if item != None:
            Journal.Clear()
            Items.SingleClick(item)
            Misc.Pause(800)
            if Journal.Search("Exceptional"):
                Player.HeadMessage(54, "Exceptional")
                Items.UseItem(bod)
                Misc.Pause(750)
                Gumps.SendAction(1526454082, 2)
                Misc.Pause(750)
                Target.TargetExecute(item)       
                Misc.Pause(750)
            else:
                Player.HeadMessage(54, "Shitty craft bro")
                Misc.Pause(500)
                UseTool = Items.FindByID(hammermodel, -1, Player.Backpack.Serial) 
                Items.UseItem(UseTool.Serial)
                Misc.Pause(500)
                Gumps.WaitForGump(949095101, 10000)
                Gumps.SendAction(949095101, 14)
                Misc.Pause(750)
                Target.TargetExecute(item)
                Misc.Pause(1000) 
        logicarray = craftinglogic(bod)      
    #craft loop finished
    
############################################################################        
####################################### SORTING ############################

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
        
def stringtest(x):
    f = open('C:/Users/Jason/PycharmProjects/BodBot/test.txt', 'a')        
    f.write(str(x))
    f.close()
  
def checkgarbo(bod):
    if comparetolist(bod, smithgarbotxt ):
        Player.HeadMessage(54, "Sending to garbage")
        Items.Move(bod, garbagecontainer, 0)
        return True
    else:
        return False
        
def sortbod(bod): #soem sort of logic to sort bods, this is called if we run out of ingots for a bod
    logicarray = craftinglogic(bod)
    if logicarray[6] is True: #ie bod is full
        Items.Move(bod, fullbodz, 0)
        Player.HeadMessage(54, "Congrats Bod is ready to be turned in")
    else:    
        Items.Move(bod, bodstorage, 0)
    
 
def grabbod():
        
        Items.UseItem(frombook)
        Misc.Pause(1000)
        Gumps.SendAction(1425364447, 5)
        Misc.Pause(1000)
        x = Items.FindByID(deedmodel, deedcolor, Player.Backpack.Serial)
        return x     
    
    
    
####################################### SORTING ############################
############################################################################        
                
def main():
    Journal.Clear()
    logicarray =  [0,0,0,0,0] #initializing 
    #bod = grabbod()
    while Items.FindByID(deedmodel,deedcolor, Player.Backpack.Serial):
        bod=Items.FindByID(deedmodel,deedcolor, Player.Backpack.Serial)
        Player.HeadMessage(54, "mark1")
        if checkgarbo(bod) is True:
          return
        else:  
            #bod = 0x47079787
            #bod = 0x43F14045 #half full bod
            
            #stringtest(logicarray)
            #stringtest(Items.GetPropStringList(bod))
            #Player.HeadMessage(54, str(logicarray))
            craftitems(bod)
            Misc.Pause(1000)
            unstock()
        sortbod(bod)

        
        
        
#Player.HeadMessage(54, str(craftinglogic(0x4050F4EF))   )     
        
while True: 
    #unstock()   
    main()
    Misc.Pause(1000)