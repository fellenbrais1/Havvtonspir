
# Practicing appending to a list using numbered items in a dictionary
# Users can add items to their chosen_list by specifying numbers
# They can confirm the list before purchasing and can also reset the list and /
# delete any items they want from the list
# Added sorting of 'chosen_list' in the code for readability

# Importing needed methods
from time import sleep

# Introduction text
print("\nWelcome to the one-stop computer shop!")
print("Please enter the number of the part you want to add to your shopping "
      "list. \nEnter '0' to review your list and confirm if it's good to go!")
sleep(1.5)

# Defining the necessary variables etc.
# The dictionary can have items added and removed and the program will adapt /
# using the 'max_items' variable based on the dictionary's len
item_dict = {"1": "Computer", "2": "Monitor", "3": "Keyboard", "4": "Mouse",
             "5": "Mouse Mat", "6": "Graphics Card", "7": "Coolant Block",
             "8": "Steering Wheel", "9": "Fan Unit", "10": "Power Supply",
             "11": "Ergonomic Management Keyboard"}

max_items = len(item_dict)

current_choice = "-"

# 'selectable_list' is filled with only the values from the key: value pairs /
# from 'item_dict' to avoid KeyError situations when indexing later
selectable_list = []
for item in item_dict.values():
    selectable_list.append(item)

chosen_list = []

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# The 'computer_parts' list is created to be able to index using the keys in /
# 'item_dict' based on the users numbered choices
computer_parts = []
for item in item_dict.keys():
    computer_parts.append(item)

finished = False

edit = True

# Main loop to enable continuable inputs
while not finished:
    while current_choice != '0':
        if current_choice in computer_parts:
            list_select = int(current_choice)
            print("\nAdding '{0}'".format(selectable_list[list_select - 1]))
            chosen_list.append(selectable_list[list_select - 1])
            sleep(1)
            print("\nYour list so far:")
            letter_count = 0
            chosen_list.sort()
            for item in chosen_list:
                print(letters[letter_count], ".\t", item, sep="")
                letter_count += 1
        else:
            print("\nPlease add options from the list below:")
            i = 1
            for values in item_dict.values():
                print(i, ".\t", values, sep="")
                i += 1
            print("0. To check your list of items before finishing.")
            print("\nPlease type '1' to '{0}' to choose an item or '0' to "
                  "check your list of items before finishing."
                  .format(max_items))

        try:
            edit = True
            current_choice = input(">>> ")
        except ValueError:
            current_choice = "-"
            print("\nPlease enter between '1' and '{0}', or '0' to check your "
                  "list of items before finishing."
                  .format(max_items))
        except IndexError:
            current_choice = "-"
            print("\nPlease enter between '1' and '{0}', or '0' to check your "
                  "list of items before finishing."
                  .format(max_items))
    else:
        print("\nThank you for your selections, your current shopping list is:")
        letter_count = 0
        chosen_list.sort()
        for item in chosen_list:
            print(letters[letter_count], ".\t", item, sep="")
            letter_count += 1
        current_choice = "-"
        sleep(1)
        choice = input("\nAre you happy with this list? Y/N ('E' to edit) "
                       ">>> ")
        choice.casefold()
        if choice == 'y':
            if not chosen_list:
                print("\nIt seems you haven't selected anything yet.")
                print("Please select the items you wish to purchase.")
                sleep(1)
            else:
                print("\nOkay, so let's go to the checkout page!")
                sleep(1)
                finished = True
        # This 'edit' block allows items to be deleted from 'chosen_list' and /
        # it also allows 'chosen_list' to be cleared completely
        elif choice == 'e':
            while edit:
                print("\nYour current shopping list is:")
                letter_count = 0
                chosen_list.sort()
                for item in chosen_list:
                    print(letters[letter_count], ".\t", item, sep="")
                    letter_count += 1
                print("\nWould you like to delete an item or remove all items?")
                print("Please choose 'D' to delete and 'R' to reset the list, "
                      "or enter '0' to cancel.")
                edit_choice = (input(">>> "))
                edit_choice.casefold()
                if edit_choice == 'r':
                    print("\nResetting your list...")
                    sleep(1)
                    chosen_list = []
                    edit_choice = "-"
                    edit = False
                elif edit_choice == 'd':
                    edit_choice = "-"
                    print("\nWhich item would you like to delete, please enter "
                          "its letter to delete it or type a number to cancel.")
                    del_choice = input(">>> ")
                    del_choice = del_choice.upper()
                    if del_choice in letters:
                        try:
                            del_index = letters.index(del_choice)
                            print("\nRemoving {0}."
                                  .format(chosen_list[del_index]))
                            sleep(1)
                            del chosen_list[del_index]
                            del_choice = "-"
                        except IndexError:
                            print("\nThat item is not in your list!")
                            del_choice = "-"
                    elif del_choice == '0':
                        print("\nExiting the edit process...")
                        sleep(1)
                        edit = False
                    else:
                        del_choice = "-"
                elif edit_choice == '0':
                    print("Exiting the edit process...")
                    sleep(1)
                    edit_choice = "-"
                    edit = False
                else:
                    edit_choice = "-"
        elif choice != 'n' and choice != 'y':
            print("\nPlease choose between 'Y' and 'N'.")
            sleep(1)
        else:
            print("\nOkay, let's choose some more items in that case.")
            sleep(1)

# Final 'chosen_list' printing and exit message
print("\nThank you for your purchases today:")
chosen_list.sort()
letter_count = 0
for item in chosen_list:
    print(letters[letter_count], ".\t", item, sep="")
    letter_count += 1
sleep(1)
print("\nWe look forward to serving you again next time.")
