#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Euler published the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n² + 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''

import math

def isPrime( n, debug=False ):
    if n < 2:
        if debug:
            print n, 'is not prime'
        return False
    currentNum = 2
    while currentNum <= math.sqrt( n ):
        if n % currentNum == 0:
            if debug:
                print n, 'is not prime'
            return False
        currentNum += 1
    if debug:
        print n, 'is prime'
    return True

def longestPrimeString( a, b, debug=False ):
    abPairs = []
    for i in xrange( -a, a ):
        for j in xrange( -b, b ):
            abPairs.append( ( i, j ) )
    n = 0
    while len( abPairs ) > 1:
        if debug:
            print 'before n =', n, ' abPairs is', abPairs
        abPairs[ : ] = [ abPair for abPair in abPairs if isPrime( abs(n**2 + abPair[ 0 ]*n + abPair[ 1 ]) ) ]
        if debug:
            print 'after n =', n, ' abPairs is', abPairs
        n += 1
    return abPairs[ 0 ][ 0 ] * abPairs[ 0 ][ 1 ]

print longestPrimeString( 1000, 1000 )
