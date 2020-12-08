# ItemID GM
# Targets dagger in bag until GM ItemID
# By MatsaMilla

def hide():
    if Player.GetRealSkillValue('Hiding') > 50:
        if Timer.Check('skill' + Player.Name) == False and not Player.BuffsExist('Hiding'):
            Player.UseSkill('Hiding')
            Timer.Create('skill' + Player.Name,11000)

def itemID():
    if Timer.Check('skill' + Player.Name) == False and Player.BuffsExist('Hiding'):
        dagger = Items.FindByID( 0x0F52 , -1 , Player.Backpack.Serial )
        Player.UseSkill( "Item ID" )
        Target.WaitForTarget( 10000  , True )
        Target.TargetExecute( dagger )
        Timer.Create('skill' + Player.Name,1000)


while Player.GetRealSkillValue( "Item ID" ) < 100:
    itemID()
    hide()
