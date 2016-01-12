#!/usr/bin/python

def longestCollatzChain( max ):
    chainsSeen = { 1 : 1 }
    maxLength = 1
    maxStartingNum = 1
    for startingPoint in range( 2, max ):
        numsInSequence = []
        currentNum = startingPoint
        currentLength = 0
        while True:
            if currentNum in chainsSeen:
                currentLength += chainsSeen[ currentNum ]
                break
            if currentNum % 2 == 0:
                currentNum = currentNum / 2
            else:
                currentNum = currentNum * 3 + 1
            currentLength += 1
            if currentNum in numsInSequence:
                break
            numsInSequence.append( currentNum )
        chainsSeen[ startingPoint ] = currentLength
        if currentLength > maxLength:
            maxLength = currentLength
            maxStartingNum = startingPoint
    return maxLength, maxStartingNum

print longestCollatzChain( 1000000 )
