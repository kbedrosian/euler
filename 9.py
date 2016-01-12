#!/usr/bin/python

def pythagoreanTriplet( sum ):
    for third in reversed( range( 1, sum - 1 ) ):
        thirdSquared = third**2
        left = sum - third
        for second in reversed( range( 1, left ) ):
            first = left - second
            if ( second**2  + first**2 ) == thirdSquared:
                return first * second * third

print pythagoreanTriplet( 1000 )
