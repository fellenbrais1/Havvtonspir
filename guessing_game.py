# Modified this code to be more robust and to handle error exceptions \
# concerning the input
# User can now choose their difficulty from three options
# Removed unnecessary code (breaks and continues)

# Importing the 'randint' function from the 'random' module to generate \
# random numbers for the 'answer' variable
from random import randint


def guesser():
    # The 'highest' variable allows us to specify what the game plays between \
    # e.g. between 1 and 'highest'
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
        try:
            difficulty_input = int(input('Choose your difficulty: '))
            try:
                guess_count = difficulty[difficulty_input - 1]
                guess_count = int(guess_count)
                guess_count_max = guess_count
                ready_1 = False
            except IndexError:
                (print("Please choose your difficulty by typing the numbers "
                       "1 (Easy), 2 (Medium), or 3 (Hard)."))
        except ValueError:
            (print("Please choose your difficulty by typing the numbers "
                   "1 (Easy), 2 (Medium), or 3 (Hard)."))

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
                guess = int(input())
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
            # 'except' handles a ValueError situation and loops back to the \
            # input
            except ValueError:
                print("I'm sorry, please enter a number between 1 and {0} "
                      "to proceed.".format(highest))

    print("GAME OVER!")


guesser()
