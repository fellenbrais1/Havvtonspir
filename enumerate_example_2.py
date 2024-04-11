# Below is the old code we used to do this an example of unpacking values.
# COMMENTED OUT FOR NOW
# for index, char in enumerate("abcdefgh"):
#     print(index, char)

# These examples show us that the for loop generates a tuple generated from /
# the output from the enumerate function.

# Using one variable 't' to generate tuples which are printed.
for t in enumerate("abcdefgh"):
    print(t)

print("\n-------------------------------------------------------------------\n")

# In this example, we unpack the values in 't' to two other variables to print /
# The output is a bit more readable for the user here.
for t in enumerate("abcdefgh"):
    index, char = t
    print(index, char)

print("\n-------------------------------------------------------------------\n")

# This is an example of the unpacking process.
index, char = (0, "a")
print(index)
print(char)
