
from data_test import battlers, battlers_data


def print_stats():
    a = b = c = d = []
    for item in battlers_data['c_1']['statuses']:
        a += [item]
        # print(item, sep=', ', end='\n',)
    for item in battlers_data['c_2']['statuses']:
        b += [item]
        # print(item, sep=', ', end='\n')
    for item in battlers_data['c_3']['statuses']:
        c += [item]
        # print(item, sep=', ', end='\n')
    for item in battlers_data['e_1']['statuses']:
        d += [item]
        # print(item, sep=', ', end='\n')
    print(a, b, c, d)
    print(battlers_data)


def init(active_name):
    r = active_name
    r['init_mod'] \
        = r['speed']
    print(r['name'], r['init_mod'])


# for battler in battlers:
#     active_name = battler
#     init(active_name)

print_stats()


if __name__ == 'main':
    print_stats()
    init(active_name=None)
