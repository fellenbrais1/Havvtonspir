# Experimental text based adventure the Lair of the Hat-Crumplers

# Defining these assets, so they can be re-defined later in the code - class selection/ character names
char_1_class = 0
char_2_class = 0
char_3_class = 0

# Defining the char_class list
char_class = ["Crimper", "Measurer", "Fitter", "Hat Thrower", "Trichomancer"]

# The character selection text to be displayed
char_selection = ("1.Crimper - A mighty crimper of edges and disarmer of traps\n"
                  "2.Measurer - A mighty combatant who measures up their opponents\n"
                  "3.Fitter - An agile fitter of hats and accessories\n"
                  "4.Hat Thrower - A deadly arm with hats for all\n"
                  "5.Trichomancer - A wielder of powerful scalp-itching magic\n")

# Introduction
print("\nWelcome, player, to the chilling tale of the \"Lair of the Hat-Crumplers\", prepare for danger\n"
      "amazement, wonder, and much much more!\n\n"
      "\t\t___________________________\n"
      "\t\t!                         /\n"
      "\t\t!          LAIR          /\n"
      "\t\t!           OF           \\\n"
      "\t\t \\        THE HAT         !\n"
      "\t\t /       CRUMPLERS        !\n"
      "\t\t!                         !\n"
      "\t-----------------------------------\n")

input("Please press enter to continue...")
print("\nThe kingdom of Bromsgrove is in need of help! The evil Hat-Crumplers have taken\n"
      "over the dungeons under the city, and are using them to continue their reign of\n"
      "hat-crumpling terror. Not a hat in the land is safe!")
input()
print("A team of three of the kingdom's finest should be able to enter the dungeons and\n"
      "stop the Hat-Crumplers once and for all. Will you be the ones to stop them?\n")

# Choice0, starting the game
choice_0 = ""
while choice_0 != "Y" or "N":
    print("Are you ready to choose your characters?\n")
    choice_0 = input("Y/N\t\t")
    if choice_0.casefold() == "y":
        print("\nThen let us set start off on a terrifying adventure, \n"
              "but do not say you have not been warned...\n")
        break
    elif choice_0.casefold() == "n":
        print("\nThen run away back to your knitting coward! Be gone!\n")
        print("GAME OVER!\n")
        exit()
    else:
        print("\nI'm sorry, please choose between 'Y' and 'N'\n")
        continue

# Character naming and class selection
# There is a lot of duplicate code for characters 1-3, I wonder if this can be done more efficiently

# Character 1
char_1_name = input("What is the name of your first character?\t")
print("\nWhat class would you like " + char_1_name.capitalize() + " to be?\n")
# ACTION Is there a character limit needed to be specified for names?
print(char_selection)
(char_1_type) = 0
while char_1_type == 0:
    try:
        char_1_type = int(input("Please type a number...\t"))
    except ValueError:
        char_1_type = 0
    if char_1_type in range(1, 6):
        break
    else:
        print("\nI'm sorry, that is not a valid number, please choose from 1-5.\n"
              "Enter 6 to see the class list again.\n")
        if char_1_type == 6:
            print("\nWhat class would you like " + char_1_name.capitalize() + " to be?\n")
            print(char_selection)
        char_1_type = 0
        continue
char_1_class = char_class[char_1_type - 1]
print("So be it, " + char_1_name.capitalize() + " will be a " + char_1_class + ".\n")

# Character 2
char_2_name = input("What is the name of your second character?\t\t")
print("\nWhat class would you like " + char_2_name.capitalize() + " to be?\n")
# Is there a character limit needed to be specified for names?
print(char_selection)
char_2_type = 0
while char_2_type == 0:
    try:
        char_2_type = int(input("Please type a number...\t"))
    except ValueError:
        char_2_type = 0
    if char_2_type in range(1, 6):
        break
    else:
        print("\nI'm sorry, that is not a valid number, please choose from 1-5\n"
              "Enter 6 to see the class list again.\n")
        if char_2_type == 6:
            print("\nWhat class would you like " + char_2_name.capitalize() + " to be?\n")
            print(char_selection)
        char_2_type = 0
        continue
char_2_class = char_class[char_2_type - 1]
print("So be it, " + char_2_name.capitalize() + " will be a " + char_2_class + ".\n")

# Character 3
char_3_name = input("\nWhat is the name of your third character?\t\t".capitalize())
print("\nWhat class would you like " + char_3_name.capitalize() + " to be?\n")
# Is there a character limit needed to be specified for names?
print(char_selection)
char_3_type = 0
while char_3_type == 0:
    try:
        char_3_type = int(input("Please type a number...\t"))
    except ValueError:
        char_3_type = 0
    if char_3_type in range(1, 6):
        break
    else:
        print("\nI'm sorry, that is not a valid number, please choose from 1-5\n"
              "Enter 6 to see the class list again.\n")
        if char_3_type == 6:
            print("\nWhat class would you like " + char_3_name.capitalize() + " to be?\n")
            print(char_selection)
        char_3_type = 0
        continue
char_3_class = char_class[char_3_type - 1]
print("So be it, " + char_3_name.capitalize() + " will be a " + char_3_class + ".\n")

# Defining the text displayed from char_list
char_list = char_1_name.capitalize() + ", the mighty and incomparable " + char_1_class + \
            ",\n" + char_2_name.capitalize() \
            + ", the most formidable " + char_2_class + " this world has ever seen, and,\n" + char_3_name.capitalize() \
            + ", the most deadly " + char_3_class + " in the western court.\n".format(char_class)

# Party composition text and start
print("\nYour party is composed of:\n" + char_list)

# Choice1
choice_1 = ""
while choice_1 != "Y" or "N":
    print("Are you ready to begin your adventure? It's not too late to quit,\n"
          "or to go back and re-select your characters!\n")
    choice_1 = input("Y/N\t\t")
    if choice_1.casefold() == "y":
        print("\nYour make your way down into the caverns of the hat-crumplers...\n"
              "Moisture drips from walls that seem to press in on your from every side.\n"
              "You can smell the fetid stench of the Hat-Crumplers who have been here recently\n"
              "on the air. The floor is littered with hats that have been crumpled, and you\n"
              "can almost feel the pain of their previous owners, cruelly forced to buy new hats.\n"
              "The terror of such a fate almost stops you in your tracks...")
        break
    elif choice_1.casefold() == "n":
        print("\nPlease begin again to re-select your characters!\n"
              "But if cowardice has overtaken your feeble heart then be gone!\n")
        print("PLEASE TRY AGAIN")
        exit()
    else:
        print("\nI'm sorry, please choose between 'Y' and 'N'\n")
        continue

# The hat-crumplers' dastardly hat-crumpling trap
input()
print("Suddenly, a hat-crumpling trap springs from the sides of the corridor!\n"
      "You have mere seconds before it ruins your hats!")
input()

if char_1_class == char_class[0] or char_2_class == char_class[0] or char_3_class == char_class[0]:
    print("Ah good! You have a " + char_class[0] + " in your party.\n" +
          "They effortlessly crimp down the edges of a dastardly hat-crumpling trap!\n")
    print("You are safe, for now...")
else:
    print("Good gracious! Without a Crimper present, the hat-crumpling trap thoroughly crumples your hats!\n"
          "\nGAME OVER!\n\nPlease try again!")
    exit()

print("To be continued!")
