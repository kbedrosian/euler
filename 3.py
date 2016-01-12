#!/usr/bin/python

def primeFactors( numToFactor ):
    primeFactors = []
    currentNum = 2
    while numToFactor > 1:
        if numToFactor % currentNum == 0:
            primeFactors.append( currentNum )
            numToFactor /= currentNum
        else:
            currentNum += 1
    return primeFactors

print primeFactors( 600851475143 )
