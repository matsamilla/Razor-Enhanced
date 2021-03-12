# Weapon Swapper by Matsamilla
# Swaps between weps you target, last targeted is first equipted
# if only one weapon targeted, acts as a wep toggle.

# Version 2.0: Now will toggle wep if only one targeted.

leftHand = Player.GetItemOnLayer('LeftHand')
rightHand = Player.GetItemOnLayer('RightHand')

def setWeps(text, multiple=True):
    Player.HeadMessage(76,text)
    list = []
    if multiple: 
        while multiple:
            chosenid = Target.PromptTarget()
            if chosenid > -1:
               chosen = Items.FindBySerial(chosenid)
               Misc.Pause(500)
               list.append(chosen.Serial)
            else:
               multiple = False
               if len(list) == 1:
                   return chosen
               else:
                   return list
    else:
        chosenid = Target.PromptTarget()
        if chosenid > -1:
           chosen = Items.FindBySerial(chosenid)
           Misc.Pause(500)
           Misc.SendMessage("Chose {}".format(chosen.Name))
           return chosenid
               
def swampWeps():
    for i in mainWeplist:
        if Items.FindBySerial(i) == None:
            Player.HeadMessage(33, 'Set New Weps')
            Misc.RemoveSharedValue(Player.Name + 'weplist')
            Misc.RemoveSharedValue(Player.Name + 'mainWeplist')
            checkList()
            break
        
    # set weps to temp list
    if Misc.CheckSharedValue(Player.Name + 'weplist'):
        weplist = Misc.ReadSharedValue(Player.Name + 'weplist')
    else:
        weplist =[]
        for i in mainWeplist:
            weplist.append(i)
        Misc.SetSharedValue(Player.Name + 'weplist', weplist)
        
    # clear hands
    if rightHand:
        Items.Move(rightHand,Player.Backpack.Serial,0)
        Misc.Pause(600)
            
    if leftHand:
        Items.Move(leftHand,Player.Backpack.Serial,0)
        Misc.Pause(600)

    # get last list position
    lastPos = len(weplist) -1

    # equip next wep in list
    #currentWep = Items.FindBySerial(currentWep)
    Player.EquipItem(weplist[lastPos])

    # delete last equipt wep from temp list
    weplist.pop()
    if not weplist:
        Misc.RemoveSharedValue(Player.Name + 'weplist')
    else:
        weplist = Misc.ReadSharedValue(Player.Name + 'weplist')
        
def toggleWep():
    if rightHand:
        if rightHand.Serial == wep:
            Items.Move(wep,Player.Backpack.Serial,0)
            return
#        else:
#            Items.Move(rightHand.Serial,Player.Backpack.Serial,0)
#            Misc.Pause(600)
#            Player.EquipItem(wep)
#            return
                
    if leftHand:
        if leftHand.Serial == wep:
            Items.Move(wep,Player.Backpack.Serial,0)
            return
        else:
            Items.Move(leftHand.Serial,Player.Backpack.Serial,0)
            Misc.Pause(600)
            Player.EquipItem(wep)
            return
    else:
        Player.EquipItem(wep)
        
# check to see if weps are saved
def checkList():
    global mainWeplist
    global wep
    if Misc.CheckSharedValue(Player.Name + 'singlewep'):
        tempwep = Items.FindBySerial(Misc.ReadSharedValue(Player.Name + 'singlewep'))
        if tempwep:
            wep = tempwep.Serial
        else:
            Misc.RemoveSharedValue(Player.Name + 'singlewep')
            checkList()
            
    elif Misc.CheckSharedValue(Player.Name + 'mainWeplist') == False:
        mainWeplist = setWeps("Target Wep(s), then cancel target.")
        if isinstance(mainWeplist, list):
            Misc.SetSharedValue(Player.Name + 'mainWeplist', mainWeplist)
        else:
            Misc.SetSharedValue(Player.Name + 'singlewep', mainWeplist.Serial)
            wep = mainWeplist.Serial
        Misc.Pause(600)
    else:
        mainWeplist = Misc.ReadSharedValue(Player.Name + 'mainWeplist')

try:
    checkList()

    if isinstance(mainWeplist, list):
        Misc.SendMessage('Swap Wep', 33)
        swampWeps()
    else:
        Misc.SendMessage('Toggle Wep', 33)
        toggleWep()
except:
    Misc.RemoveSharedValue(Player.Name + 'mainWeplist')
    Misc.RemoveSharedValue(Player.Name + 'singlewep')
    Misc.RemoveSharedValue(Player.Name + 'weplist')
    Player.HeadMessage(33, 'Something went wrong, reset weps')
