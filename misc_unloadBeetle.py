# simple script to move items out of a beetle
# Target an item in a beetle, then container to move them to.
# Script will move all matching items from beetle to container
# By MatsaMilla

itemToMove = Target.PromptTarget('Select Item Inside container to move')

destinationContainer = Target.PromptTarget('Where to move items?')

def unloadBeetle ( item , destination ):

    foundItem = Items.FindBySerial( item )

    container = Items.FindBySerial( foundItem.Container )

    for i in container.Contains:
        if i.ItemID == foundItem.ItemID:
            Items.Move
            Items.Move ( i , destination , 0 )
            Misc.Pause( 600 )
        

unloadBeetle ( itemToMove , destinationContainer )