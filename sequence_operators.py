# This code shows examples of concatenation with strings and numerical \
# operations with ints etc.

string_1 = "He's "
string_2 = "probably "
string_3 = "pining "
string_4 = "for the "
string_5 = "fjords."

# Simple string concatenation.
print(string_1
      + string_2
      + string_3
      + string_4
      + string_5)
print("He's " "probably " "pining " "for the " "fjords.")

# Multiplying the output (duplicating) of a string.
print("Hello\n" * 5)

# This one doesn't work because you cannot add str to int.

# COMMENTED OUT FOR NOW
# print("Hello" * 5 + 4)

# Duplicating the output of a string and then adding one other string at the \
# end.
print("Hello" * 5 + "4")

# Operators being used to generate, and maybe test True or False Boolean \
# values.
today = "Friday"
print("day" in today)  # returns a Bool value True.
print("Fri" in today)  # returns a Bool value True.
print("Thur" in today)  # returns a Bool value False.
print("parrot" in "fjord")  # returns a Bool value False.
