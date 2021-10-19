def writeautofill(x):
    f = open('C:/Users/Jason/PycharmProjects/BodBot/smithautofill.txt', 'a')        
    f.write(str(x))
    f.close()   
def writegarbo(x):
    f = open('C:/Users/Jason/PycharmProjects/BodBot/smithgarbo.txt', 'a')        
    f.write(str(x))
    f.close()   
def stringtest(x):
    bodList = Items.GetPropStringList(x)
    f = open('C:/Users/Jason/PycharmProjects/BodBot/test.txt', 'a')        
    f.write(str(bodList))
    f.close()  
    
    
    
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
        

               
def comparetolist(input):
    filepath = 'C:/Users/Jason/PycharmProjects/BodBot/' + input + ".txt"
    f = open(filepath, 'r')        
    allinlist = f.readlines()
    f.close()
  
    #Player.HeadMessage(54, str(len(allinlist)))
    for i in range(0, len(allinlist)):
        #Player.HeadMessage(54, str(allinlist[i]))
        #Player.HeadMessage(54, str(getstringofbod(0x44D90146)))
        if getstringofbod(0x44D90146) == allinlist[i]:
            Player.HeadMessage(54, "yes")
        else:
            Player.HeadMessage(54, "No")

            #writeautofill(getstringofbod(0x444785C5))    

#bod = 0x47842EEF    #lbod        
#bod = 0x479CFE6D
#bod = 0x47079787 #femail plate
bod = Target.PromptTarget("select bod to trash")
#bod =0x41104ADC
#writeautofill(getstringofbod(bod)) #adds to autofill
writegarbo(getstringofbod(bod)) #adds to garbo list
#stringtest(bod) #prints raw string to test.txt

    
    