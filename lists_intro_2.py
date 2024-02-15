# Replacing items in a list with indexing and slices

computer_parts = [
    "computer",
    "monitor",
    "keyboard",
    "mouse",
    "mouse mat",
]

print(computer_parts)

# replacing a value in a list using an index position
computer_parts[3] = "trackball"
print(computer_parts)

# printing a slice from 'computer_parts'
print(computer_parts[3:])

# Replacing items in a list using a slice
# In this example, each letter of the new assignment is treated as a new list /
# this means we get a slightly odd result and output
computer_parts[3:] = "trackball"
print(computer_parts)

# If we put the item to be added as a list element, it will only add one new /
# list item to the existing list
computer_parts[3:] = ["trackball"]
print(computer_parts)

# This replaces up to and including the slice end value with the specified list
computer_parts = [
    "computer",
    "monitor",
    "keyboard",
    "mouse",
    "mouse mat",
]

computer_parts[0:2] = [
    "sodium",
    "calcium",
    "ceasium",
]

print(computer_parts)
