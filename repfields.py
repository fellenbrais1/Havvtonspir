
# here we are casting an int to a str so we can concatenate it using +
age = 24
print("My age is " + str(age) + " years")

# .format method is better as you don't need to cast to type first
print("My age is {0} years".format(age))
print("There are {0} days in {1}, {2}, {3}, {5}, {6}, and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct, and Dec".format(31))
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2},"
      "Sep: {1}, Oct: {2}, Nov: {1}, Dec: {1}".format(28, 30, 31))

print("""\nJan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {1}
""".format(28, 30, 31))
