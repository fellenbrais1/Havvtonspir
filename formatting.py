
# Examples of using the '.format()' method in code to replace strings with values
# We have specified the width of the string replacement fields using the number after
# The ':' in the curly braces
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} amd cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

# Right align using the > symbol
for i in range(1, 13):
    print("No. {0:>2} squared is {1:>3} amd cubed is {2:>4}".format(i, i ** 2, i ** 3))

# Left align using the < symbol
for i in range(1, 13):
    print("No. {0:<2} squared is {1:<3} amd cubed is {2:<4}".format(i, i ** 2, i ** 3))

# Center using the caret symbol ^ after the colon
for i in range(1, 13):
    print("No. {0:^2} squared is {1:^3} amd cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

# Here we have specified the index value 0, a width reserved of 12, 52, 62, or 72
# '.numf' specifies how many floating point numbers we want to generate
print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:<12f}".format(22/7))
print("Pi is approximately {0:<12.50f}".format(22/7))
print("Pi is approximately {0:<52.50f}".format(22/7))
print("Pi is approximately {0:<62.50f}".format(22/7))
print("Pi is approximately {0:<72.50f}".format(22/7))

# The maximum precision Python allows is between 51 and 53 digits
# More than this is not worth specifying
# More digits can be specified, but they are only padded with zeroes
print("Pi is approximately {0:<72.54f}".format(22/7))

# If we don't specify field numbers you can't use a field number more than once
# Also, they are used in the order they are written into the '.format()' method
# This cannot be changed without specifying field numbers ourselves
for i in range(1, 13):
    print("No. {} squared is {} amd cubed is {:4}".format(i, i ** 2, i ** 3))
