
string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
print("he's " "probably " "pining " "for the " "fjords")

print("Hello\n" * 5)

# this one doesn't work because you cannot add etc to this number in this case
# print("Hello" * 5 + 4)

print("Hello" * 5 + "4")

today = "Friday"
print("day" in today)   # returns a Bool value True
print("Fri" in today)   # returns a Bool value True
print("Thur" in today)  # returns a Bool value False
print("parrot" in "fjord")  # returns a Bool value False
