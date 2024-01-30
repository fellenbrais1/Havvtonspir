
# Practice code indexing values in a string

#                    1
#         012345678910123
parrot = "Norwegian Blue"

print(parrot)

# Printing from an index of the variable 'parrot'
print(parrot[3])
print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[8])

# Printing more than one index value at the same time and concatenating them
print()
print(parrot[3] + parrot[4])
print(parrot[3] + parrot[6] + parrot[8])

# using negative index values to index the string in reverse order
print()
print(parrot[-1])
print(parrot[-14])

print()
print(parrot[-11])
print(parrot[-10])
print()
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

# This is a slice without a step value
# The top index value goes up to and not including this final value
print(parrot[0:6])  # Norweg
print(parrot[3:5])

# You can omit a number that is just 0 or the maximum number and python can /
# interpret it correctly
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:14])
print(parrot[10:])
print(parrot[0:])
print(parrot[:10])

# If you only have a colon Python will give you a full slice
print(parrot[:])

letters = "abcdefghijklmnopqrstuvwxyz"

print(parrot[-4:-2])    # Bl
print(parrot[-4:12])    # Bl

# Step values go at the end of the slice not the middle
print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw

# An example of using a step value in a slice, it can be used to take out /
# separators like this
number = "9,223,372,036,854,775,807"
print(number[1::4])

number = "9,223;372:036 854,775;807"
print(number[1::4])
# We can then split out these separators
separators = number[1::4]
print(separators)

# This code takes all values not in separators and prints them as joined values
values = "".join(char if char not in separators else " " for char in number)\
    .split()
print([int(val) for val in values])
