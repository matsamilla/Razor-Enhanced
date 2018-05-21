
def provoTwoNearest():
    instruments_list = [0xe9e, 0x2805, 0xe9d, 0xe9c, 0xeb3, 0xeb2, 0xeb1]
    instrument_total = 0
        
    for i in Player.Backpack.Contains:
        if i.ItemID in instruments_list:
            instrument_total += 1 
            Items.UseItem(i)
            Misc.Pause(600)
    if instrument_total == 0: Player.HeadMessage(55, "no instrument found")

        
    provo1 = 0
    provo2 = 0
    counter = 0
    max = 10 #  number of maximum try
    Target.ClearLastandQueue()
    Target.Cancel()

    Target.SetLastTargetFromList("nearestenemy")
    provo1 = provo2 = Target.GetLast()
    Target.TargetExecute(provo1)
    Target.WaitForTarget(500, True)
    while provo1 == provo2 and counter <= max: #try to find a second target 
        Target.SetLastTargetFromList("nearestenemy")
        provo2 = Target.GetLast()

    Player.UseSkill('Provocation')
    Target.WaitForTarget(500, True)
    Target.TargetExecute(provo1)
    Target.WaitForTarget(500, True)
    Target.TargetExecute(provo2)

    Target.ClearLastandQueue()
    Target.Cancel() 
    
provoTwoNearest()