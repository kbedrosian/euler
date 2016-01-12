#!/usr/bin/python

import string

def namesScoreSum( names ):
    scoreSum = 0
    names.sort()
    for i in range( len( names ) ):
        scoreSum += ( i + 1 ) * sum( string.uppercase.index( letter ) + 1 for letter in names[ i ] )
    return scoreSum

print namesScoreSum( [ w.strip( '"' ) for w in open( 'p022_names.txt', 'r' ).read().split( ',' ) ] )
