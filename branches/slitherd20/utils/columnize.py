# This is a little functionality module that I'm going to call:
###   The Columnizer!!! ###
# The whole point here is to take a list and display it in a nicely ordered
# column format.  Based upon Kuros' code from the original Slither base.

def columnize(player, list, columns, sorted = True, padding = 2):
    # Start out with a blank line for some nice whitespace padding
    player.writePlain("\r\n")
    # First, we need to make sure that our list isn't empty
    try:
        assert list[0] != 0
    except:
        return
    # Some variables we're going to use in the course of our function
    iter        = 1
    length      = 0
    numColumns  = columns

    # Now we check to see if we want the list displayed alphabetically
    if sorted == True:
        list.sort()

    # Now we get down to actually displaying the list...
    # We start by measuring the size of each object in the list, to figure out
    # how much space we need to make it look right...
    for item in list:
        if len(item) > length:
            # You can pass a different padding size if you want, we default
            # to two because it makes a nicely padded list.
            length = len(item) + padding

    # Here, we're actually printing out the list...
    for item in list:
        if iter == numColumns:
            # We throw in a carriage return when we've reached out column limit
            player.writePlain( item + '\r\n')
            # We reset iter to 1 because with zero indexing, we'd have to make
            # things ugly subtracting 1 from the number of columns that were
            # passed, easier to fudge 1-indexing.
            iter = 1
        else:
            z = length - len(item)
            player.writePlain(item)
            for a in range(z):
                player.writePlain(" ")
            iter += 1
    player.writeWithPrompt("\r\n")