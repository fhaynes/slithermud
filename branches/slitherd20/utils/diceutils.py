import random

def roll(numOf, numSide):
    return [random.randint(1,numSide) for i in range(numOf)]

def rollTotal(numOf, numSide):
    results = [random.randint(1, numSide) for i in range(numOf)]
    total = 0
    for eachRes in results:
        total += eachRes
    return total

def statRoll(numStats, numDie, numSides):
    """
    I added this function to handle a method of rolling stats.
    This will actually roll twice the number of "stats" that you want,
    returning a list of the highest of the selection.  This works well
    for getting rid of a lot of the lower rolls.
    Running this function for 6 stats generally returns a set of values
    averaging around 11-12, with 9 or 10 being the general low and a value
    of 16 being pretty high.
    """
    statList = [rollTotal(numDie, numSides) for i in range(2 * numStats)]
    statList.sort()
    return statList[numStats:]