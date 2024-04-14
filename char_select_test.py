# This test doesn't work for now, there is still more I need to learn here.

def active_character_select(battlers: list):
    """
    Determines which player character is the active character in a turn.

    This function does not work as intended.
    DO NOT USE.

    :param battlers: A list of battlers that take part in the battle handling.
    :return: 'active_char_list' is yielded by the function.
    """
    max_index = len(battlers) + 1
    while True:
        for item in range(max_index):
            index = item
            print("ITEM IS:", item)
            while index <= max_index:
                active_character = index
                yield active_character
                index += 1
            else:
                exit()


def testo(
        active_turn_list: list,
        battlers: list
):
    """
    A practice function using a generator to determine active player character.

    This function does not work as intended.
    DO NOT USE.

    :param active_turn_list: The player characters involved in battle handling.
    :param battlers: A list of battlers that take part in the battle handling.
    :return: 'active_char_list' is yielded by the function.
    """
    start = 0
    while True:
        for i in range(start, len(battlers)):
            active_character_dict = active_turn_list[i]
            yield active_character_dict
            start += 1
            if i > len(battlers):
                start = 0
