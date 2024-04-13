# Using a for loop to iterate through and remove any separators.

number = "9,223;372:036 854,775;807"
# We have to first initialize separators before we add to it later.
separators = ""

# We can use a 'for' loop to iterate through the characters in the 'number' \
# variable.
# If a character is not numeric it will be added to the 'separators' value.
for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in number) \
    .split()
print([int(val) for val in values])

# Using a user specified variable to do the same thing.
number = input("Please enter a series of numbers using any separators "
               "you like: ")
# We have to first initialize separators before we add to it later otherwise \
# there could be issues.
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(
    char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))
