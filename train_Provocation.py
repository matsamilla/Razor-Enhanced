'''
Author: TheWarDoctor95
Other Contributors:
    Last Contribution By: MatsaMilla - March 28, 2020

Description: Uses the instruments from the player backpack and the selected target
    to train Provocation to GM Provokes mobs onto yourself
    
    Targets nearest mob until 75, then tries to target a rotting corpse if one is around.
    
'''
from System.Collections.Generic import List
from System import Byte

# provo skill cooldown
provocationTimerMilliseconds = 10200

instruments = [0xe9e, 0x2805, 0xe9c, 0xeb3, 0xeb1, 0x0eb2 , 0x0E9D] 

enemyFilter = Mobiles.Filter()
enemyFilter.Enabled = True
enemyFilter.RangeMax = 12
enemyFilter.Notorieties = List[Byte](bytes( [ 3 , 4 ] ) )

rottingFilter = Mobiles.Filter()
rottingFilter.Enabled = True
rottingFilter.RangeMax = 12
rottingFilter.Bodies = List[int] ( [ 0x009B ] )

def TrainProvocation():
    '''
    Trains Musicianship by using the instruments in the player bag
    Transitions to a new instrument if the one being used runs out of uses
    '''
    global provocationTimerMilliseconds
    global provocationTarget

    Timer.Create( 'provocationTimer', 1 )

    while Player.GetSkillValue( 'Provocation' ) < 100:
        
        rottingMob = Mobiles.ApplyFilter(rottingFilter)
        rotting = Mobiles.Select(rottingMob, "Nearest")
        
        enemyMob = Mobiles.ApplyFilter(enemyFilter)
        enemy = Mobiles.Select(enemyMob, "Farthest")
        
        if Timer.Check( 'provocationTimer' ) == False:
            Journal.Clear()
            
            Player.UseSkill( 'Provocation' )
            Misc.Pause(120)
            
            # selects an instrument if on is needed.
            if Journal.Search("What instrument shall you play?"):
                for i in Player.Backpack.Contains:
                    if i.ItemID in instruments:
                        Target.TargetExecute(i)
                        Player.HeadMessage(33, "Instrument Found")
                        Journal.Clear()
                        Misc.Pause(200)
                        break
                Misc.SendMessage('No Instruments found',33)
                Stop

            Target.WaitForTarget( 2000, True )
            
            # targets a mob
            if Player.GetSkillValue( 'Provocation' ) < 75:
                Target.TargetExecute( enemy )
            elif Player.GetSkillValue( 'Provocation' ) > 75:
                if rotting:
                    Target.TargetExecute( rotting )
                else:
                    Target.TargetExecute( enemy )
            else:
                Target.TargetExecute( enemy )
            
            Target.WaitForTarget( 2000, True )
            Target.Self()

            Timer.Create( 'provocationTimer', provocationTimerMilliseconds )

        # Wait a little bit so that the while loop does not consume as much CPU
        Misc.Pause( 50 )
    
    Player.HeadMessage(66, 'Wahoo! GM Provo!')

# Start Training
TrainProvocation()
