
a = 12
b = 3

print(a + b)    # addition
print(a - b)    # subtraction
print(a / b)    # division produces a float result
print(a // b)   # integer division produces an int result
print(a * b)    # multiplication
print(a % b)    # modulo division, the remainder after integer division
print(a ** b)   # exponent operator (raising a number to a power specified)

print()

for i in range(1,4):
    print(i)

# the below example wouldn't work because it is using a float instead of an int after division
# for i in range(1, a / b):
#     print(i)

# this one would work as integer division returns an int which can be used in a range
for i in range(1, a // b):
    print(i)

# you shouldn't code like this as it is very wasteful and verbose
i = 1
print(i)
i = 2
print(i)
i = 3
print(i)

# This expression won't give the desired result due to operator precedence
print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print(a / (b * a) / b)
