# This is a very early build of the battle system, which loops around and is \
# comprised of functions calling one another, at the moment it provides a lot \
# of debugging data which would not be present in the finished article, I \
# tried to make it a lot more dependent on the master dictionary, but it \
# seems that having some data in a list is so much easier for indexing.

# A checking function could be called at the end of each turn if the number of \
# active player characters or enemies reaches zero, which would send an \
# argument back to another function somewhere else that handles the ending of \
# battles.

from data_test import battlers, battlers_data as bd
from random import randint
import operator


# This function assigns initiative values to each participant in the battle.
def init():
    """
    Determines the initiative value of the active character in a list.

    Initiative is based off of the character's 'init' and the generated
    'init_mod' scores summed together with a random int between 0 and 20.
    Statuses also affect the generated 'init_mod'.

    :return: Function prints messages, calls 'active_turn()' and returns 'None'.
    """
    print_string = ""
    init_list = []
    for battler in battlers:
        active_name = battler
        an = active_name
        if 'KO' in an['statuses']:
            an['init_mod'] = an['init_mod'] = 0
        elif 'haste' in an['statuses']:
            an['init_mod'] = an['speed'] + 20 + randint(0, 20)
        elif 'slow' in an['statuses']:
            an['init_mod'] = an['speed'] - 20 + randint(0, 20)
        else:
            an['init_mod'] = an['speed'] * 2 / 1.5 + randint(0, 20)
        an['init_mod'] = an['init_mod'].__round__()
        an['init'] = an['init_mod']
        data = an['name'], an['init'], an['statuses']
        init_list.append(data)
    else:
        init_list = sorted(init_list, key=operator.itemgetter(1),
                           reverse=True)
        for item in init_list:
            print_string += str.ljust(item[0] + "'s initiative: ", 30) \
                            + str(item[1]) + "\n"
            if 'KO' in item[2]:
                print_string += "{0} is KOed!\n".format(item[0])
            elif 'slow' in item[2]:
                print_string += "{0} is slowed!\n".format(item[0])
            elif 'haste' in item[2]:
                print_string += "{0}, is moving fast!\n".format(item[0])
    for item in print_string:
        print(item, end="")
    else:
        active_turn()


# This function sorts the 'active_turn_list' based on the initiative values \
# generated in the prior function
def active_turn():
    """
    Creates 'active_turn_list' by indexing into character data.

    'active_turn_list' is reversed to give usable output for battle handling.

    :return: Function prints messages, calls 'battle_turn()' and returns 'None'.
    """
    active_turn_list = []
    for battler in battlers:
        battler_initiative = battler['ref'], battler['name'], \
                             battler['init'], battler['init_mod'], \
                             battler['statuses']
        active_turn_list.append(battler_initiative)

    active_turn_list = sorted(active_turn_list, key=operator.itemgetter(2),
                              reverse=True)
    battle_turn(active_turn_list)


# This function applies damage etc. in order and would probably be changed in \
# future to handle only damage and assigning the 'KO' status, another function \
# should be made to handle the choices player characters and enemies will make \
# and that can call this one when needed
def battle_turn(active_turn_list: list):
    """
    Determines damage taken by battler characters and applies new HP totals.

    Calls 'print_stats()' after execution.

    :param active_turn_list: The list of participating characters in a battle.
    :return: Function prints messages, calls 'print_stats()' and returns 'None'.
    """
    i = 0
    condition = True
    while condition:
        for i in range(len(active_turn_list)):
            active_character_dict = active_turn_list[i]
            print("\nThe active character is: ", active_character_dict[1])
            input(">>>")
            character_ref = (active_character_dict[0])
            cr = character_ref
            print(bd[cr]['name'], "'s HP: ", bd[cr]['current_HP'], sep="")
            if 'KO' in bd[cr]['statuses']:
                print(bd[cr]['name'], 'is knocked out!')
                continue
            else:
                damage = randint(25, 75) - bd[cr]['defence']
                if damage < 0:
                    print('{0} was unharmed!'.format(bd[cr]['name']))
                else:
                    bd[cr]['current_HP'] = bd[cr]['current_HP'] - damage
                    print('{0} took {1} damage!'.format(bd[cr]['name'], damage))
                if bd[cr]['current_HP'] <= 0:
                    print("{0} is KOed!".format(bd[cr]['name']))
                    bd[cr]['current_HP'] = 0
                    bd[cr]['statuses'].append(str('KO'))
                else:
                    print(bd[cr]['name'], 'now has', bd[cr]['current_HP'],
                          'HP!')
                input(">>>")
        i += 1
        if i == len(active_turn_list):
            print()
            condition = False
            print_stats(active_turn_list)


# This is a debugging function to check changes to stats are being applied, \
# but could be repurposed to produce character stats as displayed in a stats \
# screen or menu etc.
def print_stats(active_turn_list: list):
    """
    Prints out a list of status effects for all active battler characters.

    Makes use of the battlers_data dictionary to get data to process.

    :param active_turn_list: The list of participating characters in a battle.
    :return: function prints messages, calls 'print_statuses()' and returns
    'None'.
    """
    stat_list = []
    for i in range(len(active_turn_list) + 1):
        stats = []
        try:
            ref = battlers[i]['ref']
            for k, v in bd[ref].items():
                add = k, v
                stats.append(add)
            else:
                stat_list += (str.ljust(
                    "{0}'s stats: ".format(bd[ref]['name']), 30), stats,)
        except IndexError:
            continue
        except KeyError:
            continue
    else:
        for line in stat_list:
            print(line)
    print()
    print_statuses(active_turn_list)


# This is a debugging function to check changes to statuses are being applied, \
# but could be called later as a 'check party status' action in a menu or in \
# a battle etc.
def print_statuses(active_turn_list: list):
    """
    Prints the status list for each active character in battle handling.

    Makes use of the battlers_data dictionary to get data to process.

    :param active_turn_list: The list of participating characters in a battle.
    :return: Function prints messages, calls 'init()' and returns 'None'.
    """
    statuses_list = []
    for i in range(len(active_turn_list) + 1):
        statuses = []
        try:
            ref = battlers[i]['ref']
            for v in bd[ref]['statuses']:
                statuses += [v]
            else:
                statuses_list += (str.ljust(
                    "{0}'s statuses: ".format(bd[ref]['name']), 30),
                                  statuses)
        except IndexError:
            continue
        except KeyError:
            continue
    else:
        for line in statuses_list:
            print(line)
    print("\nNext turn!\n")
    init()


# This function starts the process for now, but in future it would all be \
# called by the central game engine.
init()
