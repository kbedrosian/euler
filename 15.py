#!/usr/bin/python

def nChooseK( n, k ):
    def factorial( x ):
        return reduce( lambda x, y: x * y, range( 1, x+1 ) )
    return factorial( n ) / ( factorial( n - k ) * factorial( k ) )

print nChooseK( 40, 20 )
