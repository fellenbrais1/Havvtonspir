
# This code makes use of the calendar module to simply print a calendar based on the data
from calendar import *


def calender_maker():
    year = int(input("Enter the year: "))
    print(calendar(year, 2, 1, 8, 3))


if __name__ == " __main__":
    calender_maker()
