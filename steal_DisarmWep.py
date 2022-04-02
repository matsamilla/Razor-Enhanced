# disarm steal wep by MatsaMilla
# updated 4/2/2022
# have fun


Player.HeadMessage(66, "Select your Target")
disarmTarget = Mobiles.FindBySerial(Target.PromptTarget())

def stealCheck():
    Misc.Pause(120)
    if Journal.SearchByType( 'You fail to steal the item.' , 'Regular' ):
        Player.HeadMessage(33, 'FAILED')
    elif Journal.SearchByType( 'You successfully steal the item.' , 'Regular' ):
        Player.HeadMessage(66, 'Wep Stolen!')

if disarmTarget:
    
    rightHand = disarmTarget.GetItemOnLayer('RightHand')
    leftHand = disarmTarget.GetItemOnLayer('LeftHand')
    
    if righHand:
        stealTarget = rightHand
    
    elif leftHand:
        stealTarget = leftHand
        
    else:
        Player.HeadMessage(66, "They are unarmed")
        stealTarget = None
        
    if stealTarget != None:
        
        Journal.Clear()
        Player.WeaponDisarmSA( )
        Misc.Pause(120)

        if Journal.Search("You decide to not try to stun anyone."):
            Player.WeaponDisarmSA( )

        while Player.DistanceTo(disarmTarget) > 1:
            Misc.Pause(10)

        Player.Attack(disarmTarget)
        if not Target.HasTarget():
            Player.UseSkill('Stealing')
        Target.WaitForTarget(1500)
        Target.TargetExecute(stealTarget)
            
        stealCheck()
    
else:
    Player.HeadMessage(66, "You didn't target a mobile")
        

        