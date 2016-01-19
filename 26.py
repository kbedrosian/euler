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
    def digitAtIdx( digitIdx ):
        if digitIdx < len( dividendDigits ):
            return dividendDigits[ digitIdx ]
        else:
            return 0

    if dividend == 0:
        return None

    quotientStr = ''
    lengthOfRepeatedSequence = None
    dividendDigits = digits( dividend )

    digitIdx = 0
    intermediateDividend = dividendDigits[ 0 ]
    intermediateDividendsIdx = {}
    while True:
        if digitIdx == len( dividendDigits ):
            quotientStr += '.'

        if intermediateDividend < divisor:
            quotientStr += '0'
            digitIdx += 1
            intermediateDividend = 10 * intermediateDividend + digitAtIdx( digitIdx )
            continue

        if intermediateDividend in intermediateDividendsIdx:
            lengthOfRepeatedSequence = \
                digitIdx - intermediateDividendsIdx[ intermediateDividend ]
            quotientStr += ')'
            break

        # Consume the intermediate dividend.
        intermediateDividendsIdx[ intermediateDividend ] = digitIdx
        intermediateQuotient = intermediateDividend / divisor
        assert intermediateQuotient in range( 1, 10 )
        quotientStr += str( intermediateQuotient )

        digitIdx += 1
        intermediateDividend = 10 * ( intermediateDividend % divisor ) + digitAtIdx( digitIdx )

        if intermediateDividend == 0:
            break


    return lengthOfRepeatedSequence

if __name__ == '__main__':
    maxLenRepeatedSequence = 0
    divisorForMaxSeq = 1
    for i in xrange( 1, 1000 ):
        l = longestRepeatedSequenceInQuotient( 1, i )
        if l > maxLenRepeatedSequence:
            maxLenRepeatedSequence = l
            divisorForMaxSeq = i

    print 'Max length repeating sequence is %d, for 1/%d' % ( maxLenRepeatedSequence, divisorForMaxSeq )

