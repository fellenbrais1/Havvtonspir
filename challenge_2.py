# A coding challenge from a textbook, prompting a user to enter a middle \
# name, a favorite type of pasta, and a number to concatenate into a new \
# password for the user.


def password_creation() -> str:
    """
    Creates a password for a number of user inputs.

    Asks the user for a name, type of pasta, and number and uses these to
    generate a password. Invalid inputs will prompt another entry attempt.

    :return: 'created_password' is returned as a string.
    """
    middle_name = favourite_pasta = number = ""
    loop_count = 0

    print("Now we are going to make you a new password...")

    while loop_count == 0:
        print("\nPlease type your middle name in all letters.")
        middle_name = str(input(">>> "))
        middle_name = middle_name.replace(" ", "")
        middle_name = middle_name.capitalize()
        print("You have typed in: ", middle_name, ".", sep="")
        if middle_name.isalpha():
            print("That middle name is acceptable.")
            loop_count = 1
        else:
            print("That input is not acceptable.")

    while loop_count == 1:
        print("\nPlease type in your favourite type of pasta in all letters.")
        favourite_pasta = str(input(">>> "))
        favourite_pasta = favourite_pasta.replace(" ", "")
        favourite_pasta = favourite_pasta.casefold()
        print("You have typed in: ", favourite_pasta, ".", sep="")
        if favourite_pasta.isalpha():
            print("That answer is acceptable.")
            loop_count = 2
        else:
            print("That input is not acceptable.")

    while loop_count == 2:
        print("\nPlease input a number using only digits.")
        number = str(input(">>> "))
        number = number.replace(" ", "")
        print("You have typed in: ", number, ".", sep="")
        if number.isdigit():
            print("That number is acceptable.")
            loop_count = 3
        else:
            print("That input is not acceptable.")

    while loop_count == 3:
        created_password = middle_name.capitalize() \
                           + favourite_pasta.casefold() \
                           + number.casefold()
        created_password = created_password.replace(" ", "")
        return created_password


password = password_creation()
password_done = False
answer = ""

while not password_done:
    password_done = False
    answer = ""
    while answer != "y" and answer != "n":
        print("Your new password is: ", password, ".", sep="")
        print("Is this password acceptable? (Y) Or would you like "
              "to try again? (N)")
        answer = str(input(">>> "))
        answer = answer.casefold()
    else:
        if answer == "y":
            password_done = True
        elif answer == "n":
            print("Let's try again shall we?")
            answer = ""
            password = password_creation()
        else:
            while answer != "y" and answer != "n":
                print("Please choose between Y and N.")
                answer = str(input(">>> "))
                answer = answer.casefold()
            else:
                answer = ""
else:
    print("Well done, please use the password:", password, "in future.")
    exit()

password_creation()
