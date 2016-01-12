#!/usr/bin/python

def letterCountForNumbers( max, verbose=False ):
    digitStrs = {
        1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four', 
        5 : 'five',
        6 : 'six',
        7 : 'seven',
        8 : 'eight',
        9 : 'nine' }
    teenStrs = {
        10 : 'ten',
        11 : 'eleven',
        12 : 'twelve',
        13 : 'thirteen',
        14 : 'fourteen',
        15 : 'fifteen',
        16 : 'sixteen',
        17 : 'seventeen',
        18 : 'eighteen',
        19 : 'nineteen' }
    tensFrom20 = {
        2 : 'twenty',
        3 : 'thirty',
        4 : 'forty',
        5 : 'fifty',
        6 : 'sixty',
        7 : 'seventy',
        8 : 'eighty',
        9 : 'ninety' }

    totalNumStrLen = 0
    for num in range( 1, max+1 ):
        if verbose:
            print 'string for %s is' % num,
            numStr = ''
        power = 3
        numStrLen = 0
        useAnd = False
        while num:
            powerOfTen = 10 ** power
            if powerOfTen == 100 or powerOfTen == 1000:
                digit = num / powerOfTen
                num %= powerOfTen
                if digit:
                    useAnd = True
                    if power == 3:
                        digitStr = digitStrs[ digit ] + ' thousand '
                        if verbose:
                            numStr += digitStr 
                        numStrLen += len( ''.join( digitStr.split() ) )
                    elif power == 2:
                        digitStr = digitStrs[ digit ] + ' hundred '
                        if verbose:
                            numStr += digitStr
                        numStrLen += len( ''.join( digitStr.split() ) )
            elif powerOfTen == 10:
                if useAnd:
                    twoDigitsStr = 'and '
                else:
                    twoDigitsStr = ''
                if num < 10:
                    twoDigitsStr += digitStrs[ num ]
                elif num < 20:
                    twoDigitsStr += teenStrs[ num ]
                else:
                    tens = num / 10
                    ones = num % 10
                    twoDigitsStr += tensFrom20[ tens ] + ' ' + ( digitStrs[ ones ] if ones else '' )
                if verbose:
                    numStr += twoDigitsStr
                numStrLen += len ( ''.join( twoDigitsStr.split() ) )
                num = 0
            else:
                assert False, power
            power -= 1
        if verbose:
            print '%s (len %s)' % ( numStr, numStrLen )
        totalNumStrLen += numStrLen
    return totalNumStrLen

print letterCountForNumbers( 1000, verbose=False )
