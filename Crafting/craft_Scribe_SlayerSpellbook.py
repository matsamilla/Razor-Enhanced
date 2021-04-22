# Slayer Spellbook Crafter by MatsaMilla
# Last edit: Matsamilla 10/19/20
#
# Restocks blank scrolls from beetle (1k at a time)
# Moves slayers to beetle
from System.Collections.Generic import List
import winsound
import sys

#***************SETUP SECTION**********************************
#ItemSerials
beetle = 0x0023F0A0 # inspect beetle, copy serial of beetle here
beetleContainer = 0x439F1BD4 # inspect an item inside your beetles pack, copy container ID here (https://imgur.com/a/Yjfn8mB)
ignoreBook = 0x458CD42E # do not throw away your full spellbook
keepAll = False # true to keep all slayers, false keeps only ones in keepSlayerProps

toolTipsOn = True #true if using tool tips
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

keepSlayerProps = ['Silver','Reptilian Death','Elemental Ban','Repond','Exorcism','Arachnid Doom','Fey',
                    'Balron Damnation','Daemon Dismissal','Orc Slaying','Dragon Slaying', 'Blood Drinking'] 
    #'Blood Drinking','Balron Damnation','Daemon Dismissal','Ogre Thrashing','Dragon Slaying','Orc Slaying'
    
if not keepAll:
    Player.HeadMessage(66, 'Keeping:')
    for i in keepSlayerProps:
        Player.HeadMessage(66, i)
        Misc.Pause(200)
else:
    Player.HeadMessage(66, 'Keeping All Slayers')
    
slayers = ['Silver','Reptilian Death','Elemental Ban','Repond','Exorcism','Arachnid Doom','Fey',
                    'Balron Damnation','Daemon Dismissal','Orc Slaying', 'Blood Drinking', 'Troll Slaughter',
                    'Ogre Thrashing','Dragon Slaying','Earth Shatter','Elemental Health','Flame Dousing',
                    'Summer Wind','Vacuum','Water Dissipation','Gargoyles Foe','Scorpions Bane','Spiders Death',
                    'Terathan','Lizardman Slaughter','Ophidian','Snakes Bane']
    
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
    sys.exit()
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
    if Items.BackpackCount(scrolls, -1) < 16:
        restockScrolls()
        Misc.Pause(dragTime)
        if Items.BackpackCount(scrolls, -1) < 16:
            Misc.SendMessage('Out of Scrolls',33)
            Misc.Beep()
            if not Player.Mount:
                Mobiles.UseMobile(beetle)
                Misc.Pause(dragTime)
            sys.exit()
            
def restockScrolls():
    if Player.Mount:
        Mobiles.UseMobile(self)
        Misc.Pause(dragTime)
        Mobiles.SingleClick(beetle)
        Misc.WaitForContext(beetle, 1500)
        if Player.Visible:
            Misc.ContextReply(beetle, 10)
        else:
            Misc.ContextReply(beetle, 0)
        Misc.Pause(dragTime)
        beetleScrolls = Items.FindByID(scrolls, noColor, beetleContainer)
        if beetleScrolls:
            Player.HeadMessage (66, 'Restocking')
            Items.Move(beetleScrolls, self_pack, 500)
            Misc.Pause(dragTime)
    
    if not Player.Mount:
        Mobiles.UseMobile(beetle)
        Misc.Pause(dragTime)
        
def FindItem( itemID, container, color = -1, ignoreContainer = [] ):
    '''
    Searches through the container for the item IDs specified and returns the first one found
    Also searches through any subcontainers, which Misc.FindByID() does not
    '''

    ignoreColor = False
    if color == -1:
        ignoreColor = True

    if isinstance( itemID, int ):
        foundItem = next( ( item for item in container.Contains if ( item.ItemID == itemID and ( ignoreColor or item.Hue == color ) ) ), None )
    elif isinstance( itemID, list ):
        foundItem = next( ( item for item in container.Contains if ( item.ItemID in itemID and ( ignoreColor or item.Hue == color ) ) ), None )
    else:
        raise ValueError( 'Unknown argument type for itemID passed to FindItem().', itemID, container )

    if foundItem != None:
        return foundItem

    subcontainers = [ item for item in container.Contains if ( item.IsContainer and not item.Serial in ignoreContainer ) ]
    for subcontainer in subcontainers:
        foundItem = FindItem( itemID, subcontainer, color, ignoreContainer )
        if foundItem != None:
            return foundItem
        
def craftBook():
    currentPen = FindItem(pen, Player.Backpack)#Items.FindByID(pen, -1, -1)
    if currentPen:
        if Gumps.CurrentGump() != 0x38920abd:
            Items.UseItem(currentPen.Serial)
        Gumps.WaitForGump(0x38920abd,1500)
        Gumps.SendAction(0x38920abd, 57)
        Gumps.WaitForGump(0x38920abd,1500)
        Gumps.SendAction(0x38920abd, 16)
        Misc.Pause(2000)
    else:
        Misc.SendMessage('Out of Pens',33)
        Misc.Beep()
        if not Player.Mount:
                Mobiles.UseMobile(beetle)
                Misc.Pause(dragTime)
        sys.exit()
def slayerCheck():
    global craftedBook
    craftedBook = Items.FindByID(spellbook, -1, self_pack)
    
    if toolTipsOn:
        if keepAll:
            Items.WaitForProps(craftedBook, 1500)
            props = Items.GetPropStringList(craftedBook)
            if any(elem in slayers for elem in props):
                Player.HeadMessage (66, props[3]) 
                moveSlayerBookToBeetle()
            else:
                trashSpellbook()
        else:
            Items.WaitForProps(craftedBook, 1500)
            props = Items.GetPropStringList(craftedBook)
            if any(elem in keepSlayerProps for elem in props):
                Player.HeadMessage (66, props[3])
                moveSlayerBookToBeetle()
            else:
                trashSpellbook()
    
    else:
        if Journal.SearchByType('You have successfully crafted a slayer spellbook.', 'Regular'):
            if keepAll:
                moveSlayerBookToBeetle()
                Journal.Clear()
            else:
                if toolTipsOn:
                    Items.WaitForProps(craftedBook, 1500)
                    props = Items.GetPropStringList(craftedBook)
                    if any(elem in keepSlayerProps for elem in props):
                        moveSlayerBookToBeetle()
                    else:
                        trashSpellbook()
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
