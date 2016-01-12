#!/usr/bin/python

def maxPathSum( rows ):
    maxPathSumFrom = {}
    for i in reversed( range( len( rows ) ) ):
        for j in range( len( rows[ i ] ) ):
            if i == len( rows ) - 1:
                maxPathSumFrom[ ( i, j ) ] = rows[ i ][ j ]
            else:
                maxPathSumFrom[ ( i, j ) ] = rows[ i ][ j ] + max( maxPathSumFrom[ ( i+1, j ) ], maxPathSumFrom[ ( i+1, j+1 ) ] )
    return maxPathSumFrom[ ( 0, 0 ) ]

rowStr = open( 'p067_triangle.txt', 'r' ).read()
rows = [ [ int( n ) for n in row.split() ] for row in rowStr.split( '\n' )[ :-1 ] ]

print maxPathSum( rows )
