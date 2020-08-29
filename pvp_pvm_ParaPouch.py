#para pouch popper
if Player.Paralized:
    Player.ChatSay (20, "[pouch")
    pouch = Items.FindByID( 0x0E79 , 0x0489 , Player.Backpack.Serial )
    if pouch:
        Items.WaitForProps(pouch, 500)
        Misc.Pause(120)
        charges = Items.GetPropValue(pouch, 'Charges')
    if charges > 0:
        Player.HeadMessage(0x0489,"{} charges".format(int(charges)))
