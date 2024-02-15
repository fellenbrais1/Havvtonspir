# More experimentation with '.sort()' and 'sorted()' and 'list()'
# Also comparisons and '.copy()'

empty_list = []  # Creating an empty list

even = [
    2, 4, 6, 8,
]

odd = [
    1, 3, 5, 7, 9,
]

# You can create a list by concatenating existing lists
numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

# The original is still available as 'sorted()' does not change the original
print(numbers)

# When you create a list from a sequence of characters it will retain the /
# properties of what made it. e.g. 'sorted_numbers' is a list of ints as it /
# was made of ints, 'digits' is a list of strings as it was made of strings
digits = sorted("432985617")
print(digits)

# You can use the 'list' function to create a list from any iterable
# e.g. using a string literal
digits_2 = list("432985617")
print(digits_2)

# e.g. using a variable
more_numbers = list(numbers)
print(more_numbers)

# This code prints out a Bool if things are the same variable or not
print(numbers is more_numbers)

# This code checks if the contents of two variables are the same
print(numbers == more_numbers)

# You can also create a list by using a slice, but this is used in older Python
more_numbers_2 = numbers[:]
print(more_numbers_2)
print(numbers is more_numbers_2)
print(numbers == more_numbers_2)

# You can use the .copy() method instead of a slice as it is more efficient /
# This works in Python 3 and onwards
more_numbers_3 = numbers.copy()
print(more_numbers_3)
print(numbers is more_numbers_3)
print(numbers == more_numbers_3)
