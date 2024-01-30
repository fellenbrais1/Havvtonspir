
# This code shows that we can use a for loop to find a variable in a list
shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

print(shopping_list)
item_to_find = input('\nWhat item would you like to find?: ')
item_to_find = item_to_find.casefold()

# This was replaced by a user function that can specify this instead

# COMMENTED OUT FOR NOW
# item_to_find = 'spam'

# Here we bind the found_at variable to None to avoid errors later on in the /
# program
# This could be in a situation where an item is not found in the list for /
# example
found_at = None

# Breaking out of the loop means we don't need to do any processing once the /
# desired result is found
for index in range(len(shopping_list)):
    if shopping_list[index].casefold() == item_to_find:
        found_at = index
        break

# To print a message if the specified value is found or not found in the list
if found_at is not None:
    print('\'{0}\' found at position {1}'.format(item_to_find, found_at))
else:
    print('\'{0}\' not found in the list!'.format(item_to_find))

# This is an alternative and much more efficient way of doing this operation /
# in Python

# COMMENTED OUT FOR NOW
# if item_to_find in shopping_list:
#     found_at = shopping_list.index(item_to_find)
# else:
#     print('\'{0}\' not found in the list!'.format(item_to_find))
