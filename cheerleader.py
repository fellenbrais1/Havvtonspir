# This program accepts a name from the user and then prints it out letter by \
# letter.
# This is an example of a for loop iterating through a set of values.


def cheerleader():
    """
    Function to cheer for someone's name letter by letter.

    This function will accept any string, and ends with an exclamation mark. A
    space will also result in an empty line in the output.

    :return: Function prints messages and returns 'None'.
    """
    from time import sleep
    name = input("Who do you want to cheer on?: ")
    # 'name' is formatted to make it easier to handle and to avoid problems \
    # with output.
    name = name.casefold()
    name = name.capitalize()
    # This for loop iterates through the letters in 'name' and prints them up \
    # in uppercase.
    # If a space in included in the name, no exclamation mark is included for \
    # that iteration.
    for char in name:
        if char == " ":
            print()
            sleep(1)
        else:
            print(char.upper(), "!")
            sleep(1)
    name = name.split()
    print()
    for word in name:
        # I have changed the seperator here to avoid unintended output.
        print(word.title(), sep="", end=" ")
    print("!")


cheerleader()
