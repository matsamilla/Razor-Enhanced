# Weapon Swapper by Matsamilla
# Swaps between weps you target, last targeted is first equipted
# if only one weapon targeted, acts as a wep toggle.

# Version 3.0: Works better with 1 handed & shields

leftHand = Player.GetItemOnLayer('LeftHand')
rightHand = Player.GetItemOnLayer('RightHand')
twoHandedWeps = [ 0x0F4D,0x143E,0x0F4B,0x0F49,0x13FB,0x0F43,0x0F45,0x1443,0x0F43,0x0F62,0x1403,0x1439,0x0E89,0x13F8,0x0DF0,0x0E81,0x13B2,0x26C2,0x0F50,0x13FD ]
shields = [ 0x1B76,0x1B74,0x1B7B,0x1B73,0x1B72,0x1B79,0x1B7A ]

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

    # get last list position
    lastPos = len(weplist) -1

    # equip next wep in list
    #currentWep = Items.FindBySerial(currentWep)
    
    wep = Items.FindBySerial(weplist[lastPos])
    
    if wep.ItemID in twoHandedWeps:
        Misc.SendMessage('Two Handed')
        if rightHand:
            Items.Move(rightHand.Serial,Player.Backpack.Serial,0)
            Misc.Pause(600)
        if leftHand:
            Items.Move(leftHand.Serial,Player.Backpack.Serial,0)
            Misc.Pause(600)
            Player.EquipItem(wep)
        else:
            Player.EquipItem(wep)
            
    elif wep.ItemID in shields:
        Misc.SendMessage('Shield')
        if leftHand:
            if leftHand.Serial == wep.Serial:
                Items.Move(wep,Player.Backpack.Serial,0)
            else:
                Items.Move(leftHand.Serial,Player.Backpack.Serial,0)
                Misc.Pause(600)
                Player.EquipItem(wep)
        else:
            Player.EquipItem(wep) 
        
        
    else:
        if rightHand:
            Misc.SendMessage('disarming right')
            Items.Move(rightHand,Player.Backpack.Serial,0)
            Misc.Pause(600)
            Player.EquipItem(wep)
            # delete last equipt wep from temp list
            weplist.pop()
            if not weplist:
                Misc.RemoveSharedValue(Player.Name + 'weplist')
            else:
                weplist = Misc.ReadSharedValue(Player.Name + 'weplist')
            return
                
        if leftHand:
            Misc.SendMessage('disarming left')
            if leftHand.ItemID in shields:
                Player.EquipItem(wep)
                
            else:                
                Items.Move(leftHand,Player.Backpack.Serial,0)
                Misc.Pause(600)
                Player.EquipItem(wep)
        
        else:
            Player.EquipItem(wep)

    # delete last equipt wep from temp list
    weplist.pop()
    if not weplist:
        Misc.RemoveSharedValue(Player.Name + 'weplist')
    else:
        weplist = Misc.ReadSharedValue(Player.Name + 'weplist')
        
def toggleWep():
    if wep.ItemID in twoHandedWeps:
        Misc.SendMessage('Two Handed')
        if rightHand:
            Items.Move(rightHand.Serial,Player.Backpack.Serial,0)
            Misc.Pause(600)
        if leftHand:
            if leftHand.Serial == wep.Serial:
                Items.Move(wep,Player.Backpack.Serial,0)
                Misc.Pause(600)
            else:
                Items.Move(leftHand.Serial,Player.Backpack.Serial,0)
                Misc.Pause(600)
                Player.EquipItem(wep)
        else:
            Player.EquipItem(wep)
            
    elif wep.ItemID in shields:
        Misc.SendMessage('Shield')
        if leftHand:
            if leftHand.Serial == wep.Serial:
                Items.Move(wep,Player.Backpack.Serial,0)
            else:
                Items.Move(leftHand.Serial,Player.Backpack.Serial,0)
                Misc.Pause(600)
                Player.EquipItem(wep)
        else:
            Player.EquipItem(wep) 
        
        
    else:
        if rightHand:
            if rightHand.Serial == wep.Serial:
                Items.Move(wep,Player.Backpack.Serial,0)
                return
                
        if leftHand:
            if leftHand.Serial == wep.Serial:
                Items.Move(wep,Player.Backpack.Serial,0)
                return
            elif leftHand.ItemID in shields:
                Player.EquipItem(wep)
        
        else:
            Player.EquipItem(wep)
        
# check to see if weps are saved
def checkList():
    global mainWeplist
    global wep
    if Misc.CheckSharedValue(Player.Name + 'singlewep'):
        tempwep = Items.FindBySerial(Misc.ReadSharedValue(Player.Name + 'singlewep'))
        if tempwep:
            wep = tempwep
        else:
            Misc.RemoveSharedValue(Player.Name + 'singlewep')
            checkList()
            
    elif Misc.CheckSharedValue(Player.Name + 'mainWeplist') == False:
        mainWeplist = setWeps("Target Wep(s), then cancel target.")
        if isinstance(mainWeplist, list):
            Misc.SetSharedValue(Player.Name + 'mainWeplist', mainWeplist)
        else:
            Misc.SetSharedValue(Player.Name + 'singlewep', mainWeplist.Serial)
            wep = mainWeplist
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
