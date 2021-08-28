# Sallos SmartPot by MatsaMilla
# Drinks cure if poisoned, otherwise drinks heal

def potDrink():
    if Player.Poisoned:
        Player.ChatSay( 1 , '[drink greatercurepotion')
        Misc.Pause(100)
        if Journal.Search( 'You do not have any of those potions.'):
            Player.HeadMessage(33, "No Cure pots!")
    else:
        Player.ChatSay( 1 , '[drink greaterhealpotion')
        Misc.Pause(100)
        if Journal.Search( 'You do not have any of those potions.'):
            Player.HeadMessage(33, "No Heal pots!")

def usePot():
    if Player.Poisoned:
        orangePot = Items.FindByID(0x0F07,0,Player.Backpack.Serial,True)
        if orangePot:
            Items.UseItem(orangePot)
        else:
            Player.HeadMessage(33, "No Cure pots!")
    else:
        yellowPot = Items.FindByID(0x0F0C,0,Player.Backpack.Serial,True)
        if yellowPot:
            Items.UseItem(orangePot)
        else:
            Player.HeadMessage(33, "No Heal pots!")

if Misc.ShardName() == "Ultima Forever":
    potDrink()
else:
    usePot()
