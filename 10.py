#!/usr/bin/python
import math

def sumOfPrimes( max ):
    primesSeen = [ 2 ]
    primeSum = 2
    currentNum = 3
    while currentNum < max:
        hasDivisor = False
        for prime in primesSeen:
            if prime > math.sqrt( currentNum ):
                break
            if currentNum % prime == 0:
                hasDivisor = True
                break
        if not hasDivisor:
            primesSeen.append( currentNum )
            primeSum += currentNum
        currentNum += 2
    return primeSum

print sumOfPrimes( 2000000 )
