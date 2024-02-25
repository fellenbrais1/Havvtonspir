# This test doesn't work for now, there is still more I need to learn here

def active_character_select(battlers):
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


def testo(active_turn_list, battlers):
    start = 0
    while True:
        for i in range(start, len(battlers)):
            active_character_dict = active_turn_list[i]
            yield active_character_dict
            start += 1
            if i > len(battlers):
                start = 0
