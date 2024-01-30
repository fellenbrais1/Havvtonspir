
# A coding challenge from a textbook, it makes the user suggest a word /
# starting with a letter of the alphabet, printing it out as an increasingly /
# long string until the end of the alphabet

print("Let's play \"Let's go to the market today!\"")
print("You have to say \"I went to the market today and bought a [thing]\" "
      "starting with the current letter of the alphabet")


def went_market():
    # Starting letter = "a"
    # Starting ord value = 97
    ord_value = 97
    base_list = "I went to the market today and bought an "
    shopping_list = base_list
    vowel_set = ["a", "e", "i", "o", "u"]

    while ord_value <= 122:
        print("")
        letter_value = ord_value
        current_letter = chr(letter_value)
        print("Current letter is:", current_letter)
        input_message = "Enter an item starting with {0}: "\
            .format(current_letter)
        current_item = (str(input(input_message)))
        current_item = current_item.lower()
        current_item = current_item.lstrip()
        current_item = current_item.rstrip()
        if current_item.startswith(current_letter):
            shopping_list = shopping_list + current_item
            print(shopping_list)
            ord_value += 1
            letter_value = ord_value
            current_letter = chr(letter_value)
            if ord_value == 123:
                continue
            else:
                if current_letter in vowel_set:
                    shopping_list = shopping_list + " and an "
                else:
                    shopping_list = shopping_list + " and a "
        else:
            print("That doesn't start with {0}! Please try again.".format
                  (current_letter))
            ord_value = ord_value
    else:
        print("You have completed the game! Your completed shopping list is:")
        print(shopping_list)
        exit()


went_market()
