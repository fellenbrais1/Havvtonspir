
# Another attempt at this code, this time stopping when reading from the /
# start when a value doesn't need to be deleted, and then stopping when /
# reading from the end when an item doesn't need to be deleted

# The code does this by running from the bottom until an item doesn't need to /
# be deleted, then reversing the list and running from the top until an item /
# doesn't need to be deleted, the list is then re-reversed to normal

# Overall, this results in a lot less loops than the other methods (in this /
# use case)

min_valid = 100
max_valid = 200

data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

deleting = True
while deleting:
    for index, value in enumerate(data):
        if value <= min_valid:
            del data[index]
            break
        else:
            deleting = False
            break

data = list(reversed(data))
deleting_2 = True

while deleting_2:
    for index, value in enumerate(data):
        if value <= value >= max_valid:
            del data[index]
            break
        else:
            deleting_2 = False
            break

data = list(reversed(data))

print("\nDeleting finished...")
print("Cleansed data:", data)

# -----------------------------------------------------------------------------

# Also, another list of deleted items could be created when scanning the list /
# then these items can be deleted from the list all in one go

# This code is not really much more efficient than the code above, it still /
# has to constantly re-loop around the code to get a result, and it also has /
# to do another for loop to generate the 'items_to_delete' list

min_valid = 100
max_valid = 200

data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

list_to_delete = []

deleting = True
cleansing = True

while deleting:
    for index, value in enumerate(data):
        if (value <= min_valid) or (value >= max_valid):
            list_to_delete.append(data[index])
    else:
        while cleansing:
            for item in data:
                if item in list_to_delete:
                    data.remove(item)
                    break
                else:
                    continue
            else:
                deleting = False
                cleansing = False

print("\nDeleting finished...")

print("Cleansed data:", data)
print("Elements deleted:", list_to_delete)
