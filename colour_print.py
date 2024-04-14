# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

print(RED, "This will be in red.", sep="")
print(RESET, "This is now reset.", sep="")


def print_special(colour, provided_text):
    """

    :param colour:
    :param provided_text:
    :return:
    """
    print_string = colour + provided_text
    print(print_string, RESET)


print_special(RED, "My name is Michael")
print_special(MAGENTA, "And I live in a Pichael.")

print("I like cheese.")
