# This test doesn't work for now, there is still more I need to learn here.

from data_test import battlers
from random import randint
import operator


# Initiative order calculation.
def initiative_generator():
    """
    Determines the initiative order of the active characters in battle handling.

    'active_turn_list' is sorted to be useful for determining turn order.

    :return: 'active_turn_list' is returned as a list.
    """
    active_turn_list = []
    for battler in battlers:
        battler_initiative = battler['ref'], battler['name'], \
                             battler['initiative']
        active_turn_list.append(battler_initiative)

    active_turn_list = sorted(active_turn_list, key=operator.itemgetter(2))
    print(active_turn_list)
    return active_turn_list


# Active character in turn generation.
def turn_order():
    """
    Uses the 'active_turn_list' to determine the turn order of characters.

    Once it has run through the list of battlers, a new turn is started.

    :return: Function handles data, prints messages, and returns 'None'.
    """
    while True:
        i = 0
        for i in range(len(battlers)):
            active_character_dict = active_turn_list[i]
            print("The active character is: ", active_character_dict[1])
            input(">>>")
            i += 1
            if i == len(battlers):
                print("\nNext turn!")
                break
                i = 0


for item in battlers:
    item['initiative'] = randint(0, 10)

if __name__ == " __main__":
    initiative_generator()
    turn_order()
