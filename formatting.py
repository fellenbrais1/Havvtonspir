
# we have specified the width of the string replacement fields using the number after
# the : in the curly braces
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} amd cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

# right align using the > symbol
for i in range(1, 13):
    print("No. {0:>2} squared is {1:>3} amd cubed is {2:>4}".format(i, i ** 2, i ** 3))

# left align using the < symbol
for i in range(1, 13):
    print("No. {0:<2} squared is {1:<3} amd cubed is {2:<4}".format(i, i ** 2, i ** 3))

# center using the caret symbol ^ after the colon
for i in range(1, 13):
    print("No. {0:^2} squared is {1:^3} amd cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

# here we have specified the index value 0, a width reserved of 12, 52, 62, or 72
# the .numf specifies how many floating point numbers we want to generate
print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:<12f}".format(22/7))
print("Pi is approximately {0:<12.50f}".format(22/7))
print("Pi is approximately {0:<52.50f}".format(22/7))
print("Pi is approximately {0:<62.50f}".format(22/7))
print("Pi is approximately {0:<72.50f}".format(22/7))

# the maximum precision Python allows is between 51 and 53 digits
# more than this is not worth specifying
# more digits can be specified but they are only filled with zeroes
print("Pi is approximately {0:<72.54f}".format(22/7))

# if we don't specify field numbers you can't use a field number more than once
# also, they are used in the order they are written into the .format() method
# this cannot be changed without specifying field numbers ourselves
for i in range(1, 13):
    print("No. {} squared is {} amd cubed is {:4}".format(i, i ** 2, i ** 3))
