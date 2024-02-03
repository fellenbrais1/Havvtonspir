
# Practicing using the '.extend()' and '.sort()' methods

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
print(even)
another_even = even
print(another_even)

even.sort()
print(even)

# You can use 'sort' to reverse the order of the sorted item like so
even.sort(reverse=True)
print(even)

# You can see that the variable 'another_even' gives us the same output as /
# 'even' as they are two different names for the same list not separate lists
print(another_even)
