# Changed this program to use the 'get_integer()' function to get user input \
# and validate it before the program uses it.

from random import randint


def guesser() -> None:
    """
    Runs a number guessing game with three levels of difficulty.

    Includes error handling for invalid user inputs.
    """
    highest = 10
    answer = randint(1, highest)

    difficulty = [
        '4',
        '3',
        '2',
    ]

    guess = guess_count = guess_count_max = 0

    print('1. Easy\n2. Medium\n3. Hard')
    ready_1 = True

    while ready_1:
        print("Please choose your difficulty by typing the numbers 1 "
              "(Easy), 2 (Medium), or 3 (Hard).")
        # This calls 'get_integer() to capture user input and validate.
        difficulty_input = get_integer(">>>: ")
        try:
            guess_count = difficulty[difficulty_input - 1]
            guess_count = int(guess_count)
            guess_count_max = guess_count
            ready_1 = False
        # Removed the ValueError check block as the 'get_integer()' function \
        # does this now.
        except IndexError:
            print("That number is invalid, please enter a number "
                  "between 1 and 3.")

    print("You must guess a number between 1 and {1}, you have "
          "{0} guesses. \nGood luck!".format(guess_count, highest))
    print("You can also enter '0' to quit the game.")
    while guess != answer:
        if guess_count == 0:
            print("I am sorry you have run out of guesses!")
            print("GAME OVER!")
            exit()
        else:
            if guess_count > 1:
                print("You have {0} guesses left.".format(guess_count))
            else:
                print("You have {0} guess left.".format(guess_count))
            print("Please guess a number between 1 and {0}.".format(highest))
            try:
                # This calls 'get_integer() to capture user input and validate.
                guess = get_integer(">>>: ")
                if guess == 0:
                    print("See you next time!")
                    exit()
                if 0 < guess < highest + 1:
                    if guess == answer:
                        if guess_count == guess_count_max:
                            print("Well done, you got the correct guess on "
                                  "your first try!")
                            print("You win the grand prize! If we had one!")
                            break
                        else:
                            print("Well done, you got the correct guess!")
                            break
                    elif guess < answer:
                        print("You guessed too low!")
                        guess_count -= 1
                    else:
                        print("You guessed too high!")
                        guess_count -= 1
                else:
                    print("I'm sorry, please enter a number between 1 and "
                          "{0} to proceed.".format(highest))
            except ValueError:
                print("I'm sorry, please enter a number between 1 and {0} "
                      "to proceed.".format(highest))

    print("GAME OVER!")


# This function reads a user input and returns it if the input cannot be \
# changed into an int. This is then called whenever the program needs an input.
def get_integer(prompt: str) -> int:
    """
    Checks if a string is numeric and returns it as an int.

    A non-numeric string will result in another attempt for user input.

    :param prompt: The str user input fed to this function.
    :return: 'temp' as an int for use in the main program.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("'{0}' is not a valid input, please enter a number."
                  .format(temp))


guesser()
