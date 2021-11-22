# Explode pot 1 key executer.
# hit once to arm
# hit again to toss at last target

# true to cancel target after arming
cancelTarget = False

msgcolor = 53
fakeTarget = 0x00000
lastTarget = Target.GetLast()

import sys
            
def potArmOrThrow():
    # tosses pot if has been charging
    if Timer.Check( 'ex' + Player.Name ) == True:
        Player.HeadMessage( msgcolor, 'Tossing' )
        usePot()
        Target.WaitForTarget(1500)
        Target.TargetExecute(lastTarget)
        Timer.Create( 'ex' + Player.Name , 1)

    # starts charging pot 
    else:
        usePot()
        Timer.Create( 'ex' + Player.Name , 4500)
        if cancelTarget:
            Target.Cancel()
    
def usePot():
    if Misc.ShardName() == "Ultima Forever":
        drinkPot()
    else:
        usePotType()
    
def drinkPot():
    Player.ChatSay(msgcolor, '[drink GreaterExplosionPotion')
    Misc.Pause(120)
    if Journal.Search( 'You do not have any of those potions.'):
        Player.HeadMessage(msgcolor, 'Out of Exp Pots')
        sys.exit()
    elif Journal.Search('You must wait a moment before using another explosion potion'):
        Misc.NoOperation()
        
def usePotType():
    pot = Items.FindByID(0x0F0D,0,Player.Backpack.Serial,True)
    if pot:
        Items.UseItem(pot)
    else:
        Player.HeadMessage(33, "No Explode pots!")

Journal.Clear()
potArmOrThrow()
