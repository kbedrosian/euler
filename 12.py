#!/usr/bin/python

import math

def triangleNumWithMoreDivisors( moreThan ):
    currentNum = 1
    currentTriangleNum = 1
    while True:
        divisors = 2
        potentialDivisor = 2
        while potentialDivisor < math.sqrt( currentTriangleNum ):
            if currentTriangleNum % potentialDivisor == 0:
                divisors += 2
            potentialDivisor += 1
        if divisors > moreThan:
            return currentTriangleNum
        currentNum +=  1
        currentTriangleNum += currentNum

print triangleNumWithMoreDivisors( 500 )
