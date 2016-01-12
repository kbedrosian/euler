#!/usr/bin/python

import math

def amicableSum( max ):
    amicableSum = 0
    currentNum = 1
    divisorSums = {}
    while currentNum < max:
        divisorSum = 1
        potentialDivisor = 2
        while potentialDivisor <= math.sqrt( currentNum ):
            if currentNum % potentialDivisor == 0:
                divisorSum += potentialDivisor
                if potentialDivisor != ( currentNum / potentialDivisor ):
                    divisorSum += currentNum / potentialDivisor
            potentialDivisor += 1
        if divisorSum in divisorSums and divisorSums[ divisorSum ] == currentNum:
            print ( currentNum, divisorSum )
            amicableSum += currentNum + divisorSum
        divisorSums[ currentNum ] = divisorSum
        currentNum += 1
    return amicableSum

print amicableSum( 10000 )
