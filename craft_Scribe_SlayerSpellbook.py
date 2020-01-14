# Slayer Spellbook Crafter by MatsaMilla
# Last edit: Matsamilla 1/5/20
#
# Restocks blank scrolls from beetle (1k at a time)
# Moves slayers to beetle
from System.Collections.Generic import List
import winsound

#***************SETUP SECTION**********************************
#ItemSerials
beetle = 0x0023F0A0
ignoreBook = 0x458CD42E # do not throw away your full spellbook
keepAll = False # true to keep all slayers, False keeps supers only
#**************************************************************

error = "Sounds\error.wav"
cheer = "Sounds\cheer.wav"
dragTime = 600
pen = 0xfbf
scrolls = 0x0EF3
spellbook = 0x0EFA
noColor = 0x0000
self_pack = Player.Backpack.Serial
self = Player.Serial
rightHand = Player.CheckLayer('RightHand')

keepSlayerProps = ['Silver','Reptilian Death','Elemental Ban','Repond','Exorcism','Arachnid Doom','Fey'] 
    # some other popular lesser slayers, add to list above if you want to keep
    #'Blood Drinking','Balron Damnation','Daemon Dismissal','Ogre Thrashing','Dragon Slaying','Orc Slaying'
    
if not rightHand:
    Player.EquipItem(ignoreBook)
    Misc.Pause(dragTime)

# Use neraby trashcan
trashBarrelFilter = Items.Filter()
trashBarrelFilter.OnGround = 1
trashBarrelFilter.Movable = False
trashBarrelFilter.RangeMin = 0
trashBarrelFilter.RangeMax = 2
trashBarrelFilter.Graphics = List[int]( [ 0x0E77 ] )
trashBarrelFilter.Hues = List[int]( [ 0x03B2 ] )
trashcanhere = Items.ApplyFilter( trashBarrelFilter )

if not trashcanhere:
    Player.HeadMessage( 1100, 'No trashcan nearby!' )
    Stop
else:
    global trashcan
    trashcan = trashcanhere[ 0 ]

def moveSlayerBookToBeetle():
    if Player.Mount:
        Mobiles.UseMobile(self)
        Misc.Pause(dragTime)
        Items.Move(craftedBook, beetle, 1)
        Misc.Pause(dragTime)
        Mobiles.UseMobile(beetle)
        Misc.Pause(dragTime)
        
def trashSpellbook():
    if craftedBook:
        Items.Move(craftedBook, trashcan, 1)
        Misc.Pause(dragTime)
    
def hide():
    if not Player.BuffsExist('Hiding') and Timer.Check('hideskill') == False:
        Player.UseSkill('Hiding')
        Timer.Create('hideskill',11000)

def checkMats():
    if Items.BackpackCount(pen, -1) < 1:
        Misc.SendMessage('Out of Pens',33)
        winsound.PlaySound(error, winsound.SND_FILENAME)
        if not Player.Mount:
                Mobiles.UseMobile(beetle)
                Misc.Pause(dragTime)
        Stop
        
    if Items.BackpackCount(scrolls, -1) < 16:
        restockScrolls()
        Misc.Pause(dragTime)
        if Items.BackpackCount(scrolls, -1) < 16:
            Misc.SendMessage('Out of Scrolls',33)
            winsound.PlaySound(error, winsound.SND_FILENAME)
            if not Player.Mount:
                Mobiles.UseMobile(beetle)
                Misc.Pause(dragTime)
            Stop
            
def restockScrolls():
    if Player.Mount:
        Mobiles.UseMobile(self)
        Misc.Pause(dragTime)
        backpackscrolls = Items.FindByID(scrolls, noColor, self_pack)
        if backpackscrolls:
            Items.Move(backpackscrolls, beetle, -1)
            Misc.Pause(dragTime)
        Mobiles.SingleClick(beetle)
        Misc.WaitForContext(beetle, 1500)
        Misc.ContextReply(beetle, "Open Backpack")
        Misc.Pause(dragTime)
        beetleScrolls = Items.FindByID(scrolls, noColor, -1)
        if beetleScrolls:
            Items.Move(beetleScrolls, self_pack, 500)
            Misc.Pause(dragTime)
    
    if not Player.Mount:
        Mobiles.UseMobile(beetle)
        Misc.Pause(dragTime)
        
def craftBook():
    currentPen = Items.FindByID(pen, -1, -1)
    Items.UseItem(currentPen.Serial)
    Gumps.WaitForGump(0x38920abd,1500)
    Gumps.SendAction(0x38920abd, 57)
    Gumps.WaitForGump(0x38920abd,1500)
    Gumps.SendAction(0x38920abd, 16)
    Misc.Pause(2000)
    
def slayerCheck():
    global craftedBook
    craftedBook = Items.FindByID(spellbook, -1, self_pack)
    
    if Journal.SearchByType('You have successfully crafted a slayer spellbook.', 'Regular'):
        if keepAll:
            moveSlayerBookToBeetle()
            Journal.Clear()
        else:
            Items.SingleClick(craftedBook.Serial)
            Misc.Pause(dragTime)
            if any(Journal.Search(keep) for keep in keepSlayerProps):
                moveSlayerBookToBeetle()
                Journal.Clear()
            else:
                trashSpellbook()
    else:
        trashSpellbook()
            
while True:
    Journal.Clear()
    if Player.GetRealSkillValue('Hiding') > 30:
        hide() 
    checkMats()           
    craftBook()
    while Items.BackpackCount(spellbook, -1) > 0:
        slayerCheck()
    if not Player.Mount:
        Mobiles.UseMobile(beetle)
        Misc.Pause(dragTime)
