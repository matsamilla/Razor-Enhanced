# Use this to cast Mana Vampire on someone (or yourself) until you run out of regs.
# By MatsaMilla

#----------------------------------------------------

training = Target.PromptTarget("Target training dummy")
dummy = Mobiles.FindBySerial(training)

bows = [0x13B2,0x26C2,0x0F50,0x13FD]
leftHand = Player.GetItemOnLayer('LeftHand')
def equipBow():
    #Misc.Pause( config.dragDelayMilliseconds )
    if Player.GetRealSkillValue('Archery') > 80:
        player_bag = Items.FindBySerial(Player.Backpack.Serial)
        if not leftHand:
            for i in player_bag.Contains:
                if i.ItemID in bows:
                    Player.EquipItem(i.Serial)
                    Misc.Pause( 600 )

while True:
    dummy = Mobiles.FindBySerial(training)
    if Player.DistanceTo(dummy) < 12:
        Player.SetWarMode(False)
        Spells.CastMagery("Mana Vampire")
        Target.WaitForTarget(1500, False)
        Target.TargetExecute(dummy)
        Player.SetWarMode(True)
        Player.SetWarMode(False)
        Misc.Pause(2500)
    
    Player.SetWarMode(False)
    
    if Player.Mana < 40:
        Player.UseSkill('Meditation')
        while Player.Mana < Player.ManaMax:
            
            if not Player.BuffsExist('Meditation') and Timer.Check('med') == False:
                Misc.Pause(2000)
                Player.UseSkill('Meditation')
                Timer.Create('med', 7000)
            Misc.Pause(100)
                
    if Items.BackpackCount( 0x0F8D, -1) < 1:
        Stop
    if Journal.Search('Did it, got it') == 50:
        Stop
            