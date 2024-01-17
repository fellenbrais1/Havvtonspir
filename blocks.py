
name = input("What is your name? ")
name = name.capitalize()
age = int(input("How old are you {0}? ".format(name)))
print("You are {0} years old {1}".format(age, name))

# this if code block will make a decision based on a check of the age condition
print()
if age < 18:
    print("Please come back in {0} years".format(18 - age))
else:
    print("You are old enough to vote")
    print("Please put an 'X' in the box")

# we can reverse the order of how we deal with things in any situation, it doesn't really matter
# unless there are some cases where this is very important or it makes sense to do it one way
print()
if age >= 18:
    print("You are old enough to vote")
    print("Please put an 'X' in the box")
else:
    print("Please come back in {0} years".format(18 - age))

# we can also use elif blocks to help us test other coniditions that come up
print()
if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry Yoda you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an 'X' in the box")
