# This file demonstrates using nested for loops, usually 'i' and 'j' are \
# values used here.

for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2}".format(j, i, i * j))
    print("-------------")
