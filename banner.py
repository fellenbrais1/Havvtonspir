# An example function that does not return anything, but actually performs an \
# action, in this breaking down some text and printing it line by line with \
# custom formatting.


# The 'splitlines()' method splits a specified unit of text into new lines \
# that the code can process.
# I have specified a default value for the provided_width parameter that will \
# be used if no other argument is provided by the code.
def banner_text(
        provided_text=" ",
        provided_width=60
):
    """
    Prints provided text by line with asterisk formatting.

    This function will raise a 'ValueError' if 'provided_text' is too wide for
    the provided_width and crash the function.

    :param provided_text: This is the text that will be fed into the function,
    an asterisk prints a line of asterisks, a space produces an empty line.
    :param provided_width: Specified width to format to, if the text is wider
    than this width a ValueError will be raised.
    :return: Function prints messages and returns 'None'.
    """
    lines = provided_text.splitlines()
    for line in lines:
        if len(line) > provided_width - 4:
            # Added a 'raise ValueError' with a descriptive comment that will \
            # help people to debug the problem.
            raise ValueError("'{0}' is wider than the specified width: '{1}'"
                             .format(provided_text, provided_width))

        if line == "*":
            print("*" * provided_width)
        else:
            output_string = "**{0}**".format(line.center(provided_width - 4))
            print(output_string)


# Text that will be used by the 'banner_text()' function.
text_to_call = """*
Always look on the bright side of life...
If life seems jolly rotten,
There's something you've forgotten!
And that's to laugh and dance and smile and sing,

When you're feeling in the dumps,
Don't be silly chumps,
Just purse your lips and whistle - that's the thing!
And... always look on the bright side of life...
*
"""

# A second text that will be used by the 'banner_text()' function.
text_to_call_2 = """*
The Quartet of Wither
The left hand holds the sword of god,
the right hand palms the book.
The left one grips the reels of line,
the right one baits the hook.
The demon's claw chokes the throat of man,
but the saint's is just as sharp.
The left is for the tools of death,
the right, the lute , the harp.
-Author Unknown
*
"""

# A loop to enable user input for 'screen_width'.
while True:
    screen_width = 60
    try:
        screen_width = int(input("What screen width do you want to print "
                                 "to?: "))
        banner_text(text_to_call, screen_width)
        break
    except ValueError as e:
        if "larger than the specified width" in str(e):
            raise ValueError("'{0}' is wider than the specified width: '{1}'"
                             .format(text_to_call, screen_width))
        else:
            print("Please enter a numerical value for the screen width.")
            continue

# A duplicate of the code above to handle process for 'text_to_call_2', \
# ideally, this would be handled within the function to avoid duplication.
while True:
    screen_width = 60
    try:
        screen_width = int(input("What screen width do you want to print "
                                 "to?: "))
        banner_text(text_to_call_2, screen_width)
        break
    except ValueError as e:
        if "larger than the specified width" in str(e):
            raise ValueError("'{0}' is wider than the specified width: '{1}'"
                             .format(text_to_call_2, screen_width))
        else:
            print("Please enter a numerical value for the screen width.")
            continue

print("\n-------------------------------------------------------------------\n")

banner_text()

print("\n-------------------------------------------------------------------\n")

# This is how we can call the docstring to be printed etc. using '__doc__'.
print(banner_text.__doc__)
print("\n-------------------------------------------------------------------\n")
print(input.__doc__)
print("\n-------------------------------------------------------------------\n")
