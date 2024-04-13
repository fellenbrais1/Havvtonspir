# This code imports code from another file to be used here.

from guessing_game_module import guesser

# Statements to collect the user's data.
name = input("What is your name? ")
name = name.capitalize()
age = int(input("How old are you {0}? ".format(name)))
print("You are {0} years old {1}.".format(age, name))

# This if code block will make a decision based on a check of the age condition.
print()
if age < 18:
    print("Please come back in {0} years.".format(18 - age))
else:
    print("You are old enough to vote.")
    print("Please put an 'X' in the box.")

# We can reverse the order of how we deal with things in any situation, it \
# doesn't really matter.
# Unless there are some cases where this is very important or if it makes \
# sense to do it one way.
print()
if age >= 18:
    print("You are old enough to vote.")
    print("Please put an 'X' in the box.")
else:
    print("Please come back in {0} years.".format(18 - age))

# We can also use elif blocks to help us test other conditions that come up.
print()
if age < 18:
    print("Please come back in {0} years.".format(18 - age))
elif age == 900:
    print("Sorry Yoda, you die in Return of the Jedi!")
else:
    print("You are old enough to vote.")
    print("Please put an 'X' in the box.")

print()

# This is a callback to the function imported in the import code at the top.
guesser()
