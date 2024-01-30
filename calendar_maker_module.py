
# This code is just 'calendar_maker.py' but trimmed down, so it can be \
# imported into other programs
from calendar import *


def calender_maker():
    year = int(input("Enter the year: "))
    print(calendar(year, 2, 1, 8, 3))


# This final piece of code means that 'Calendar_Module' won't run \
# automatically when imported
# '__name__ == "__main__"' means that it will only run if called and made into \
# the main active code
if __name__ == "__main__":
    calender_maker()
