# An experiment in using the .split' method.

panagram = "The quick brown fox jumps over the lazy dog"
print(panagram)

print("\n-------------------------------------------------------------------\n")

# Here the '.split' method is used to split a sentence into words.
# Whitespace is the default thing used as a splitting point.

words = panagram.split()
print(words)

print("\n-------------------------------------------------------------------\n")

# This is just a practice at modifying the output.

vowels = "aeiou"
for word in words:
    for letter in word:
        if letter not in vowels:
            print(letter, end="")
    print()

print("\n-------------------------------------------------------------------\n")

# This is just a practice at modifying the output.

for word in words:
    if word.casefold() != "the":
        print(word)

print("\n-------------------------------------------------------------------\n")

# We can use '.split' to modify long strings of numbers etc.

numbers = "9,223,372,036,854,775,807"
generated_list = numbers.split(",")
print(generated_list)

print()

# However, to do any mathematical operations, we will have to convert each \
# incidence of a string to an int first, this can be done by creating a new \
# list of the converted values, however, this could run into memory problems \
# when dealing with very large lists etc.

int_list = []
for item in generated_list:
    item = int(item)
    int_list.append(item)

for item in int_list:
    print(type(item), item)

print("\n-------------------------------------------------------------------\n")

# Alternatively, we can replace the values with ints in place, this can be \
# more efficient in terms of memory, but you lose the original list, which \
# could be a problem.

for index in range(len(generated_list)):
    generated_list[index] = int(generated_list[index])

print(generated_list)
