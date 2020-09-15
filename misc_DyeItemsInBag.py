# use this to dye all items inside a container (I use to dye armor)

dyeTub = Target.PromptTarget( 'Target dye tub' )
container = Items.FindBySerial( Target.PromptTarget( 'Target Container with armor' ) )

for i in container.Contains:
    Items.UseItem(dyeTub)
    Target.WaitForTarget(1500)
    Target.TargetExecute(i)
    Misc.Pause(550)