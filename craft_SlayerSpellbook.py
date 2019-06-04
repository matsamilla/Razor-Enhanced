# Slayer Spellbook Crafter by MatsaMilla
# Last edit: Matsamilla 6/4/19
#
# Restocks blank scrolls from beetle (1k at a time)
# Moves slayers to beetle

#***************SETUP SECTION**********************************
#ItemSerials
trashcan = 0x4007b816
beetle = 0x1aa252
ignoreBook = 0x458CD42E # don't throw away your full spellbook
#**************************************************************

dragTime = 600
pen = 0xfbf
scrolls = 0xef3
spellbook = 0x0EFA
noColor = 0x0000
self_pack = Player.Backpack.Serial
self = Player.Serial
rightHand = Player.CheckLayer('RightHand')
if not rightHand:
    Player.EquipItem(ignoreBook)
    Misc.Pause(dragTime)

keepProps = ['Silver','Undead','Snake','Lizardman','Dragon','Reptile','Terathan','Scorpion',
'Spider','Orc Slaying','Ogre','Water','Earth','Elemental','Flame','Vacuum','Repond','Fey','Gargoyle',
'Daemon','Exorcism']

def moveSlayerBookToBeetle():
    if Player.Mount:
        Mobiles.UseMobile(self)
        Misc.Pause(dragTime)
        #slayerBook = Items.FindByID(spellbook, noColor, self_pack)
        Items.Move(craftedBook, beetle, 1)
        Misc.Pause(dragTime)
        Mobiles.UseMobile(beetle)
        Misc.Pause(dragTime)
        
def trashSpellbook():
    #trashbook = Items.FindByID(spellbook, noColor, self_pack)
    Items.Move(craftedBook, trashcan, 1)
    Misc.Pause(dragTime)
    
def hide():
    if not Player.BuffsExist('Hiding'):
        Player.UseSkill('Hiding')

def checkMats():
    if Items.BackpackCount(pen, -1) < 1:
        Misc.SendMessage('Out of Pens',33)
        winsound.PlaySound(error, winsound.SND_FILENAME)
        Misc.ScriptStop('craft_SlayerSpellbook.py')
        
    if Items.BackpackCount(scrolls, -1) < 16:
        restockScrolls()
        if Items.BackpackCount(scrolls, -1) < 16:
            Misc.SendMessage('Out of Scrolls',33)
            winsound.PlaySound(error, winsound.SND_FILENAME)
            Misc.ScriptStop('craft_SlayerSpellbook.py')
            
def restockScrolls():
    if Player.Mount:
        Mobiles.UseMobile(self)
        Misc.Pause(dragTime)
        backpackscrolls = Items.FindByID(scrolls, noColor, self_pack)
        Items.Move(backpackscrolls, beetle, -1)
        Misc.Pause(dragTime)
        Misc.WaitForContext(0x001AA252, 10000)
        Misc.ContextReply(0x001AA252, 'Open Backpack')
        Misc.Pause(dragTime)
        beetleScrolls = Items.FindByID(scrolls, noColor, -1)
        Items.Move(beetleScrolls, self_pack, 1000)
        Misc.Pause(dragTime)
        Mobiles.UseMobile(beetle)
        Misc.Pause(dragTime)
        
def craftBook():
    currentPen = Items.FindByID(pen, -1, self_pack)
    Items.UseItem(currentPen.Serial)
    Gumps.WaitForGump(0x38920abd,1500)
    Gumps.SendAction(0x38920abd, 57)
    Gumps.WaitForGump(0x38920abd,1500)
    Gumps.SendAction(0x38920abd, 16)
    Misc.Pause(2000)
    
def slayerCheck():
    global craftedBook
    craftedBook = Items.FindByID(spellbook, -1, self_pack)
    if Journal.Search('You have successfully crafted a slayer'):
        moveSlayerBookToBeetle()
        Journal.Clear()
    else:
        #double check
        Items.SingleClick(craftedBook.Serial)
        Misc.Pause(dragTime)
        if any(Journal.Search(keep) for keep in keepProps):
            Misc.SendMessage('SLAYER SAVED')
            moveSlayerBookToBeetle()
            Journal.Clear()
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
