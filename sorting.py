
# Experimenting with the '.sort()' and 'sorted()' functions

pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
for item in letters:
    print(item)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]

# 'sorted()' creates a new list assigned to a different variable, the original /
# list is unchanged. We can also reverse order with '.sorted()' as well'
sorted_numbers = sorted(numbers, reverse=True)
for item in sorted_numbers:
    print(item)

# The '.sort()' method changes the list we called it on
numbers.sort()
print(numbers)

another_sorted_numbers = numbers.sort()
print(numbers)
# This final call returns a value of 'None' as the '.sort()' method doesn't /
# allow a return as the list has already been changed in place and can't be /
# accessed anymore (a little confusing)
print(another_sorted_numbers)

# You can pass a string literal to '.sorted()' without having to pass a variable
missing_letter = sorted("The quick brown fox jumped over the lazy dog")
print(missing_letter)

# Both '.sort()' and '.sorted()' place capital letters in front of lowercase /
# ones.
# If you want to do case-insensitive sorting you can specify that the str /
# should be treated as '.casefold()' as follows:
missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)
print(missing_letter)

names = ["Graham", "John", "terry", "eric", "Terry", "michael"]
names.sort()
print(names)
names.sort(key=str.casefold)
print(names)

# You can't call a variable sorted as it will break code using the '.sorted()' /
# function. It is good practice not to have any variables have the same name /
# as any of the built-in Python functions
