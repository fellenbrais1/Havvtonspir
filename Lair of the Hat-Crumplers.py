# Experimental text based adventure the Lair of the Hat-Crumplers

# Defining these assets, so they can be re-defined later in the code - class selection/ character names
char1class = 0
char2class = 0
char3class = 0

# Defining the charclass list
charclass = ["Crimper", "Measurer", "Fitter", "Hat Thrower", "Trichomancer"]

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
choice0 = ""
while choice0 != "Y" or "N":
    print("Are you ready to choose your characters?\n")
    choice0 = input("Y/N\t\t")
    if choice0.casefold() == "y":
        print("\nThen let us set start off on a terrifying adventure, \n"
              "but do not say you have not been warned...\n")
        break
    elif choice0.casefold() == "n":
        print("\nThen run away back to your knitting coward! Be gone!\n")
        print("GAME OVER!\n")
        exit()
    else:
        print("\nI'm sorry, please choose between 'Y' and 'N'\n")
        continue

# Character naming and class selection
# There is a lot of duplicate code for characters 1-3, I wonder if this can be done more efficiently

# Character 1
char1name = input("What is the name of your first character?\t")
print("\nWhat class would you like " + char1name.capitalize() + " to be?\n")
# ACTION Is there a character limit needed to be specified for names?
print(char_selection)
(char1type) = 0
while char1type == 0:
    try:
        char1type = int(input("Please type a number...\t"))
    except ValueError:
        char1type = 0
    if char1type in range(1, 6):
        break
    else:
        print("\nI'm sorry, that is not a valid number, please choose from 1-5.\n"
              "Enter 6 to see the class list again.\n")
        if char1type == 6:
            print("\nWhat class would you like " + char1name.capitalize() + " to be?\n")
            print(char_selection)
        char1type = 0
        continue
char1class = charclass[char1type - 1]
print("So be it, " + char1name.capitalize() + " will be a " + char1class + ".\n")

# Character 2
char2name = input("What is the name of your second character?\t\t")
print("\nWhat class would you like " + char2name.capitalize() + " to be?\n")
# Is there a character limit needed to be specified for names?
print(char_selection)
char2type = 0
while char2type == 0:
    try:
        char2type = int(input("Please type a number...\t"))
    except ValueError:
        char2type = 0
    if char2type in range(1, 6):
        break
    else:
        print("\nI'm sorry, that is not a valid number, please choose from 1-5\n"
              "Enter 6 to see the class list again.\n")
        if char2type == 6:
            print("\nWhat class would you like " + char2name.capitalize() + " to be?\n")
            print(char_selection)
        char2type = 0
        continue
char2class = charclass[char2type - 1]
print("So be it, " + char2name.capitalize() + " will be a " + char2class + ".\n")

# Character 3
char3name = input("\nWhat is the name of your third character?\t\t".capitalize())
print("\nWhat class would you like " + char3name.capitalize() + " to be?\n")
# Is there a character limit needed to be specified for names?
print(char_selection)
char3type = 0
while char3type == 0:
    try:
        char3type = int(input("Please type a number...\t"))
    except ValueError:
        char3type = 0
    if char3type in range(1, 6):
        break
    else:
        print("\nI'm sorry, that is not a valid number, please choose from 1-5\n"
              "Enter 6 to see the class list again.\n")
        if char3type == 6:
            print("\nWhat class would you like " + char3name.capitalize() + " to be?\n")
            print(char_selection)
        char3type = 0
        continue
char3class = charclass[char3type - 1]
print("So be it, " + char3name.capitalize() + " will be a " + char3class + ".\n")

# Defining the text displayed from char_list
char_list = char1name.capitalize() + ", the mighty and incomparable " + char1class + ",\n" + char2name.capitalize() \
            + ", the most formidable " + char2class + " this world has ever seen, and,\n" + char3name.capitalize() \
            + ", the most deadly " + char3class + " in the western court.\n".format(charclass)

# Party composition text and start
print("\nYour party is composed of:\n" + char_list)

# Choice1
choice1 = ""
while choice1 != "Y" or "N":
    print("Are you ready to begin your adventure? It's not too late to quit,\n"
          "or to go back and re-select your characters!\n")
    choice1 = input("Y/N\t\t")
    if choice1.casefold() == "y":
        print("\nYour make your way down into the caverns of the hat-crumplers...\n"
              "Moisture drips from walls that seem to press in on your from every side.\n"
              "You can smell the fetid stench of the Hat-Crumplers who have been here recently\n"
              "on the air. The floor is littered with hats that have been crumpled, and you\n"
              "can almost feel the pain of their previous owners, cruelly forced to buy new hats.\n"
              "The terror of such a fate almost stops you in your tracks...")
        break
    elif choice1.casefold() == "n":
        print("\nPlease begin again to re-select your characters!\n"
              "But if cowardice has overtaken your feeble heart then be gone!\n")
        print("PLEASE TRY AGAIN")
        exit()
    else:
        print("\nI'm sorry, please choose between 'Y' and 'N'\n")
        continue

# The hat-crumplers dastardly hat-crumpling trap
input()
print("Suddenly, a hat-crumpling trap springs from the sides of the corridor!\n"
      "You have mere seconds before it ruins your hats!")
input()

if char1class == charclass[0] or char2class == charclass[0] or char3class == charclass[0]:
    print("Ah good! You have a " + charclass[0] + " in your party.\n" +
          "They effortlessly crimp down the edges of a dastardly hat-crumpling trap!\n")
    print("You are safe, for now...")
else:
    print("Good gracious! Without a Crimper present, the hat-crumpling trap thoroughly crumples your hats!\n"
          "\nGAME OVER!\n\nPlease try again!")
    exit()

print("To be continued!")
