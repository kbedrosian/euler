#!/usr/bin/python

'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

def numbersSumOfPowers( exponent, debug=False ):
    results = set()
    soFar = set()
    stack = [ ( i, i ** exponent ) for i in range( 1, 10 ) ]
    while stack:
        ( num, sumOfPowers ) = stack.pop()
        if num not in soFar:
            soFar.add( num )

            for digit in range( 0, 10 ):
                nextSumOfPowers = sumOfPowers + ( digit ** exponent )
                nextNum = ( num * 10 ) + digit
                if debug:
                    print 'for', ( num, sumOfPowers ), 'considering successor', \
                          ( nextNum, nextSumOfPowers ), 'for digit', digit

                if nextSumOfPowers == nextNum and nextNum != 1:
                    if debug:
                        print 'adding', nextNum, 'to results'
                    results.add( nextNum )

                if nextNum > nextSumOfPowers and ( nextNum * 10 ) > ( 9 ** exponent ):
                    if debug:
                        print 'not following', ( nextNum, nextSumOfPowers )
                    continue

                stack.append( ( nextNum, nextSumOfPowers ) )
    return results

print sum( numbersSumOfPowers( 5 ) )
