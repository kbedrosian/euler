#!/usr/bin/python

'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
from datetime import date, timedelta

class Weekday:
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6

# Value for February here is one less than it should be for a leap year.
DAYS_IN_MONTH = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

def numSundaysFirstOfMonth( startDate, endDate ):
    # Start with 1 Jan. 1900 as a point of reference.
    currentDate = date( 1900, 1, 1 )
    currentWeekday = Weekday.Monday
    result = 0
    while currentDate <= endDate:
        if currentDate >= startDate:
            if currentWeekday == Weekday.Sunday:
                result += 1
        days_in_month = DAYS_IN_MONTH[ currentDate.month - 1 ]
        if currentDate.month == 2:
            if ( currentDate.year % 4 == 0 ) and \
               ( currentDate.year % 100 != 0 or currentDate.year % 400 == 0 ):
                days_in_month += 1
        currentDate += timedelta( days=days_in_month )
        currentWeekday = ( currentWeekday + days_in_month ) % 7
    return result

print numSundaysFirstOfMonth( date( 1901, 1, 1 ), date( 2000, 12, 31 ) )
