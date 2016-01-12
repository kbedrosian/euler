#!/usr/bin/python

'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

def factorial( x ):
    if x == 1:
        return 1
    else:
        return reduce( lambda x, y: x * y, range( 1, x+1 ) )

def digitLexicographicPermutation( permNum ):
    # Make it 0-based.
    permNum -= 1
    # Determine digits from left to right.
    permutation = []
    digitsLeft = range( 10 )
    while digitsLeft:
        if len( digitsLeft ) == 1:
            digit = digitsLeft[ 0 ]
        else:
            # Figure out how many permutations there are for each choice of this next digit, leaving the remaining digits free.
            # We'll floor-divide the number of permutations we have left by this, to determine the digit.
            permsPerDigit = factorial( len( digitsLeft ) - 1 )
            digit = digitsLeft[ permNum / permsPerDigit ]
            permNum %= permsPerDigit
        permutation.append( digit )
        digitsLeft.remove( digit )
    return ''.join( map( str, permutation ) )

print digitLexicographicPermutation( 1000000 )
