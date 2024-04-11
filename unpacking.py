# Using assignments like these allow any changes to only have to be made /
# in one place rather than several.

a = b = c = d = e = f = 42
print(c)

print("\n-------------------------------------------------------------------\n")

# We can also create multiple assignments in this way, just be careful that /
# the order is correct as this could cause annoying to find bugs.
# In this case we are unpacking a tuple, there must be the same amount of /
# values on each side of the assignment otherwise there will be an error.
# The values on the left of the assignment are treated as a tuple because /
# Python makes them into one.

x, y, z = 1, 2, 76
print(x, y, z)

print("\n-------------------------------------------------------------------\n")

# We can specifically create a tuple to make this easier to see. Here, we /
# create the tuple called 'data'.

print("Unpacking a tuple.")

data = (
    1,
    2,
    76,
)

# Then we unpack the contents of data and assign to the variables 'x, y, z'
# In this case, it is data that is the tuple, x, y, z are just variables here.
# Tuples cannot be on both sides of an assignment because tuples are immutable.
x, y, z = data

# Then we print these variables showing that the unpacking has been successful.
print(x)
print(y)
print(z)

print("\n-------------------------------------------------------------------\n")

# We can unpack the values from any sequence type in Python.
# However, if we append or delete an item to this list, the unpacking will /
# fail the next time it runs.

print("Unpacking a list.")

data_list = [
    12,
    13,
    14,
]

p, q, r = data_list
print(p)
print(q)
print(r)
