# Experimenting with some common sequence operators.

even = [
    2, 4, 6, 8,
]

odd = [
    1, 3, 5, 7, 9,
]

names = [
    "peony",
    "elleanora",
    "bob",
    "zyzax",
    "a",
]

# 'mixed_list' is an experiment to see if it will work with 'min' and 'max'.
mixed_list = [
    1, 7, 1024, "Bob", 1.665,
    "Alice", "Zyzarro",
]

# 'min' returns the lowest or closest to a and shortest value in a set of
# values.
# 'max' returns the highest or closest to a and longest value in a set of
# values.

print(min(even))
print(max(even))

print()
print(min(odd))
print(max(odd))

print()
print(min(names))
print(max(names))

# 'min' and 'max' do not work for 'mixed_list' as it contains a mixture of \
# elements that cannot be compared with mathematical operators like in these \
# methods.

# COMMENTED OUT FOR NOW.
# print()
# print(min(mixed_list))
# print(max(mixed_list))

# However, 'len' still works with 'mixed_list' as its elements can be counted.
print()
print(len(even))
print(len(odd))
print(len(names))
print(len(mixed_list))

# '.count' returns how many times a value specified in the parentheses occurs \
# in the variable of value it is dot suffixed to.

print()
print("mississippi".count("s"))

# 'iss' returns a value of 2 as it occurs twice in 'mississippi'.
print("mississippi".count("iss"))

# However, 'issi' returns a value of 1, the string 'issi' does occur twice, \
# but as these overlap Python cannot count them independently of one another.
print("mississippi".count("issi"))
