setTarget = Mobiles.FindBySerial( Target.PromptTarget() )
msgColor = 1

if setTarget:
    Target.SetLast(setTarget.Serial)
    Player.ChatParty('Changing last target to ' + setTarget.Name)
    if setTarget.Notoriety == 1:
        msgColor = 1266 #blue
    elif setTarget.Notoriety == 2:
        msgColor = 77 #green
    elif setTarget.Notoriety == 3 or setTarget.Notoriety == 4:
        msgColor = 902 #grey
    elif setTarget.Notoriety == 5:
        msgColor = 47 #orange
    elif setTarget.Notoriety == 6:
        msgColor = 33 #red
    Mobiles.Message( setTarget, 15 , '*Target*' )
    Player.HeadMessage( msgColor , 'Target: ' + setTarget.Name )