# A test of different modules that could be used for a battle handling system.

from data_test import battlers_data
from random import randint


def print_statuses() -> None:
    """
    Prints the status list for each active character in battle handling.

    Makes use of the battlers_data dictionary to get data to process.
    """
    a = []
    b = []
    c = []
    d = []
    for i in range(battlers_data + 1):
        for item in [i], ['statuses']:
            a += item
        print(a)
    for item in battlers_data['c_2']['statuses']:
        b += [item]
        print(b)
    for item in battlers_data['c_3']['statuses']:
        c += [item]
        print(c)
    for item in battlers_data['e_1']['statuses']:
        d += [item]
        print(d)
    print(a, b, c, d)


def init(active_name: any) -> None:
    """
    Determines the initiative value of the active character in a list.

    Initiative is based off of the character's 'init' and the generated
    'init_mod' scores summed together with a random int between 0 and 20.

    :param active_name: The active character name fed to the function.
    """
    r = active_name
    if 'slow' in r['statuses']:
        r['init_mod'] \
            = r['speed'] - 20
        r['init'] = r['init_mod'] + randint(0, 20)
        r['init_mod'] = r['init_mod'].__round__()
    elif 'haste' in r['statuses']:
        r['init_mod'] \
            = r['speed'] + 20
        r['init'] = r['init_mod'] + randint(0, 20)
        r['init_mod'] = r['init_mod'].__round__()
    elif 'KO' in r['statuses']:
        r['init_mod'] \
            = 0
        r['init'] = r['init_mod']
    else:
        r['init_mod'] \
            = r['speed'] * 2 / 1.5
        r['init_mod'] = r['init_mod'].__round__()
        r['init'] = r['init_mod'] + randint(0, 20)

    print(r['name'], r['init_mod'])


if __name__ == 'main':
    print_statuses()
    init(active_name=None)
