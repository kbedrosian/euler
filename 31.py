#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

COIN_VALUES_IN_PENCE = { 1, 2, 5, 10, 20, 50, 100, 200 }

def waysToChange( numPence ):
    soFar = set()
    results = set()
    stack = [ ( (), 0 ) ]
    while stack:
        ( changeDictItems, changeSum ) = stack.pop()
        if changeDictItems in soFar:
            continue
        soFar.add( changeDictItems )
        for coinValue in COIN_VALUES_IN_PENCE:
            nextChangeSum = changeSum + coinValue

            nextChangeDict = dict( changeDictItems )
            if coinValue not in nextChangeDict:
                nextChangeDict[ coinValue ] = 0
            nextChangeDict[ coinValue ] += 1
            nextChangeDictItems = tuple( sorted( nextChangeDict.items() ) )

            if nextChangeSum == numPence:
                results.add( nextChangeDictItems )
            elif nextChangeSum < numPence:
                stack.append( ( nextChangeDictItems, nextChangeSum ) )
    return results

print len( waysToChange( 200 ) )
