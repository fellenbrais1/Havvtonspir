
# Trying to supply arguments to an imported function to make it use the /
# supplied inputs
try:
    from story_of_you import story_of_you
except ImportError:
    print("Change the name of your file to something else or check if other "
          "problems are occurring")
    exit()
    # This has to be put here to keep the IDE happy but really the next line /
    # of code is unreachable
    from story_of_you import story_of_you

# This code is to specify values to be used by the 'story_of_you' function /
# instead of the default ones
input_name = "Michael"
input_age = "35"
input_hobbies = ["Gaming", "Eating", "Programming"]

# This block of code is to test 'story_of_you' by supplying empty values

# COMMENTED OUT FOR NOW
# input_name = ""
# input_age = ""
# input_hobbies = []

story_of_you(input_name, input_age, input_hobbies)
