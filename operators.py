# An example of the mathematical operators that can be used in Python

a = 12
b = 3

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a / b)  # Division produces a float result
print(a // b)  # Integer division produces an int result
print(a * b)  # Multiplication
print(a % b)  # Modulo division, the remainder after integer division
print(a ** b)  # Exponent operator (raising a number to a power specified)

print()

for i in range(1, 4):
    print(i)

# The below example wouldn't work because it is using a float instead of an \
# int after division

# COMMENTED OUT FOR NOW
# for i in range(1, a / b):
#     print(i)

# This code would work as integer division returns an int which can be used \
# in a range
for i in range(1, a // b):
    print(i)

# You shouldn't code like this as it is very wasteful and verbose
i = 1
print(i)
i = 2
print(i)
i = 3
print(i)

# This expression won't give the desired result due to operator precedence
# Change the order you want an equation to run in by adding or removing \
# parentheses
print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print(a / (b * a) / b)
