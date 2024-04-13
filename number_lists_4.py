# This is the same as the previous example, but concatenating the two lists \
# we produce a list with the entirety of the second list appended to the end \
# of the other list.

empty_list = []

even = [
    2, 4, 6, 8,
]

odd = [
    1, 3, 5, 7, 9,
]

numbers = even + odd
print(numbers)

for number_list in numbers:
    print(number_list)

# -----------------------------------------------------------------------------

# This adds each item as a list to another list, thus creating a nested list \
# this means that the lists in this list can be iterated over using nested for \
# loops to print out the contents of each one as below.

print()

empty_list_2 = []

even = [
    2, 4, 6, 8,
]

odd = [
    1, 3, 5, 7, 9,
]

numbers = [even, odd]
print(numbers)

# outer loop.
for number_list in numbers:
    print(number_list)
    # inner loop.
    for value in number_list:
        print(value)
