
from data_test import battlers, battlers_data

for item in battlers_data['c_1']['statuses']:
    print(item)
print(battlers_data['c_1']['statuses'])
for item in battlers_data['c_2']['statuses']:
    print(item)
for item in battlers_data['c_3']['statuses']:
    print(item)
for item in battlers_data['e_1']['statuses']:
    print(item)
print(battlers_data)


def init():
    for name in battlers:
        ref = name
        ref['init_mod'] \
            = ref['speed']
        print(ref['name'], ref['init_mod'])


init()
