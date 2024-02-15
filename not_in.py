# In this code we are practicing more with 'in' and 'not in' to test conditions
# Remember that 'not in' reverses the True/False value of something

potential_options = [
    "cinema",
    "gaming",
]

print("The potential options are: ")
for item in potential_options:
    print(item)
activity = input("\nWhat would you like to do today? ")
activity.casefold()

# Using 'in'
if "cinema" in activity:
    print("\nThen lets go to the cinema!")
elif "gaming" in activity:
    print("\nThen it's time to play games!")
else:
    print("\nThen let's do {0} then".format(activity))

# Using 'not in'
if "cinema" and "gaming" not in activity:
    print("\nBut I want to go to the cinema or do some gaming! I don't want "
          "to {0}!".format(activity))
else:
    print("\nThen lets {0}!".format(activity))
