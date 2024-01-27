
# 'Guessing_Game' but made into a module that won't run automatically when imported
# Modified the code to make it more robust and handle errors concerning user input
# User can now choose between three difficult options on launch

from random import *


def guesser():
    answer = randint(1, 9)
    difficulty = ['4', '3', '2']
    guess = 0
    guess_count = 0

    print('1. Easy\n2. Medium\n3. Hard')
    ready_1 = True

    while ready_1:
        try:
            difficulty_input = int(input('Choose your difficulty: '))
            try:
                guess_count = difficulty[difficulty_input - 1]
                guess_count = int(guess_count)
                ready_1 = False
            except IndexError:
                print("Please choose your difficulty by typing the numbers 1 (Easy), 2 (Medium), or 3 (Hard)")
            continue
        except ValueError:
            print("Please choose your difficulty by typing the numbers 1 (Easy), 2 (Medium), or 3 (Hard)")

    print("You must guess a number between 1 and 9, you have {0} guesses \nGood luck!".format(guess_count))
    while guess != answer:
        if guess_count == 0:
            print("I am sorry you have run out of guesses")
            print("GAME OVER")
            exit()
        else:
            if guess_count > 1:
                print("You have {0} guesses left".format(guess_count))
            else:
                print("You have {0} guess left".format(guess_count))
            print("Please guess a number between 1 and 10 ")
            try:
                guess = int(input())
                if 0 < guess < 10:
                    if guess == answer:
                        print("Well done, you got the correct guess!")
                        break
                    elif guess < answer:
                        print("You guessed too low!")
                        guess_count -= 1
                    else:
                        print("You guessed too high!")
                        guess_count -= 1
                        continue
                else:
                    print("I'm sorry, please enter a number between 1 and 9 to proceed")
                    continue
            # 'except' handles a ValueError situation and loops back to the input
            except ValueError:
                print("I'm sorry, please enter a number between 1 and 9 to proceed")
                continue

    print("GAME OVER")


# This code causes it not to run automatically and only when called by another program
if __name__ == " __main__":
    guesser()
