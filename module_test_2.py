# A test of different modules that could be used for a battle handling system.

import operator
from data_test import battlers
from module_test import init


def main_loop() -> None:
    """
    Determines the 'active_name' of the active character in battle handling.

    Function uses this to call 'init()'.
    """
    for battler in battlers:
        active_name = battler
        init(active_name)


def active_turn() -> None:
    """
    Creates 'active_turn_list' by indexing into character data.

    'active_turn_list' is reversed to give usable output. for battle handling.
    """
    active_turn_list = []
    for battler in battlers:
        if 'KO' in battler['statuses']:
            continue
        else:
            battler_initiative = battler['ref'], battler['name'], \
                                 battler['init'], battler['init_mod'], \
                                 battler['statuses']
            active_turn_list.append(battler_initiative)

    active_turn_list = sorted(active_turn_list, key=operator.itemgetter(2),
                              reverse=True)
    print(active_turn_list)


if __name__ == 'main':
    main_loop()
