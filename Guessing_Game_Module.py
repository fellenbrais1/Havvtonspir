
from random import *


def guesser():
    answer = randint(1, 9)
    guess = 0
    guess_count = 3

    while guess != answer:
        if guess_count == 0:
            print("I am sorry you have run out of guesses")
            print("GAME OVER")
            exit()
        else:
            print("You have {0} guesses left".format(guess_count))
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

            except ValueError:
                print("I'm sorry, please enter a number between 1 and 9 to proceed")
                continue

    print("GAME OVER")


if __name__ == " __main__":
    guesser()
