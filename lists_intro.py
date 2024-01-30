
# An example with playing with lists, iterating through them, and adding to them

computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]

print()
for item in computer_parts:
    print(item)

# The user is allowed to add to a list only if it is a new item
# Then the user can break out of the loop and display the amended list
building_list = True
while building_list:
    parts_choice = input("\nWhat do you need for your computer? ")
    parts_choice.casefold()
    if parts_choice == "exit":
        print("Exiting program...")
        exit()
    if parts_choice in computer_parts:
        print("\nYes, that is already on the list")
    else:
        print("\nThat is not on the list, let's add it shall we.")
        computer_parts.append(parts_choice)
    for item in computer_parts:
        print(item)
    print("\nWould you like to add more parts?")
    choice = ""
    while choice == "":
        choice = input("'y' or 'n'? ")
        choice.casefold()
        if choice == "y":
            break
        elif choice != "n" and "y":
            print("Please type either 'y' or 'n'.")
            choice = ""
        else:
            print("Okay, that's enough parts for now I guess.")
            building_list = False
            break

print("\nYour final computer parts list is:")
for item in computer_parts:
    print(item)

# Testing indexing a list
print("\nThe salesman recommends that you buy a '{0}' first".format(computer_parts[1]))

# Practicing slicing a list
print("\nI recommend all of the following:")
for item in computer_parts[0:3]:
    print(item)
print()
for item in computer_parts[:-1]:
    print(item)
print()
for item in computer_parts[0::2]:
    print(item)

# Practicing sub-indexing a list
print("\nThe first letter of the third item is:", computer_parts[2][0])
