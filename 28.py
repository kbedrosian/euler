#!/usr/bin/python
'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

(spiral = 1 3 5 7 9 13 17 21 25)
It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

curr_num = 1
diagonals_sum = 1
side_len = 3
while side_len <= 1001:
    for _ in xrange(4):
        curr_num += (side_len - 1)
        diagonals_sum += curr_num
    side_len += 2
print diagonals_sum
