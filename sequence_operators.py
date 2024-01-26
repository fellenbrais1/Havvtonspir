
# This code shows examples of concatenation with strings and numerical operations with ints etc
string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

# Simple string concatenation
print(string1 + string2 + string3 + string4 + string5)
print("he's " "probably " "pining " "for the " "fjords")

# Multiplying the output (duplicating) of a string
print("Hello\n" * 5)

# This one doesn't work because you cannot add str to int

# COMMENTED OUT FOR NOW
# print("Hello" * 5 + 4)

# Duplicating the output of a string and then adding one other string at the end
print("Hello" * 5 + "4")

# Operators being used to generate, and maybe test True or False Boolean values
today = "Friday"
print("day" in today)   # returns a Bool value True
print("Fri" in today)   # returns a Bool value True
print("Thur" in today)  # returns a Bool value False
print("parrot" in "fjord")  # returns a Bool value False
