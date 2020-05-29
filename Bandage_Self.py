# Bandage Timer by Wardoc
# Contributions by Matsamilla
# last updated 5/29/20 - added overhead message option
# I have this always running, start at login.

# True for overhead Bandage messages, false for in system messages
overheadMessage = False



msgcolor = 88
Misc.SetSharedValue('bandageDone', True)
def BandagesApplying():
    # Fetch the Journal entries (oldest to newest)
    regularText = Journal.GetTextByType( 'Regular' )

    # Reverse the Journal entries so that we read from newest to oldest
    regularText.Reverse()

    # Read back until the bandages were started to see if they have finished applying
    for line in regularText[ 0 : len( regularText ) ]:
        if (line == 'You begin applying the bandages.' or
                line == 'Your hands are still busy applying other bandages.'):
            break
        if ( line == 'You finish applying the bandages.' or
                line == 'You heal what little damage your patient had.' or
                line == 'You apply the bandages, but they barely help.' or
                line == 'That being is not damaged!' or
                line == 'You have cured the target of all poisons!' or
                line == 'You are unable to resurrect your patient.' or 
                line == 'You are able to resurrect your patient' or
                line == 'You are able to resurrect the creature.' or
                line == 'You fail to resurrect the creature.' or
                line == 'You did not stay close enough to heal your patient!'):
            return False
    return True


def WaitForBandagesToApply():
    Misc.SetSharedValue('bandageDone', False)
    #bandageDone = False
    secondsCounter = 0
    while BandagesApplying():
        worldSave()
        Misc.Pause( 1000 )
        
        if overheadMessage:
            if secondsCounter == 0:
                Player.HeadMessage( msgcolor, 'Bandage Started' )
            else:
                Player.HeadMessage (msgcolor, 'Bandage: %is' % ( secondsCounter ))
        else:
            if secondsCounter == 0:
                Misc.SendMessage( 'Bandage Started' , msgcolor )
            else:
                Misc.SendMessage ( 'Bandage: %is' % ( secondsCounter ) , msgcolor)
        
        secondsCounter += 1
        if secondsCounter > 18:
            break
            
    if overheadMessage:
        Player.HeadMessage(msgcolor, 'Bandage Available')
    else:
        Misc.SendMessage( 'Bandage Available', msgcolor )
       
    Misc.SetSharedValue('bandageDone', True)
    return

def worldSave():
    if Journal.SearchByType('The world is saving, please wait.', 'Regular' ):
        Misc.SendMessage('Pausing for world save', 33)
        while not Journal.SearchByType('World save complete.', 'Regular'):
            Misc.Pause(1000)
        Misc.SendMessage('Continuing', 33)
        Journal.Clear()    
    
Journal.Clear()
while True:
    if Player.IsGhost:
        # Player died, wait until Player is resurrected
        while Player.IsGhost:
            Misc.Pause( 100 )
    if Journal.Search('You begin applying the bandages.'):
        WaitForBandagesToApply()
        Journal.Clear()
    Misc.Pause( 50 )
