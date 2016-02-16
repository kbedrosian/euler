#!/usr/bin/python
'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

def digits( x ):
    if x == 0:
        return [ 0 ]
    else:
        result = []
        while x > 0:
            result.append( x % 10 )
            x /= 10
        result.reverse()
        return result

def longestRepeatedSequenceInQuotient( dividend, divisor ):
    if dividend == 0:
        return None

    quotientStr = ''
    lengthOfRepeatedSequence = None
    dividendDigits = digits( dividend )

    def digitAtIdx( digitIdx ):
        if digitIdx < len( dividendDigits ):
            return dividendDigits[ digitIdx ]
        else:
            return 0

    digitIdx = 0
    intermediateDividend = dividendDigits[ 0 ]
    intermediateDividendsIdx = {}
    while True:
        if digitIdx == len( dividendDigits ):
            quotientStr += '.'

        if digitIdx >= len( dividendDigits ):
            # If we are in the fractional part, start checking for cycles i.e.
            # intermediate dividend values we have seen before.
            if intermediateDividend in intermediateDividendsIdx:
                # Remove the trailing 0 if there is one.
                if quotientStr[ -1 ] == '0':
                    quotientStr = quotientStr[ :-1 ]
                previousDigitIdx = intermediateDividendsIdx[ intermediateDividend ]
                lengthOfRepeatedSequence = digitIdx - previousDigitIdx
                quotientStr = quotientStr[ :previousDigitIdx+1 ] + '(' + quotientStr[ previousDigitIdx+1: ] + ')'
                break
            else:
                intermediateDividendsIdx[ intermediateDividend ] = digitIdx

        if intermediateDividend < divisor:
            quotientStr += '0'
            digitIdx += 1
            intermediateDividend = 10 * intermediateDividend + digitAtIdx( digitIdx )
        else:
            # Consume the intermediate dividend.
            intermediateQuotient = intermediateDividend / divisor
            assert intermediateQuotient in range( 1, 10 )
            quotientStr += str( intermediateQuotient )

            digitIdx += 1
            intermediateDividend = 10 * ( intermediateDividend % divisor ) + digitAtIdx( digitIdx )

        if intermediateDividend == 0:
            break

    print quotientStr
    return lengthOfRepeatedSequence

if __name__ == '__main__':
    l = longestRepeatedSequenceInQuotient( 1, 11 )
    maxLenRepeatedSequence = 0
    divisorForMaxSeq = 1
    for i in xrange( 1, 12 ):
        l = longestRepeatedSequenceInQuotient( 1, i )
        if l > maxLenRepeatedSequence:
            maxLenRepeatedSequence = l
            divisorForMaxSeq = i

    print 'Max length repeating sequence is %d, for 1/%d' % ( maxLenRepeatedSequence, divisorForMaxSeq )

