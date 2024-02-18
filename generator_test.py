# This test doesn't work for now, there is still more I need to learn here

from gen_test import *

dave_lister = [
    1,
    2,
    3,
    4,
]

for i in range(len(dave_lister)):
    for num in number_gen():
        print(num)

for x in range(len(dave_lister)):
    order = next(number_gen())
    print(order)
    x += 1


# This is an example from a textbook which works somehow

def incrementer():
    j = 1
    while True:
        yield j
        j += 1


inc = incrementer()

print(next(inc))
print(next(inc))
print(next(inc))
print(next(inc))
