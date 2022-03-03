# Dexxer trainer by MatsaMilla
# Will train Healing , Anatomy, Hiding & Alchemy
dummy = None
dragTime = 600
        
bows = [0x13B2,0x26C2,0x0F50,0x13FD]
leftHand = Player.GetItemOnLayer('LeftHand')

import sys
def trainingDummy():
    global dummy
    training = Target.PromptTarget("Target training dummy")
    dummy = Mobiles.FindBySerial(training)

def kegPots():
    if Journal.Search('hold any more'):
        Misc.SendMessage('Empty Keg!!')
        sys.exit()
    
    keg = Items.FindByID(0x1940,-1,Player.Backpack.Serial)
    tr = Items.FindByID(0xf0b,-1,Player.Backpack.Serial)
    ga = Items.FindByID(0xf08 ,-1,Player.Backpack.Serial)
    gs = Items.FindByID(0xf09 ,-1,Player.Backpack.Serial)
    gh = Items.FindByID(0xf0c ,-1,Player.Backpack.Serial)
    gc = Items.FindByID(0xf07 ,-1,Player.Backpack.Serial)
    
    if tr:
        Items.Move(tr, keg, 0)
        Misc.Pause(dragTime)
    elif ga:
        Items.Move(ga, keg, 0)
        Misc.Pause(dragTime)
    elif gs:
        Items.Move(gs, keg, 0)
        Misc.Pause(dragTime)
    elif gh:
        Items.Move(gh, keg, 0)
        Misc.Pause(dragTime)
    elif gc:
        Items.Move(gc, keg, 0)
        Misc.Pause(dragTime)
        
def trainAlchy():
    if Player.GetRealSkillValue('Alchemy') < 100:
        
        if Player.GetRealSkillValue('Alchemy') < 60:
            mortar = Items.FindByID(0x0E9B , -1 , Player.Backpack.Serial)
            Items.UseItem(mortar)
            Gumps.WaitForGump(0x38920abd, 1500)
            Gumps.SendAction(0x38920abd ,1)
            Gumps.WaitForGump(0x38920abd, 1500)
            Gumps.SendAction(0x38920abd ,9)
            Gumps.WaitForGump(0x38920abd, 1500)
            
            kegPots()
        
        elif Player.GetRealSkillValue('Alchemy') < 70:
            mortar = Items.FindByID(0x0E9B , -1 , Player.Backpack.Serial)
            Items.UseItem(mortar)
            Gumps.WaitForGump(0x38920abd, 1500)
            Gumps.SendAction(0x38920abd ,8)
            Gumps.WaitForGump(0x38920abd, 1500)
            Gumps.SendAction(0x38920abd ,9)
            Gumps.WaitForGump(0x38920abd, 1500)
            
            kegPots()
            
        elif Player.GetRealSkillValue('Alchemy') < 80:
            mortar = Items.FindByID(0x0E9B , -1 , Player.Backpack.Serial)
            Items.UseItem(mortar)
            Gumps.WaitForGump(0x38920abd, 1500)
            Gumps.SendAction(0x38920abd ,29)
            Gumps.WaitForGump(0x38920abd, 1500)
            Gumps.SendAction(0x38920abd ,9)
            Gumps.WaitForGump(0x38920abd, 1500)
            
            kegPots()
        
        elif Player.GetRealSkillValue('Alchemy') < 90:
            mortar = Items.FindByID(0x0E9B , -1 , Player.Backpack.Serial)
            Items.UseItem(mortar)
            Gumps.WaitForGump(0x38920abd, 1500)
            Gumps.SendAction(0x38920abd ,22)
            Gumps.WaitForGump(0x38920abd, 1500)
            Gumps.SendAction(0x38920abd ,9)
            Gumps.WaitForGump(0x38920abd, 1500)
            
            kegPots()
            
        elif Player.GetRealSkillValue('Alchemy') < 100:
            mortar = Items.FindByID(0x0E9B , -1 , Player.Backpack.Serial)
            Items.UseItem(mortar)
            Gumps.WaitForGump(0x38920abd, 1500)
            Gumps.SendAction(0x38920abd ,43)
            Gumps.WaitForGump(0x38920abd, 1500)
            Gumps.SendAction(0x38920abd ,9)
            Gumps.WaitForGump(0x38920abd, 3500)
            
            kegPots()

            
def trainHide():
    if not Timer.Check('hideTimer'):
        Player.UseSkill('Hiding')
        Timer.Create('hideTimer', 11000)
    elif Player.GetRealSkillValue('Hiding') == 100:
        if not Player.BuffsExist('Hidden'):
            Player.UseSkill('Hiding')
        
def trainHealing():
    if dummy == None:
        trainingDummy()
    if (Journal.Search('resurrect your patient.') or not Timer.Check('bandie')):
        Journal.Clear()
        bandage = Items.FindByID(0x0E21,-1,Player.Backpack.Serial)
        Items.UseItem(bandage)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(dummy)
        Timer.Create('bandie', 11000)
        
def trainResist():
    if dummy == None:
        trainingDummy()
    if not Timer.Check ('casttime')and Player.DistanceTo(dummy) < 12:
        Spells.CastMagery("Mana Vampire")
        Target.WaitForTarget(1500, False)
        Target.TargetExecute(dummy)
        Timer.Create('casttime', 3000)
    
    Player.SetWarMode(False)

def equipBow():
    #Misc.Pause( config.dragDelayMilliseconds )
    if Player.GetRealSkillValue('Archery') > 80:
        player_bag = Items.FindBySerial(Player.Backpack.Serial)
        if not leftHand:
            for i in player_bag.Contains:
                if i.ItemID in bows:
                    Player.EquipItem(i.Serial)
                    Misc.Pause( 600 )
                    
def trainAnat():
    if dummy == None:
        trainingDummy()
    if Timer.Check('anat') == False:
        Player.UseSkill('Anatomy')
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(dummy)
        Timer.Create('anat', 5000)
        
def attkHealTarget():
    if dummy == None:
        trainingDummy()
    if dummy.Hits < 25 and Misc.ReadSharedValue('bandageDone') == True:
        Items.UseItemByID(0x0E21, 0)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(dummy)
        Misc.Pause (500)
    if dummy.Hits < 10:
        Player.SetWarMode(False)
        while dummy.Hits < 25:
            Misc.Pause(100)
        Player.SetWarMode(True)
        Player.Attack(dummy)
        
def BandageSelf():
    if Misc.ReadSharedValue('bandageDone') == True:
        Items.UseItemByID(0x0E21, 0)
        Target.WaitForTarget(1500, False)
        Target.Self()
        Misc.Pause (500)
        
Journal.Clear()
while True:
    if Player.GetRealSkillValue('Healing') > 30 and (Player.Hits < 50 or Player.Poisoned):
        BandageSelf()
    if Player.GetRealSkillValue('Anatomy') > 30 and Player.GetRealSkillValue('Anatomy') < 100:
        trainAnat()
    if Player.GetRealSkillValue('Hiding') > 30 and Player.GetRealSkillValue('Hiding') < 100:
        trainHide()
    if Player.GetRealSkillValue('Healing') > 30 and Player.GetRealSkillValue('Healing') < 100:
        trainHealing()
    if Player.GetRealSkillValue('Alchemy') > 30 and Player.GetRealSkillValue('Alchemy') < 100:
        trainAlchy()
    
    Misc.Pause(100)
    if Target.HasTarget( ) == True:
        Target.Cancel()
