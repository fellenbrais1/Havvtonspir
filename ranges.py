
# You can also iterate a for loop over a range
# The range goes from the start value up to but not including the stop value
for i in range(1, 21):
    print("i is now {}".format(i))

# You don't need to specify a start value as it defaults to 0
for i in range(21):
    print(i)

# You can also use a step value as well
for i in range(0, 11, 2):
    print(i)

# You can use a negative step value, but remember to reverse the order of the start and stop value
for i in range(10, 0, -2):
    print(i)

# You can also test if a value is contained within a range or not as the example below
# Most of the time there is a more efficient way to do this but this can be useful too
age = int(input("How old are you? "))

# We need to specify the stop value as one higher than what we need to test for
if age in range(16, 66):
    print("Have a good day at work!")
else:
    print("Enjoy your free time!")
