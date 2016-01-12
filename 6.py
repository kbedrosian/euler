#!/usr/bin/python

def sumSquareDifference( max ):
    return sum( range( 1, max + 1 ) )**2 - sum( num**2 for num in range( 1, max + 1 ) )

print sumSquareDifference( 10 )
