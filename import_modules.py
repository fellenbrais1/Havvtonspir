
# This is a test of importing modules to use in another program
# In this case the modules have been coded to only run when called and not \
# automatically
# This is just an experiment, due to exit() statements in some functions it is \
# possible to end this
# Program without everything having chance to execute

# Comment imports out if you want to test the others
from calendar_maker_module import calender_maker
from guessing_game_module import guesser
from jespers_hi_lo_module import jespers_hi_lo
from hi_lo_module import hi_lo

# Comment functions out if you want to test the others
calender_maker()
guesser()
jespers_hi_lo()
hi_lo()
