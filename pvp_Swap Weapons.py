# Weapon Swapper by Matsamilla
# Swaps between weps you target, last wep targeted will be first equiped

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
if Misc.CheckSharedValue(Player.Name + 'mainWeplist') == False:
    mainWeplist = setWeps("Target Weps, then cancel target.")
    Misc.SetSharedValue(Player.Name + 'mainWeplist', mainWeplist)
    Misc.Pause(600)

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
currentWep = len(weplist) -1

# equip next wep in list
Player.EquipItem(weplist[currentWep])

# delete last equipt wep from temp list
weplist.pop()
if not weplist:
    Misc.RemoveSharedValue(Player.Name + 'weplist')
else:
    weplist = Misc.ReadSharedValue(Player.Name + 'weplist')
