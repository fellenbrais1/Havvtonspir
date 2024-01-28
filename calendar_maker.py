
# This code makes use of the calendar module to simply print a calendar based on the data
from calendar import *

# This function uses calendar data to print out a simple formatted calendar


def calender_maker():
    year = int(input("Enter the year: "))
    print(calendar(year, 2, 1, 8, 3))


# This function call runs the defined function
calender_maker()
