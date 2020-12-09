# Poison trainer by MatsaMilla
# NEED: Bag of poison kegs
#       Empty bag for emtpy kegs to go into
#       Food to poison    

backpack = Player.Backpack.Serial
dragTime = 600
msgColor = 33
pKeg = None

def GetBag ( sharedValue, promptString ):
    if Misc.CheckSharedValue( sharedValue ):
        bag = Misc.ReadSharedValue( sharedValue )
        if not Items.FindBySerial( bag ):
            bag = Target.PromptTarget( promptString )
            Misc.SetSharedValue( sharedValue, bag )
    else:
        bag = Target.PromptTarget( promptString )
        Misc.SetSharedValue( sharedValue, bag )
    return bag
    
kegBag = Target.PromptTarget( 'Select Bag with Poison Kegs' )# GetBag( 'KegBag', 'Select Bag with Poison Kegs' )
emptyKegBag = Target.PromptTarget( 'Select Bag for empty Kegs' ) #GetBag( 'eKegBag', 'Select Bag for empty Kegs' )
toPoison = Target.PromptTarget( 'Target what you want to poison' ) #GetBag( 'toPoisonn', 'Target what you want to poison')

Items.UseItem(kegBag)
Misc.Pause(dragTime)
        
def restockKeg():
    emptyKeg = Items.FindByID( 0x1940 , -1 , backpack )
    if emptyKeg != None:
        Items.Move( emptyKeg , emptyKegBag , 0 )
        Misc.Pause(dragTime)
    
    Items.UseItem(kegBag)
    Misc.Pause(dragTime)
    
    pKeg = Items.FindByID( 0x1940 , -1 , kegBag )
    
    if pKeg != None:
        Items.Move( pKeg , backpack , 0 )
        Misc.Pause(dragTime)
    elif pkeg == None:
        Misc.SendMessage('Out of kegs', msgColor)
        Misc.Beep()
        Stop
            
def trainPoison():
    pkeg = Items.FindByID( 0x1940 , -1 , backpack )
    
    if not Items.BackpackCount(0xf0a, -1):
        Items.UseItem(pkeg)
        Misc.Pause(dragTime)
    
    ppot = Items.FindByID( 0xf0a , -1 , backpack )
    
    if ppot and Timer.Check('poisonTimer') == False:
        Player.UseSkill('Poisoning')
        Target.WaitForTarget(1500)
        Target.TargetExecute(ppot)
        Target.WaitForTarget(1500)
        Target.TargetExecute(toPoison)
        Timer.Create('poisonTimer', 11000)
    elif pkeg == None:
        restockKeg()
        Journal.Clear()
    
    if Journal.Search('The keg is empty.'):
        restockKeg()
        Journal.Clear()
        
def boxRefresh():
    if Timer.Check('boxrefresh') == False:
        Items.DropItemGroundSelf(kegBag, 0)
        Timer.Create('boxrefresh', 180000) #300000 = 5 mins    
        
Journal.Clear()        
while True:
    if Player.GetRealSkillValue('Poisoning') > 30 and Player.GetRealSkillValue('Poisoning') < 100:
        trainPoison()
        boxRefresh()
    Misc.Pause(100)
    
    while Player.Hits < 50:
        Misc.Pause(50)
