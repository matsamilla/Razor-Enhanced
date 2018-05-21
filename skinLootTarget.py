#standard imports
import sys
from System.Collections.Generic import List


#global types
#generic
self_pack = Player.Backpack.Serial
##Types
corpse = 0x2006
uncutleather = 0x1079
scalesType = 0x26B4
scissorsType = 0x0F9F

##lists
bladeList = [0xf52, 0xec4, 0x13f6, 0xec3]
leathersList = List[int]((0x1081))

# Helper Functions
###################################
def getByItemID(itemid, source):
    #find an item id in container serial
    for item in Items.FindBySerial(source).Contains:
        if item.ItemID == itemid:
            return item
        else:
            Misc.NoOperation()
###################################

#create target to get corpse object
def skinLoot():
    Misc.SendMessage('Skin-Loot')
#use blade in backpack to cut corpse object
#open corpse object
#move list of items to backpack
#move ist of items to ground
#use scissors on items


def getBlade():
    for item in bladeList:
        blade = getByItemID(item, self_pack)
        if blade is not None:
            return blade
            
def getLeatherFromGround():
    leatherFilter = Items.Filter()
    leatherFilter.Enabled = True
    leatherFilter.OnGround = True
    leatherFilter.Movable = True
    leatherFilter.Graphics = leathersList
    leatherFilter.RangeMax = 2
    
    leathers = Items.ApplyFilter(leatherFilter)
    Misc.SendMessage
    for leather in leathers:
        Items.Move(leather.Serial, self_pack, 100)
        Misc.Pause(700)

def skinLoot():
    corpse = Items.FindBySerial(Target.PromptTarget())
    if corpse:
        Items.UseItem(corpse)
        Misc.Pause(550)
        for item in bladeList:
            blade = getBlade()
        if blade is not None:
            Items.UseItem(blade)
            Target.WaitForTarget(3000, True)
            Target.TargetExecute(corpse)
            Misc.Pause(1000)
        else:
            Misc.SendMessage('No Blades Found')
            sys.exit()
    else:
        sys.exit()
        
    leather = getByItemID(uncutleather, corpse.Serial)
    scales = getByItemID(scalesType, corpse.Serial)
    
    if scales is not None:
        Items.Move(scales, self_pack, 0)
        Misc.Pause(550)
        
    if leather is not None:
        Items.MoveOnGround(leather, 0, Player.Position.X + 1, Player.Position.Y + 1, Player.Position.Z)
        Misc.Pause(550)
        scissors = getByItemID(scissorsType, self_pack)
        if scissors is not None:
            Items.UseItem(scissors)
            Target.WaitForTarget(3000, True)
            Target.TargetExecute(leather)
            Misc.Pause(700)
        else:
            Misc.SendMessage('No Scissors Found')
            sys.exit()
            
        getLeatherFromGround()
        
skinLoot()
        