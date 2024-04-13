# A collection of activities to check if something is in or not in a string.

a, b, c = 7, 2, 3

print(a, b, c, sep="#", end=".")
print()

print(a + b)
print(a - b)
print(a / b)
print(a // b)
print(a % b)
print(a * b)

print("Your numbers for today are", a, b, "and", c, sep=", ")

if a > b:
    Min = a
else:
    Min = b
print("Minimum =", Min)

if a % b == 0:
    Odd_even = "Even"
else:
    Odd_even = "Odd"
print(Odd_even)

print("\nThis is a test to see if the", "sep and end carry over",
      sep=" this is the sep ", end=".")
print()

List_one = ["Michael", "Time for cheese", "Gromit", 1, "Wallace"]
print()

for item in List_one:
    if item == str:
        print(item)
    else:
        print("Item does not contain characters")
else:
    "This is the end of the list"
