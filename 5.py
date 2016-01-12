#!/usr/bin/python

def smallestEvenlyDivisible( divisors ):
    product = 1
    currentNum = 2
    numsToFactor = divisors
    while numsToFactor:
        anyDivisible = False
        updatedNumsToFactor = []
        for numToFactor in numsToFactor:
            if numToFactor % currentNum == 0:
                anyDivisible = True
                numToFactor /= currentNum
            if numToFactor > 1:
                updatedNumsToFactor.append( numToFactor )
        if anyDivisible:
            product *= currentNum
        else:
            currentNum += 1
        numsToFactor = updatedNumsToFactor
    return product

print smallestEvenlyDivisible( range( 1, 21 ) )
