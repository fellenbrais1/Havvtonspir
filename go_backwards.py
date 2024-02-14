# Indexing backwards through a list is a safer way to remove elements without /
# having to worry about the index values shuffling down

# This short loop does the same thing as 'outliers.py' but a bit more /
# efficiently, but there are reasons for the longer program

# If we delete items from a list when iterating backwards we avoid the problems/
# of index values sliding down and causing problems during iteration

# -----------------------------------------------------------------------------
# The first method does this by using a negative start, stop, and slice value /
# in the 'index in range()' statement

data = [
    104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108,
]

min_valid = 100
max_valid = 200

for index in range(len(data) - 1, - 1, - 1):
    print(index)
    if data[index] < min_valid or data[index] > max_valid:
        print(index, data)
        del data[index]

data = sorted(data)
print(data)

# -----------------------------------------------------------------------------
# This second method uses the 'reversed()' function to change the order of the /
# data, so we can then effectively iterate backwards over the list

# This second method is easier to understand and is more efficient because it /
# uses 'enumerate()' which is more efficient than indexes over 1000 items

print()
data = [
    104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108,
]

min_valid = 100
max_valid = 200

# We define a 'top_index - 1' value, so we can use this to reference the index /
# values as if we were indexing forwards, then we can use these values to /
# delete the relevant data from the list instead of using minus index values /
# which would be very confusing
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if data[index] < min_valid or data[index] > max_valid:
        print(top_index - index, data)
        del data[top_index - index]
