#!/usr/bin/python

def primeNumber( n ):
    primesSeen = [ 2 ]
    currentNum = 3
    while len( primesSeen ) < n:
        hasDivisor = False
        for prime in primesSeen:
           if currentNum % prime == 0:
               hasDivisor = True
               break
        if not hasDivisor:
            primesSeen.append( currentNum )
        currentNum += 1
    return primesSeen[ -1 ]

print primeNumber( 10001 )
