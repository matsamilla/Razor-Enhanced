#frombook = 0x43909128
frombook =0x43909128 #dehued normal book in bag
lbodstorage = 0x4083CF0E
lbodstorage2 = 0x45E3CA15
fullbod = [ 0x41660840  , 0x43908F54  ] #chest first, book second
nomatchstorage = 0x41113188

bonestorage = 0x43E08982
#leatherstorage= 0x4391DCB4 #leather keeper 1
leatherstorage= 0x43647AB7



garbagebox = 0x4009C22A #temporary 


deed = 0x14EF
tinktool = 0x1EB8
sewtool = 0x0F9D
restockchest = 0x405183AA
cloth = 0x1766
leather = 0x1081 #no color so it randomly pics a quality
ingot = 0x1BF2
trash = 0x403C2A3E
bone = 0x0F7E

barbedcolor= 0x059d
spinecolor= 0x05e4
hornedcolor= 0x0900
leathercolor = 0x0000




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
    if Items.BackpackCount(sewtool , -1) < 3:
        Misc.SendMessage('Out of sewtool',33)
        craftsewtool()
        
def craftTink():    
    UseTinkTool = Items.FindByID(tinktool, -1, Player.Backpack.Serial)
    Items.UseItem(UseTinkTool.Serial)
    Gumps.WaitForGump(949095101, 1500)
    Gumps.SendAction(949095101, 8)
    Gumps.WaitForGump(949095101, 1500)
    Gumps.SendAction(949095101, 23)
    Misc.Pause(2000)
        
        
def craftsewtool():
    UseTinkTool = Items.FindByID(tinktool, -1, Player.Backpack.Serial)
    Items.UseItem(UseTinkTool.Serial)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 8)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 44)
    Gumps.WaitForGump(949095101, 10000)
    Misc.Pause(2000)
    Gumps.SendAction(949095101, 0)    

def setsemat(material):
    
    if material == barbedcolor:
        UseTool = Items.FindByID(sewtool, -1, Player.Backpack.Serial)
        Items.UseItem(UseTool.Serial)
        Misc.Pause(500)
        Gumps.SendAction(949095101, 7)
        Misc.Pause(500)
        Gumps.SendAction(949095101, 27)
    if material == hornedcolor:
        UseTool = Items.FindByID(sewtool, -1, Player.Backpack.Serial)
        Items.UseItem(UseTool.Serial)
        Misc.Pause(500)
        Gumps.SendAction(949095101, 7)
        Misc.Pause(500)
        Gumps.SendAction(949095101, 20)
    if material == spinecolor:
        UseTool = Items.FindByID(sewtool, -1, Player.Backpack.Serial)
        Items.UseItem(UseTool.Serial)
        Misc.Pause(500)
        Gumps.SendAction(949095101, 7)
        Misc.Pause(500)
        Gumps.SendAction(949095101, 13)
    if material == "-1":
        UseTool = Items.FindByID(sewtool, -1, Player.Backpack.Serial)
        Items.UseItem(UseTool.Serial)
        Misc.Pause(500)
        Gumps.SendAction(949095101, 7)
        Misc.Pause(500)
        Gumps.SendAction(949095101, 6)
    if material == -1:
        UseTool = Items.FindByID(sewtool, -1, Player.Backpack.Serial)
        Items.UseItem(UseTool.Serial)
        Misc.Pause(500)
        Gumps.SendAction(949095101, 7)
        Misc.Pause(500)
        Gumps.SendAction(949095101, 6)


    
def unstock():
    while Items.FindByID(bone,-1, Player.Backpack.Serial):
        moveitem = Items.FindByID(bone,-1, Player.Backpack.Serial)
        Items.Move(moveitem, restockchest, 0)
        Misc.Pause(750)        
    while Items.FindByID(leather,-1, Player.Backpack.Serial):
        moveitem = Items.FindByID(leather,-1, Player.Backpack.Serial)
        Items.Move(moveitem, restockchest, 0)
        Misc.Pause(750)    
    while Items.FindByID(cloth,-1, Player.Backpack.Serial):
        moveitem = Items.FindByID(cloth,-1, Player.Backpack.Serial)
        Items.Move(moveitem, restockchest, 0)
        Misc.Pause(750) 
    
        
def checkrestock(materialtype, color): #loads crafting stuff
    if materialtype == "cloth":
        material = cloth
    elif color == barbedcolor:
        material = leather
    elif color == hornedcolor:
        material = leather    
    elif color == spinecolor:
        material = leather    
    elif color == -1:
        material = leather
        color = leathercolor
    Player.HeadMessage(54, str(materialtype))
    Player.HeadMessage(54, str(color))
    x = Items.BackpackCount(material, color)
    Player.HeadMessage(54, "Material Count" + str(x))
    if materialtype == "bone":
        if Items.BackpackCount(bone, -1) < 15:
            Items.UseItem(restockchest)
            Misc.Pause(500)       
            if Items.FindByID(bone, -1, restockchest):
                targetitem = Items.FindByID(bone, -1, restockchest)
                Items.Move(targetitem, Player.Backpack.Serial , 30)
                Misc.Pause(1000)
        if Items.BackpackCount(leather, color) < 20:
            if Items.FindByID(leather, color, restockchest):
                targetitem = Items.FindByID(leather, color, restockchest)
                Items.Move(targetitem, Player.Backpack.Serial , 75)
                Misc.Pause(1000)
        
    
    if Items.BackpackCount(material, color) < 25:
        Items.UseItem(restockchest)
        Misc.Pause(1000)       
        if Items.FindByID(material, color, restockchest):
            targetitem = Items.FindByID(material, color, restockchest)
            Items.Move(targetitem, Player.Backpack.Serial , 100)
            Misc.Pause(1000)
    if Items.BackpackCount(ingot, -1) < 10:
        Items.UseItem(restockchest)
        Misc.Pause(1000)       
        if Items.FindByID(ingot, -1, restockchest):
            targetitem = Items.FindByID(ingot, -1, restockchest)
            Items.Move(targetitem, Player.Backpack.Serial , 50)
            Misc.Pause(1000)    

def catagorylogic(bod): #working
    #Hats is first gump 1
    #shirts is first gump 8
    #pants is gump 15
    #misc is gump 22
    #footware is 29
        
    x = Items.GetPropStringList(bod)
           
######## HATS ################    
    if "doublet: 0" in x:
        return [8,2,"cloth"];
    if "shirt: 0" in x:
        return [8,9,"cloth"];
    if "fancy shirt: 0" in x:
        return [8,16,"cloth"];        
    if "tunic: 0" in x:
        return [8,23,"cloth"];        
    if "surcoat: 0" in x:
        return [8,30,"cloth"];          
    if "plain dress: 0" in x:
        return [8,37,"cloth"];
    if "fancy dress: 0" in x:
        return [8,44,"cloth"];
    if "cloak: 0" in x:
        return [8,51,"cloth"];        
    if "robe: 0" in x:
        return [8,58,"cloth"];
    if "jester suit: 0" in x:
        return [8,65,"cloth"];        
        
 
 ######## shirts ################    
    if "skullcap: 0" in x:
        return [1,2,"cloth"];
    if "bandana: 0" in x:
        return [1,9,"cloth"];
    if "floppy hat: 0" in x:
        return [1,16,"cloth"];        
    if "cap: 0" in x:
        return [1,23,"cloth"];        
    if "wide-brim hat: 0" in x:
        return [1,30,"cloth"];          
    if "straw hat: 0" in x:
        return [1,37,"cloth"];
    if "tall straw hat: 0" in x:
        return [1,44,"cloth"];
    if "wizard's hat: 0" in x:
        return [1,51,"cloth"];        
    if "bonnet: 0" in x:
        return [1,58,"cloth"];
    if "feathered hat: 0" in x:
        return [1,65,"cloth"];        
    if "tricorne hat: 0" in x:
        return [1,72,"cloth"];        
    if "jester hat: 0" in x:
        return [1,79,"cloth"];        
 
######## pants ################    
    if "short pants: 0" in x:
        return [15,2,"cloth"];
    if "long pants: 0" in x:
        return [15,9,"cloth"];
    if "kilt: 0" in x:
        return [15,16,"cloth"];        
    if "skirt: 0" in x:
        return [15,23,"cloth"];  

######## Misc ################    
    if "body sash: 0" in x:
        return [22,2,"cloth"];
    if "half apron: 0" in x:
        return [22,9,"cloth"];
    if "full apron: 0" in x:
        return [22,16,"cloth"];        
    if "oil cloth: 0" in x:
        return [22,23,"cloth"];   

 ######## FOOTWARE ################    
    if "sandals: 0" in x:
        return [29,2,"leather"];
    if "shoes: 0" in x:
        return [29,9,"leather"];
    if "boots: 0" in x:
        return [29,16,"leather"];        
    if "thigh boots: 0" in x:
        return [29,23,"leather"]; 
     
######## Leather ################          
    if "leather gorget: 0" in x:
        return [36,2,"leather"];
    if "leather cap: 0" in x:
        return [36,9,"leather"];
    if "leather gloves: 0" in x:
        return [36,16,"leather"];        
    if "leather sleeves: 0" in x:
        return [36,23,"leather"];        
    if "leather leggings: 0" in x:
        return [36,30,"leather"];          
    if "leather tunic: 0" in x:
        return [36,37,"leather"]; 

######## Studded Leather ################          
    if "studded gorget: 0" in x:
        return [43,2,"leather"];
    if "studded cap: 0" in x:
        return [43,9,"leather"];
    if "studded gloves: 0" in x:
        return [43,16,"leather"];        
    if "studded sleeves: 0" in x:
        return [43,23,"leather"];        
    if "studded leggings: 0" in x:
        return [43,30,"leather"];          
    if "studded tunic: 0" in x:
        return [43,37,"leather"];  

######## Female Leather ################          
    if "leather shorts: 0" in x:
        return [50,2,"leather"];
    if "leather skirt: 0" in x:
        return [50,9,"leather"];
    if "leather bustier: 0" in x:
        return [50,16,"leather"];        
    if "studded bustier: 0" in x:
        return [50,23,"leather"];        
    if "female leather armor: 0" in x:
        return [50,30,"leather"];          
    if "studded armor: 0" in x:
        return [50,37,"leather"];  

######## Bone Leather ################          
    if "bone helmet: 0" in x:
        return [57,2,"bone"];
    if "bone gloves: 0" in x:
        return [57,9,"bone"];
    if "bone arms: 0" in x:
        return [57,16,"bone"];        
    if "bone leggings: 0" in x:
        return [57,23,"bone"];        
    if "bone armor: 0" in x:
        return [57,30,"bone"];          
    if "orc helm: 0" in x:
        return [57,37,"bone"];  



def bagindexing():
    inventory = []
    for item in Player.Backpack.Contains: 
        inventory.append(item.Serial)
        Misc.Pause(5)
    return inventory    

def findnewitem(inv): #works but the string is weird if you print it. 
        for item in Player.Backpack.Contains:
            if item.Serial not in inv:
                return item.Serial



def craftitems(bod):
    
    count = 0
    bodarray = [0,0,0,0,0]
    checkbod = analsbod(bod) #grabs array of bod info 
    
    bodarray[0] = bod
    temp = catagorylogic(bodarray[0])

        
    while checkbod[3] == False: #checkbod[3] is true if full and false if not full
        
        bodarray [1] = temp[0]
        bodarray [2] = temp[1]
        bodarray [3] = temp[2] 
        bodarray [4] = checkbod[1]        
            
        worldSave()
        checktools()
        Player.HeadMessage(54, "Crafting Items")
        if str(bodarray[4]) == "barbed":
            material = barbedcolor
        elif str(bodarray[4]) == "spined":
            material = spinecolor
        elif str(bodarray[4]) == "horned":
            material = hornedcolor           
        else:
            material = -1
        
        setsemat(material)
        checkrestock(bodarray[3],material)

        inventory = bagindexing()        
        UseSewTool = Items.FindByID(sewtool, -1, Player.Backpack.Serial) 
        Items.UseItem(UseSewTool.Serial)
        Misc.Pause(250)    
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, bodarray[1])
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, bodarray[2])
        Misc.Pause(2000)  
        item = findnewitem(inventory)
        if item != None:
            Journal.Clear()
            Items.SingleClick(item)
            Misc.Pause(800)
            if Journal.Search("Exceptional"):
                Player.HeadMessage(54, "good")
                Items.UseItem(bodarray[0])
                Misc.Pause(750)
                Gumps.SendAction(1526454082, 2)
                Misc.Pause(750)
                Target.TargetExecute(item)
                Misc.Pause(750)
                count = count + 1
            else:
                Player.HeadMessage(54, "bad") 
                scissors = Items.FindByID(0x0F9F, -1, Player.Backpack.Serial)
                Items.UseItem(scissors.Serial)
                Misc.Pause(500)
                Target.TargetExecute(item)
                Misc.Pause(1000)
                if Journal.Search("Scissors cannot be used"):
                    Items.Move(item, trash, 0)
                    Misc.Pause(500)
        checkbod = analsbod(bod)
    unstock()
                    
                    
                    
                    
                    
 ########################################################################################        
 ########################################################################################       
 ########################################################################################
def grabbod():
        
        Items.UseItem(frombook)
        Misc.Pause(1000)
        Gumps.SendAction(1425364447, 5)
        Misc.Pause(1000)
        x = Items.FindByID(0x14EF, 0x0483, Player.Backpack.Serial)
        return x 


        
        
def sortnonmatch(bod): #sorts a bod that doesnt match an Lbod    

    sbod = catagorylogic(bod)
    if sbod[2] == "cloth":    
        craftitems(bod)
        Misc.Pause(500)
        while Items.FindByID(deed, -1, Player.Backpack.Serial):
            Items.UseItem(fullbod[0]) #open Chest
            Misc.Pause(600)
            Items.Move(fullbod[1],Player.Backpack.Serial, 0)
            Misc.Pause(600)
            Items.Move(bod, fullbod[1], 0) #store full bod in chest.
            Misc.Pause(600) 
            Items.Move(fullbod[1],fullbod[0], 0)
            Misc.Pause(600)
    elif sbod[2] == "bone":
        while Items.FindByID(deed, -1, Player.Backpack.Serial):
            Items.UseItem(nomatchstorage) #open Chest
            Misc.Pause(600)
            Items.Move(bonestorage,Player.Backpack.Serial, 0)
            Misc.Pause(600)
            Items.Move(bod, bonestorage, 0) #store full bod in chest.
            Misc.Pause(600) 
            Items.Move(bonestorage,nomatchstorage, 0)
            Misc.Pause(600)    
    elif sbod[2] == "leather":
        while Items.FindByID(deed, -1, Player.Backpack.Serial):
            Items.UseItem(nomatchstorage) #open Chest
            Misc.Pause(600)
            Items.Move(leatherstorage,Player.Backpack.Serial, 0)
            Misc.Pause(600)
            Items.Move(bod, leatherstorage, 0) #store full bod in chest.
            Misc.Pause(600) 
            Items.Move(leatherstorage,nomatchstorage, 0)
            Misc.Pause(600)                
            
            
            
    else:        
        Items.Move(bod, nomatchstorage, 0)
        Player.HeadMessage(54, "No lbod match moving to storage")
          
            
                
def comparebods(bod):
    Items.UseItem(lbodstorage)
    Misc.Pause(600)
    Items.UseItem(lbodstorage2)
    Misc.Pause(600)
    sbod = analsbod(bod)
    lbodstoragecontainer = Items.FindBySerial(lbodstorage)
    lbodstoragecontainer2 = Items.FindBySerial(lbodstorage2)
    Player.HeadMessage(54, "checking 1st container")
    for item in lbodstoragecontainer.Contains: 
        lbod = anallbod(item.Serial)
        if sbod[2] == lbod[2]: #qty 
            if sbod[1] == lbod[1] or lbod[1] == "cloth": #material                   
                for i in range(0, len(lbod)):
                    if str(sbod[4]) == str(lbod[i]):
                        Player.HeadMessage(54, "Mark 4")    
                        craftitems(bod) #fills sbod
                        Misc.Pause(600)
                        #adds it to lbod
                        Items.Move(item, Player.Backpack.Serial, 0)
                        Misc.Pause(600)
                        Items.UseItem(item)
                        Misc.Pause(600)
                        Gumps.SendAction(2703603018, 2)
                        Misc.Pause(600)
                        Target.TargetExecute(bod)
                        Misc.Pause(600)
                        
                        if lbod[1] == "spined" or lbod[1] == "barbed" or lbod[1] == "horned":
                            lbodqty=4
                        else: 
                            lbodqty = 3
                        
                        if len(lbod) == lbodqty:
                            Player.HeadMessage(54, "Lbod Full store in complete")
                            while Items.FindByID(deed, -1, Player.Backpack.Serial):
                                Items.UseItem(fullbod[0]) #open Chest
                                Misc.Pause(600)
                                Items.Move(fullbod[1],Player.Backpack.Serial, 0) #moves book to inventory
                                Misc.Pause(600)
                                Items.Move(item, fullbod[1], 0) #puts bod in book
                                Misc.Pause(600) 
                                Items.Move(fullbod[1],fullbod[0], 0)#store full bod in chest.
                                Misc.Pause(600) 
                                return
                               
                        else: #checks 2nd box
                               
                            Misc.Pause(1000)
                            Items.Move(item, lbodstorage, 0)
                            Misc.Pause(600)
                            return
                            
                        
                        
                        
                        
                            
    Player.HeadMessage(54, "checking 2nd container")
    for item in lbodstoragecontainer2.Contains: 
        lbod = anallbod(item.Serial)
        if sbod[2] == lbod[2]: #qty 
            if sbod[1] == lbod[1] or lbod[1] == "cloth": #material                   
                for i in range(0, len(lbod)):
                    if str(sbod[4]) == str(lbod[i]):
                        Player.HeadMessage(54, "Mark 4")    
                        craftitems(bod) #fills sbod
                        Misc.Pause(600)
                        #adds it to lbod
                        Items.Move(item, Player.Backpack.Serial, 0)
                        Misc.Pause(600)
                        Items.UseItem(item)
                        Misc.Pause(600)
                        Gumps.SendAction(2703603018, 2)
                        Misc.Pause(600)
                        Target.TargetExecute(bod)
                        Misc.Pause(600)
                        
                        if lbod[1] == "spined" or lbod[1] == "barbed" or lbod[1] == "horned":
                            lbodqty=4
                        else: 
                            lbodqty = 3
                        
                        if len(lbod) == lbodqty:
                            Player.HeadMessage(54, "Lbod Full store in complete")
                            while Items.FindByID(deed, -1, Player.Backpack.Serial):
                                Items.UseItem(fullbod[0]) #open Chest
                                Misc.Pause(600)
                                Items.Move(fullbod[1],Player.Backpack.Serial, 0) #moves book to inventory
                                Misc.Pause(600)
                                Items.Move(item, fullbod[1], 0) #puts bod in book
                                Misc.Pause(600) 
                                Items.Move(fullbod[1],fullbod[0], 0)#store full bod in chest.
                                Misc.Pause(600) 
                                return 
                        else: #checks 2nd box
                               
                            Misc.Pause(1000)
                            Items.Move(item, lbodstorage2, 0)
                            Misc.Pause(600)
                            return       
    




  
    


def anallbod(bod): #returns an array of info including only empty sbod info
    result = [0,0,0]
    bodList = Items.GetPropStringList(bod)        
    bodsize = len(bodList) 
    qtyarraynum = 6 #quantity in array slot 6 unless its spined/.barbed then we change to 7
    
    #Player.HeadMessage(54, bodsize) brints msg
      
    if bodList[4] == "small bulk order":
        result[0] = "small"
    else:
        result[0] = "large"
    
        
    if bodList[6].find("barbed")  == -1:
        if bodList[6].find("spined")  == -1:
                if bodList[6].find("horned")  == -1:
                    result[1] = "cloth"
                else:
                    result[1] = "horned"
                    qtyarraynum = 7
        else:
            result[1] = "spined"
            qtyarraynum = 7
        
    else:
        result[1] = "barbed"
        qtyarraynum = 7
    
    
    
        
    if bodList[qtyarraynum].find("20")  == -1:
        if bodList[qtyarraynum].find("15")  == -1:
            result[2] = 10
        else:
            result[2] = 15 
    else:
        result[2] = 20         
    if result[1] == "spined" or result[1] == "barbed" or result[1] == "horned":
        start = 8
    else:
        start = 7
    for i in range(start, bodsize):
        temp = bodList[i]
        #Player.HeadMessage(54, temp)
        #Player.HeadMessage(54, str(i))
        if temp.find(' 0') == -1:
            Misc.Pause(10)
        else:
            temp = temp.replace(":","")
            temp = temp.replace("20","")
            temp = temp.replace("15","")
            temp = temp.replace("10","")
            temp = temp.replace("0","")
            result.append(temp)
    
    return result    


def analsbod(bod):
    result = [0,0,0,0, 0,0,0] #added two zeros to deal with spined leather? 
    bodList = Items.GetPropStringList(bod)
    qtyarraynum = 6
    if bodList[4] == "small bulk order":
        result[0] = "small"
    else:
        result[0] = "large"
        
    if bodList[6].find("barbed")  == -1:
        if bodList[6].find("spined")  == -1:
                if bodList[6].find("horned")  == -1:
                    result[1] = "cloth"
                    fullcheck = 7
                else:
                    result[1] = "horned"
                    qtyarraynum = 7
                    fullcheck = 8
        else:
            result[1] = "spined"
            qtyarraynum = 7
            fullcheck = 8
        
    else:
        result[1] = "barbed"
        qtyarraynum = 7
        fullcheck = 8

        
    if bodList[qtyarraynum].find("20")  == -1:
        if bodList[qtyarraynum].find("15")  == -1:
            result[2] = 10
            
        else:
            result[2] = 15

    else:
        result[2] = 20

        
    if bodList[fullcheck].find(str(result[2]))  == -1:
        result[3] = False
    else:
        result[3] = True
        
    if result[1] == "spined" or result[1] == "barbed" or result[1] == "horned":
        start = 8
    else:
        start = 7    
    Misc.Pause(500)
    temp = bodList[start]
    temp = temp.replace(":","")
    temp = temp.replace("20","")
    temp = temp.replace("15","")
    temp = temp.replace("10","")
    temp = temp.replace("0","")

    result[4] = temp
    

    return result

def testingsmalloutput(bod):
    x = analsbod(bod) 
    Player.HeadMessage(54, str(x)) 
    Player.HeadMessage(54, 'we are making ' + str(x[0])) 
    Player.HeadMessage(54, 'it is ' + x[1]  ) 
    Player.HeadMessage(54, 'we need to make ' + str(x[2])  ) 
    Player.HeadMessage(54, 'is it full '+ str(x[3]) ) 
    Player.HeadMessage(54, 'we making '+ str(x[4]) ) 

def testlbodoutput(bod):
    zz = anallbod(bod)
    Player.HeadMessage(54, 'Mark One')
    Player.HeadMessage(54, str(len(zz)))
    for i in range(0, len(zz)):
        Player.HeadMessage(54, str(zz[i]))  
        
        
def getstringofbod(bod):
        result= ""
        bodList = Items.GetPropStringList(bod)
        for i in range(0, len(bodList)):
            result = result + bodList[i]
            
        result = result.replace("[","")
        result = result.replace("]","")
        result = result.replace("deedBlessed<BASEFONT COLOR=#204018>","")
        result = result.replace("(1155)<BASEFONT COLOR=#FFFFFF>","")
        result = result.replace("Hue: Rusty Green Weight: 1 stone","")
        result = result.replace("a bulk order","")
        result = result + '\n'
        return result
        
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
            
            



    
def main():

#initializing
    
    isautofill = False
    isgarbage = False
 
    x = Items.GetPropValue(frombook, "Deeds In Book:")
    for z in range(x): #runs all the items in the book
        Misc.Pause(500)
 
    
    #STEP 1: grab bod out of book
    
        Misc.Pause(1000) 
        bod = grabbod()
        Misc.Pause(2500)    
    #STEP 2: analyze for garbage 
        garbbodList = Items.GetPropStringList(bod)
        checkbod = analsbod(bod) #grabs array of bod info specifically for loop if its full sbod
        
        if comparetolist(bod, "garbo"):
            Player.HeadMessage(54, "Found garbage - dumping")
            Items.Move(bod, garbagebox, 0)
            Misc.Pause(1000)
            isgarbage = True
            
           
        elif str(garbbodList[5]) != "All items must be exceptional.":
            Player.HeadMessage(54, "Normal") 
            Items.Move(bod, garbagebox, 0)
            Misc.Pause(1000)
            isgarbage = True    

    #STEP 3: analyze for autocraft   
        
        elif checkbod[3] == True:
            Player.HeadMessage(54, "BODZ FULL LOOKING FOR LBOD")
            comparebods(bod)
            while Items.FindByID(deed, -1, Player.Backpack.Serial):
                Items.UseItem(fullbod[0]) #open Chest
                Misc.Pause(800)
                Items.Move(fullbod[1],Player.Backpack.Serial, 0)
                Misc.Pause(800)
                Items.Move(bod, fullbod[1], 0) #store full bod in chest.
                Misc.Pause(800) 
                Items.Move(fullbod[1],fullbod[0], 0)
                Misc.Pause(800) 
            
        elif comparetolist(bod, "autofill"):
            Player.HeadMessage(54, "Found autofill - filling")
            craftitems(bod)
            Misc.Pause(500)
            while Items.FindByID(deed, -1, Player.Backpack.Serial):
                Items.UseItem(fullbod[0]) #open Chest
                Misc.Pause(600)
                Items.Move(fullbod[1],Player.Backpack.Serial, 0)
                Misc.Pause(600)
                Items.Move(bod, fullbod[1], 0) #store full bod in chest.
                Misc.Pause(600) 
                Items.Move(fullbod[1],fullbod[0], 0)
                Misc.Pause(600) 
            isautofill = True    
    
    
    
    
    #STEP 3: is it small or large
        else:
            x = analsbod(bod)
            if str(x[0]) == "small":
                comparebods(bod)
            else:
                Player.HeadMessage(54, 'found large')
                Items.Move(bod, lbodstorage, 0)
                Misc.Pause(600)

    #Step 4: What do we do if no match?
        Misc.Pause(1000)
        if Items.FindByID(deed, -1, Player.Backpack.Serial):            
            sortnonmatch(bod)    

checktools()            
main()    


#testlbodoutput(0x450C4341)



#testlbodoutput(0x44FBDC4C)

#testingsmalloutput(0x45044849)
