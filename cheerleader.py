
# This program accepts a name from the user and then prints it out letter by letter
# This is an example of a for loop iterating through a set of values

name = input("Who do you want to cheer on? ")

# 'name' is formatted to make it easier to handle and to avoid problems with output
name = name.casefold()
name = name.capitalize()
print()

# This for loop iterates through the letters in 'name' and prints them up in uppercase
# If a space in included in the name, no exclamation mark is included for that iteration
for char in name:
    if char == " ":
        print()
    else:
        print(char.upper(), "!")

# I have changed the seperator here to avoid unintended output
print("\n", name, "!", sep="")
