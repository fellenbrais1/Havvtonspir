# Assigning values to a list, a series of values in quotes separated by commas
# In Python, we use '[]' to specify a list

shopping_list = [
    'milk',
    'pasta',
    'eggs',
    'spam',
    'bread',
    'rice',
]

# We can store any type of object in a list in Python
mix_list = [
    6,
    55.22,
    True,
    'pigs in blankets',
]

for item in mix_list:
    print(item, " is: ", type(item))

# One way to exclude an item from the list iteration for loop
# Most people will do this as the 'continue' key word isn't actually used /
# that much
print()
for item in shopping_list:
    if item != "spam":
        print("Buy: ", item)

# Another way to exclude an item from the list iteration for loop
# 'continue' makes all the remaining code in that iteration of the loop /
# to be skipped
print()
for item in shopping_list:
    if item == 'spam':
        continue
    print("Buy: ", item)

# 'break' breaks out of the loop completely and stops anything further from /
# happening there
print()
for item in shopping_list:
    if item == 'spam':
        break
    print("Buy: ", item)
