
# Trying to supply arguments to an imported function to make it use the supplied inputs
try:
    from Storyofyou import storyofyou
except ImportError:
    print("Change the name of your file to something else or check if other problems are occurring")
    exit()

# This code is to specify values to be used by the 'storyofyou' function instead of the default ones
input_name = "Michael"
input_age = "35"
input_hobbies = ["Gaming", "Eating", "Programming"]

# This block of code is to test 'storyofyou' by supplying empty values

# COMMENTED OUT FOR NOW
# input_name = ""
# input_age = ""
# input_hobbies = []

storyofyou(input_name, input_age, input_hobbies)
