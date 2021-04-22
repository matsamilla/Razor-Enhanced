# Bandage script by Matsamilla
# Relys on Bandage_Timer.py, without it it will not stop applying bandages.

# Pause at start for skill check,
# Script stops if no healing on toon.
import sys
Misc.Pause( 5000 )
if Player.GetRealSkillValue( 'Healing' ) < 50:
    Misc.SendMessage( 'No Healing, stopping script',33)
    Misc.Pause( 200 )
    sys.exit()


def BandageSelf():
    if Misc.ReadSharedValue('bandageDone') == True:
        lastTarget = Target.GetLast()
        while Target.HasTarget():
            Misc.Pause(10)
        Items.UseItemByID(0x0E21, 0)
        Target.WaitForTarget(1500, False)
        Target.Self()
        Misc.Pause (500)
        
        Target.SetLast(lastTarget)

Timer.Create( 'outOfBandageWarningIncrement', 1 )
while True:
    # make sure Bandage_Timer.py is running, script will not run
    # correctly if timer is not running.
    if not Misc.ScriptStatus('Bandage_Timer.py'):
        Misc.ScriptRun('Bandage_Timer.py')
    
    if Player.IsGhost:
        # Player died, wait until Player is resurrected
        while Player.IsGhost:
            Misc.Pause( 100 )
    
    # Checks for bandages
    if Items.BackpackCount( 0x0E21 ,-1 ):
        # only apply bandage if player is not hidden, damaged or poisoned and not one already applying.
        if Player.Visible == True and Player.Hits < Player.HitsMax or Player.Poisoned and Misc.CheckSharedValue('bandageDone') == True:
            BandageSelf()
    # if no bandages, warn player.
    elif Timer.Check( 'outOfBandageWarningIncrement' ) == False:
        Player.HeadMessage( 1100, 'Out of bandages!' )
        Timer.Create( 'outOfBandageWarningIncrement', 5000 )

    Misc.Pause( 50 )
