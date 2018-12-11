#This will provoke 2 grey mobs onto eachother or a grey mob onto a PK
#You have to setup 2 Enhanced Targetings though, nextenemy and pkenemy
#nextenemy should have grey, grey (aggro) checked. Selector set to Next, and Human flag set to no, 
#    friend flag to no, Range Min: -1, Range Max: 9
#pkenemy should have Red checked, Selector set to closeset, and Human Flag to yes, Friends flag to no.

#uncomment the block of code for it to play an insturment before you provo, guarenteeing you 
#dont have the which instrument pop up instead of provoing. 


def provoTwoNearest():
    
    if Journal.Search("What instrument"):
        Player.HeadMessage(55, "Shouldnt see this")
        instruments_list = [0xe9e, 0x2805, 0xe9d, 0xe9c, 0xeb3, 0xeb2, 0xeb1]
        instrument_total = 0
        for i in Player.Backpack.Contains:
            if i.ItemID in instruments_list:
                instrument_total += 1 
                Items.UseItem(i)
                Misc.Pause(800)
        if instrument_total == 0: Player.HeadMessage(55, "no instrument found")
    
    provo1 = 0
    provo2 = 0
    counter = 0
    max = 10 #  number of maximum try
    Target.ClearLastandQueue()
    Target.Cancel()

    Target.SetLastTargetFromList("nextenemy")
    provo1 = provo2 = Target.GetLast()
    Misc.Pause(200)
    
    if Target.GetTargetFromList("pkenemy") is None:
        while provo1 == provo2 and counter <= max: #try to find a second target 
            Target.SetLastTargetFromList("nextenemy")
            provo2 = Target.GetLast()
            counter += 1
    else:
        Target.SetLastTargetFromList("pkenemy")
        provo2 = Target.GetLast()
        Player.HeadMessage (55, "PK PK PK")

    Player.UseSkill('Provocation')
    Target.WaitForTarget(2000 , True)
    Target.TargetExecute(provo1)
    Target.WaitForTarget(2000 , True)
    Target.TargetExecute(provo2)

    Target.ClearLastandQueue()
    Target.Cancel() 
    
provoTwoNearest()
