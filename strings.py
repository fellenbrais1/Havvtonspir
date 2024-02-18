# Code to practice printing and concatenating strings

print("Today is a good day to learn Python.")
print('Python is fun!')
print("Python's strings are easy to use.")
print('We can even include "quotes" in strings.')

# String concatenation
print("Hello," + " World!")
greeting = "Hello"
name = "Bruce!"
print(greeting + " " + name)
print(greeting, name)

# If we want a space we can add that too
print(greeting + " " + name)

# Using the input function
name = input("Please enter your name ")
name = name.capitalize()
print(greeting + " " + name)

# Binding a value and then printing it
age = 24
print(age)

print(type(greeting))
print(type(age))

age_in_words = "35-years-old."
print(type(age_in_words))

# The line below will cause an error as we are concatenating an int to a string

# COMMENTED OUT FOR NOW
# # print(name + " is" + age + " years old")

# You can do this easily using comma separators instead
# The comma automatically adds a space, but you can change it by specifying, \
# "sep = ''"
print(name, "is", age, "years old.")

# You can use an f string to do something similar to .format() but potentially \
# even easier
print(name + f" is {age} years old.")

# You can use the '.numf' to specify how many decimal points to return with \
# a float
# The number specified after the ':' specifies the width of display but \
# changing it here does nothing
print(f"Pi is approximately {22 / 7:12.50f}.")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}.")
