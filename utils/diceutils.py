import random

def roll(numOf, numSide):
    return [random.randint(1,numSide) for i in range(numOf)]

def rollTotal(numOf, numSide):
    results = [random.randint(1, numSide) for i in range(numOf)]
    total = 0
    for eachRes in results:
        total += eachRes
    return total