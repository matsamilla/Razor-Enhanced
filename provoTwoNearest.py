#This will provoke 2 grey mobs onto eachother or a grey mob onto a PK
#You have to setup 2 Enhanced Targetings though, next and pkenemy
#nextenemy should have grey, grey (aggro) checked. Selector set to Next, and Human flag set to no
#pkenemy should have Red checked, Selector set to closeset, and Human Flag to yes.

#uncomment the block of code for it to play an insturment before you provo, guarenteeing you 
#don't have the "which instrument" pop up instead of provoing. 


def provoTwoNearest():
#    
#    instruments_list = [0xe9e, 0x2805, 0xe9d, 0xe9c, 0xeb3, 0xeb2, 0xeb1]
#    instrument_total = 0
#        
#    for i in Player.Backpack.Contains:
#        if i.ItemID in instruments_list:
#            instrument_total += 1 
#            Items.UseItem(i)
#            Misc.Pause(600)
#    if instrument_total == 0: Player.HeadMessage(55, "no instrument found")
    
    provo1 = 0
    provo2 = 0
    counter = 0
    max = 10 #  number of maximum try
    Target.ClearLastandQueue()
    Target.Cancel()

    Target.SetLastTargetFromList("nextenemy")
    provo1 = provo2 = Target.GetLast()
    Target.TargetExecute(provo1)
    Target.WaitForTarget(500, True)
    
    if Target.GetTargetFromList("pkenemy") is None:
        while provo1 == provo2 and counter <= max: #try to find a second target 
            Target.SetLastTargetFromList("nextenemy")
            provo2 = Target.GetLast()
            counter += 1
    else:
        Target.SetLastTargetFromList("pkenemy")
        provo2 = Target.GetLast()
        Player.HeadMessage (55, "PKPKPK")

    Player.UseSkill('Provocation')
    Target.WaitForTarget(2000 , True)
    Target.TargetExecute(provo1)
    Target.WaitForTarget(2000 , True)
    Target.TargetExecute(provo2)

    Target.ClearLastandQueue()
    Target.Cancel() 
    
provoTwoNearest()
