#!/usr/bin/python

def evenFibSum( max ):
    if max < 2:
        return 0
    evenSum = 2

    twoPrev = 1
    onePrev = 2
    currentFibNum = onePrev + twoPrev
    while currentFibNum < max:
        if currentFibNum % 2 == 0:
            evenSum += currentFibNum
        twoPrev = onePrev
        onePrev = currentFibNum
        currentFibNum = onePrev + twoPrev
    return evenSum

print evenFibSum( 4000000 )
