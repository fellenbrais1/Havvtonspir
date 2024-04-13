# This code makes use of the calendar module to simply print a calendar based \
# on the data.

from calendar import *


# This function uses calendar data to print out a simple formatted calendar.
def calender_maker():
    """
    A program to generate a calendar based on a year number.

    Makes use of calendar module to gather the data for calendar creation.

    :return: Function prints calendar and returns 'None'.
    """
    year = int(input("Enter the year: "))
    print(calendar(year, 2, 1, 8, 3))


# This function call runs the defined function.
calender_maker()
