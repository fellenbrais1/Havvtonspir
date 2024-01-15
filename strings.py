
print("Today is a good day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
# string concatenation
print("Hello," + " World!")
greeting = "Hello"
name = "Bruce"
print(greeting + name)
print(greeting, name)
# if we want a space we can add that too
print(greeting + " " + name)
# using the input function
name = input("Please enter your name ")
name = name.capitalize()
print(greeting + " " + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

age_in_words = "35-years-old"
print(type(age_in_words))

# the line below will cause an error as we are concatenating an int to a string
# # print(name + " is" + age + " years old")
# you can do this easily using comma separators instead
print(name, "is", age, "years old")

# you can use an f string to do something similar to .format() but potentially even easier
print(name + f" is {age} years old")

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
