
# Experimenting with the'.index()' method and the 'enumerate' function

# '.index()' method
# Sadly, '.index()' does not work with dictionaries unless transformation of /
# the data into lists etc. happens first

stuff_list = ["tops", "caps", "tappers"]
stuff_dict = {"1": "taps", "2": "cops", "3": "tupperware"}

# Testing the '.index()' method
print(stuff_list.index("caps"))

print()
for item in stuff_list:
    print(stuff_list.index(item) + 1, ". ", item, sep="")

# Changing the dictionary 'stuff_dict' into two lists to be indexed from
# This first one isn't particularly useful at the moment
stuff_dict_keys = []
for key in stuff_dict.keys():
    stuff_dict_keys.append(key)

# This list is more useful at the moment as the numbers can be generated some /
# other way without referencing the dictionary
stuff_dict_values = []
for value in stuff_dict.values():
    stuff_dict_values.append(value)

# This uses the index value of each item +1 to generate numbers we can use
print()
for item in stuff_dict_values:
    print(stuff_dict_values.index(item) + 1, ". ", item, sep="")

# Alternatively, an 'i' value can be specified and have one added to it each /
# loop for the same effect
# I think this is easier for now if the numbers in the list etc. have no real /
# meaning to use
print()
i = 0
for item in stuff_dict:
    print(stuff_dict_keys[i], ". ", stuff_dict[item], sep="")
    i += 1

# 'enumerate' function
# We can also use the 'enumerate' function to return an index value along with /
# an item, this is the most efficient way to do this in terms of computing /
# power and time
print("\n'enumerate' function test")
for number, item in enumerate(stuff_dict_values):
    print(number + 1, ". ", item, sep="")

# This could be a way of printing out a list and its index values for testing /
# purposes, so you know what to index in the future
print("\nAnother 'enumerate' function test")
for item in enumerate(stuff_dict_values):
    print(item)

print("\nFinal 'enumerate' function test")
stuff_dict_values.sort()
for item in enumerate(stuff_dict_values):
    print(item)
