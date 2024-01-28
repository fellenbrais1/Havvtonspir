
# In this example, we are checking if something is included in a variable
# For example, we are checking to see if a letter is in the string parrot
# If it is in the string it will equate to True, otherwise to False

parrot = "Norwegian Blue"

letter = input("Enter a character: ")
if letter in parrot:
    print("'{}' is in '{}'".format(letter, parrot))
else:
    print("I don't need that letter")
