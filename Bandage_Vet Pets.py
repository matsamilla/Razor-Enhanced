# Pet Vet by Matsamilla, updated 4/19/21
# This script relys on Bandage_Timer.py, if you do not have it, it will not work
# Add the serials of pets you want to heal to the petList
from System.Collections.Generic import List
from System import Byte
import sys

#Pet list you can add to it by putting the pets Serial number in the list. 
petList = [
# PetList
 0x00120786,# Winged Snek
 0x003FAA39,# Kuzco
 0x00049A23,# Water Wyrm
 0x0016D74B,# Pacha
 0x001BF91B, # Matsa- Mare
]

# quits if you have less than 80 HP
if Player.GetRealSkillValue('Veterinary') < 80:
    Misc.SendMessage('Not enough vet skill, stopping',33)
    sys.exit()
    
healing = None
while True:
    init = 0
    plist = []
    for i in petList:
        healPet = Mobiles.FindBySerial(i)
        if healPet:
            if healPet.Hits != 0 and Player.InRangeMobile(healPet, 1.5) and healPet.Body not in broodlings:
                plist.append(healPet.Serial)
    for j in plist:
        if init == 0:
            healing = Mobiles.FindBySerial(j)
            init = 1
        healPet = Mobiles.FindBySerial(j)
        if healPet:
            if healPet.Hits <= healing.Hits or healPet.Poisoned:
                Misc.SendMessage(healPet.Name)
                healing = Mobiles.FindBySerial(healPet.Serial)
    if healing:
        pet2Heal = Mobiles.FindBySerial(healing.Serial)
        if pet2Heal:
            if (pet2Heal.Hits < 23 or pet2Heal.Poisoned) and Player.InRangeMobile(pet2Heal, 1.5):
                if Misc.ReadSharedValue('bandageDone') == True and Player.Visible:
                    prevTarget = Target.Last()
                    if Target.HasTarget( ) == False:
                        Misc.SendMessage("Healing " + pet2Heal.Name, 33)  
                        Items.UseItemByID(0x0E21, -1)
                        Target.WaitForTarget(1500)
                        Target.TargetExecute(pet2Heal)
                        Misc.Pause(600)
    
    Misc.Pause(10)
