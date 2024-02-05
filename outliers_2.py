
# Another attempt at this code, this time stopping when reading from the /
# start when a value doesn't need to be deleted, and then stopping when /
# reading from the end when an item doesn't need to be deleted

# TODO Build this code to do what it says above

# min_valid = 100
# max_valid = 200
#
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]
#
# deleting = True
# while deleting:
#     for index, value in enumerate(data):
#         if (value < min_valid) or (value > max_valid):
#             del data[index]
#             break
#     else:
#         deleting = False
# print("Deleting finished...")
# print(data)

# Also, another list of deleted items could be created when scanning the list /
# then these items can be deleted from the list all in one go

# TODO Make this code as well, need a function to delete multiple items from /
# TODO a list object

min_valid = 100
max_valid = 200

data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

list_to_delete = []

deleting = True
while deleting:
    for index, value in enumerate(data):
        if (value < min_valid) or (value > max_valid):
            list_to_delete.append(data[index])
    else:
        for item in data:
            if item in list_to_delete:
                del data(item)
        deleting = False
print("Deleting finished...")
print(data)

print(list_to_delete)
