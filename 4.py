#!/usr/bin/python

def largestPalindromeProduct( maxFactor ):
    maxPalindrome = 0
    factor1 = maxFactor
    while factor1 > 0:
        factor2 = factor1
        while factor2 > 0:
            product = factor1 * factor2
            productStr = str( product )
            if productStr == ''.join( reversed( productStr ) ):
                if product > maxPalindrome:
                    maxPalindrome = product
            factor2 -= 1
        factor1 -= 1
    return maxPalindrome

print largestPalindromeProduct( 99 )
