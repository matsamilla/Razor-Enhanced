# Weapon Swapper by Matsamilla
# Swaps between weps you target, last targeted is first equipted

# Version 1.3: fixed error not reading shared value, and fixed if weps not found

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
                       return list
                   else:
                       return list
        else:
            chosenid = Target.PromptTarget()
            if chosenid > -1:
               chosen = Items.FindBySerial(chosenid)
               Misc.Pause(500)
               Misc.SendMessage("Chose {}".format(chosen.Name))
               return chosenid

# check to see if weps are saved
def checkList():
    global mainWeplist
    if Misc.CheckSharedValue(Player.Name + 'mainWeplist') == False:
        mainWeplist = setWeps("Target Weps, then cancel target.")
        Misc.SetSharedValue(Player.Name + 'mainWeplist', mainWeplist)
        Misc.Pause(600)
    else:
        mainWeplist = Misc.ReadSharedValue(Player.Name + 'mainWeplist')

checkList()
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
