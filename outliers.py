# Practising deleting items from a list.

data = [
    4, 5, 104, 105, 110,
    120, 130, 130, 150, 160,
    170, 183, 185, 187, 188,
    191, 350, 360,
]

# Deleting the first two values because their values are too low.
del data[0:2]
print(data)

# Deleting the last two elements because their values are too large.
data = [
    4, 5, 104, 105, 110,
    120, 130, 130, 150, 160,
    170, 183, 185, 187, 188,
    191, 350, 360,
]

del data[16:]
print(data)

# If the first two elements of the list were already removed, you would have \
# to change the index value to remove items from the end as the index numbers \
# have all shifted down to accommodate the shorter list.

data = [
    4, 5, 104, 105, 110,
    120, 130, 130, 150, 160,
    170, 183, 185, 187, 188,
    191, 350, 360,
]

del data[0:2]
print(data)
del data[14:]
print(data)

# OR we can use a minus slice to always be able to take the last two values \
# from the list regardless of whether any elements have been removed before.
data = [
    4, 5, 104, 105, 110,
    120, 130, 130, 150, 160,
    170, 183, 185, 187, 188,
    191, 350, 360,
]

del data[-2:]
print(data)

# We could set some 'min' and 'max' values to test if a value is within the \
# desired range and then delete them if they are not within that range.
min_valid = 100
max_valid = 200

data = [
    4, 5, 104, 105, 110,
    120, 130, 130, 150, 160,
    170, 183, 185, 187, 188,
    191, 350, 360,
]

for index, value in enumerate(data):
    if (value < min_valid) or (value > max_valid):
        del data[index]

print(data)

# This code does not work because the size and index values of the list are \
# changed every time there is a change made to the list.
# This means that some items will be skipped because of the index \
# reassignments and the way that Python iterates through the code.
# Be very careful when changing the size of a list that you are iterating over.

# You can't mess with the execution of a for loop in python like you can in \
# some other languages, for example you shouldn't change the index value \
# manually in Python as it always causes a lot of problems.

# This can cause big problems when trying to automate processes in python.

# I found a way to automate this successfully using a loop that runs in a \
# loop until there is nothing else to be deleted. This works but is probably \
# very inefficient in terms of computing power.
print()

min_valid = 100
max_valid = 200

data = [
    4, 5, 104, 105, 110,
    120, 130, 130, 150, 160,
    170, 183, 185, 187, 188,
    191, 350, 360,
]

deleting = True
while deleting:
    for index, value in enumerate(data):
        if (value < min_valid) or (value > max_valid):
            del data[index]
            break
    else:
        deleting = False
print("Deleting finished...")
print(data)

min_valid = 100
max_valid = 200

data = [
    4, 5, 104, 105, 110,
    120, 130, 130, 150, 160,
    170, 183, 185, 187, 188,
    191, 350, 360,
]

stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print("\nStop value:", stop)
del data[:stop]
print(data)

# -----------------------------------------------------------------------------

# Processing the high values in the list.
min_valid = 100
max_valid = 200

data = [
    104, 105, 110, 120, 130,
    130, 150, 160, 170, 183,
    185, 187, 188, 191, 350,
    360,
]

# This is a way to index backwards through a list, using a start and stop \
# value of -1 and a step value of -1.
start = 0
for index in range(len(data) - 1, - 1, - 1):
    # To check it is iterating backwards properly.
    # COMMENTED OUT FOR NOW.
    # print(index)
    if data[index] <= max_valid:
        start = index + 1
        break

# This code does the same as what we did with the low values, we change the \
# index value to generate a deletion slice we can use, adding 1 to make sure \
# we do not delete the value that actually represents the start value.
# Start represents from where we should start deleting from, but not including \
# this piece of data.

print("Start value:", start)  # For debugging.
del data[start:]
print(data)
