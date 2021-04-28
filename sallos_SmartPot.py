# Sallos SmartPot by MatsaMilla
# Drinks cure if poisoned, otherwise drinks heal
if Player.Poisoned:
    Player.ChatSay( 1 , '[drink greatercurepotion')
    Misc.Pause(100)
    if Journal.Search( 'You do not have any of those potions.'):
        Player.HeadMessage(msgColor, "No Cure pots!")
else:
    Player.ChatSay( 1 , '[drink greaterhealpotion')
    Misc.Pause(100)
    if Journal.Search( 'You do not have any of those potions.'):
        Player.HeadMessage(msgColor, "No Heal pots!")
