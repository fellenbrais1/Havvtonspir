# A coding challenge from a textbook asking for three numbers which it /
# then multiplies together

print("")
print(100 + 200)
a, b = 10, 100
print(a * b)

number_a = ""
number_b = ""
number_c = ""

loop_count = 0
while loop_count == 0:
    number_a = input("\nWhat number will you choose for a? ")
    if number_a.isdigit():
        loop_count = 1
    else:
        print("That is not a number, please try again:")
        loop_count = 0
while loop_count == 1:
    number_b = input("\nWhat number will you choose for b? ")
    if number_b.isdigit():
        loop_count = 2
    else:
        print("That is not a number, please try again:")
        loop_count = 1
while loop_count == 2:
    number_c = input("\nWhat number will you choose for c? ")
    if number_c.isdigit():
        loop_count = 3
    else:
        print("That is not a number, please try again:")
        loop_count = 2

if loop_count == 3:
    number_a = int(number_a)
    number_b = int(number_b)
    number_c = int(number_c)
    print("\na times b =", number_a * number_b)
    print("\nb times c =", number_b * number_c)
    print("\nAll the numbers multiplied together are =", (number_a * number_b)
          * number_c)

print('\n"One",\t\\Two\n\t\t"Three"')
