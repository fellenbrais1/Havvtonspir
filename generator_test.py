# This test doesn't work for now, there is still more I need to learn here.

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

print("\n-------------------------------------------------------------------\n")

for x in range(len(dave_lister)):
    order = next(number_gen())
    print(order)
    x += 1

print("\n-------------------------------------------------------------------\n")


# This is an example from a textbook which works somehow.
def incrementer():
    """
    Function to yield a number counting up by 1 each time it is called.

    After being yielded, the value of 'j' will increase by 1 for next call.

    :return: 'j' is yielded each time and then added 1 to.
    """
    j = 1
    while True:
        yield j
        j += 1


inc = incrementer()

# Calling on the 'inc' function increases the value of the output by 1 each \
# time.
print(next(inc))
print(next(inc))
print(next(inc))
print(next(inc))
print(next(inc))
print(next(inc))
print(next(inc))
print(next(inc))
print(next(inc))
print(next(inc))
