
# Testing True and False conditions and branching outputs
day = str(input("What day is it? "))
temperature = int(input("What is the temperature today? "))
raining = False

# Testing with an if block for True and False values
if day == "Saturday" and temperature > 27 and not raining:
    print("Go swimming")
else:
    print("Learn Python")

# This expression could be vaguely interpreted by the program
if day == "Saturday" and temperature > 27 or not raining:
    print("Go swimming")
else:
    print("Learn Python")

# Use parentheses to make sure the code is being interpreted in the way you /
# want it to be
if (day == "Saturday" and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("Learn Python")

# In this example the IDE throws up a potential problem as a piece of code /
# cannot be reached

# COMMENTED OUT FOR NOW
# if 0:
#     print("True")
# else:
#     print("False")

name = input("Please enter your name: ")
if name:
    print("Hello {}".format(name))
else:
    print("Are you the man with no name?")
