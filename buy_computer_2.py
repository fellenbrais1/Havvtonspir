
# Another way to generate a list of numbers from a list we could use to test /
# the users input using an 'if choice in valid_choices:' type condition

item_list = ["Computer", "Monitor", "Keyboard", "Mouse",
             "Mouse Mat", "Graphics Card", "Coolant Block",
             "Steering Wheel", "Fan Unit", "Power Supply",
             "Ergonomic Management Keyboard"]

# This code works well with lists, but will not work with unsorted /
# dictionaries, so I still prefer my method for now
# This is called a list comprehension method
# We have to add a '+ 1' here as the final value is not included in the range
valid_choices = [str(i) for i in range(1, len(item_list) + 1)]
print(valid_choices)

# Another way to do the same thing with slightly simpler code
# We have to add a '+ 1' here as the final value is not included in the range
valid_choices_2 = []
for i in range(1, len(item_list) + 1):
    valid_choices_2.append(str(i))
print(valid_choices_2)
