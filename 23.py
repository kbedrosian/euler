#!/usr/bin/python
import math

def sumOfDivisors( num ):
    divisorSum = 1
    potentialDivisor = 2
    while potentialDivisor <= math.sqrt( num ):
        if num % potentialDivisor == 0:
            divisorSum += potentialDivisor
            otherDivisor = num / potentialDivisor
            # Don't count duplicates.
            if otherDivisor != potentialDivisor:
                divisorSum += otherDivisor
        potentialDivisor += 1
    return divisorSum

def isAbundant( num ):
    return sumOfDivisors( num ) > num
    
def nonAbundantSum( max ):
    '''Returns the sum of all numbers less than the given max which are the sum of 
    two abundant numbers.'''
    # Start out assuming all numbers are not sums of two abundant numbers.  
    # We'll mark entries True as we find such numbers.
    sumOfTwoAbundants = [ False ]*( max + 1 )
    # We only need to consider abundant numbers less than max.
    abundantNums = []
    for num in xrange( 1, max + 1 ):
        if isAbundant( num ):
            abundantNums.append( num )
            for abundantNum in abundantNums:
                if abundantNum + num > max:
                    break
                else:
                    sumOfTwoAbundants[ abundantNum + num ] = True
    numsNotSumOfTwoAbundants = [ num for num in xrange( 1, max + 1 ) if not sumOfTwoAbundants[ num ] ]
    result = sum( numsNotSumOfTwoAbundants )
    return result

print nonAbundantSum( 28124 )
