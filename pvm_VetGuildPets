# This script relys on Bandage_Timer.py, if you do not have it, it will not work
# Bandages any guilded pet if within 1 tile
from System.Collections.Generic import List
from System import Byte
import sys

def find(notoriety):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = 1.5
    fil.IsHuman = False
    fil.IsGhost = False
    fil.Notorieties = List[Byte](bytes([notoriety]))
    list = Mobiles.ApplyFilter(fil)

    return list
    
# quits if you have less than 80 HP
if Player.GetRealSkillValue('Veterinary') < 80:
    Stop
    
healing = None
while True:
    petList = find(2)
    init = 0
    plist = []
    for i in petList:
        healPet = Mobiles.FindBySerial(i.Serial)
        if healPet:
            if healPet.Hits != 0 and Player.InRangeMobile(healPet, 1.5):
                plist.append(healPet.Serial)
    for j in plist:
        if init == 0:
            healing = Mobiles.FindBySerial(j)
            init = 1
        healPet = Mobiles.FindBySerial(j)
        if healPet:
            if healPet.Hits <= healing.Hits or healPet.Poisoned:
                healing = Mobiles.FindBySerial(healPet.Serial)
    if healing:
        pet2Heal = Mobiles.FindBySerial(healing.Serial)
        if pet2Heal:
            if (pet2Heal.Hits < 23 or pet2Heal.Poisoned) and Player.InRangeMobile(pet2Heal, 1.5):
                if Misc.ReadSharedValue('bandageDone') == True and Player.Visible:
                    if Target.HasTarget( ) == False:
                        Misc.SendMessage("Healing " + pet2Heal.Name, 33)  
                        Items.UseItemByID(0x0E21, -1)
                        Target.WaitForTarget(1500)
                        Target.TargetExecute(pet2Heal)
                        Misc.Pause(600)
    
    Misc.Pause(10)
