# Simple script to attack a target from a list and set it to last target
# Set up a targeting filter on the Targeting tab named enemy, example here https://imgur.com/a/f9rvEPe
# The example above will target the nearest grey non humanoid non friended mob within 12 tiles.

# set enemy variable from the targeting list 'enemy' 
enemy = Target.GetTargetFromList('enemy')

# check if there is an enemy, if there is continue
if enemy:
    Player.ChatSay(44,"All Kill")
    Target.WaitForTarget(1500)
    # this will target the enemy variable obtained from the list in the first line
    Target.TargetExecute(enemy)
    
# if no enemies, alert the player with a head message
else:
    Player.HeadMessage(44,"No Enemies")
    
