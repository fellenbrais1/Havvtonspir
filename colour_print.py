# 'colorama' allows ANSI formatting codes to be used in the terminal without \
# issues for Windows, Mac, and Linux operating systems.
import colorama

# Some ANSI escape sequences for colours and effects
# 'L' = 'light'
WHITE = '\u001b[0;37m'
GRAY = "\033[0;30m"
BLACK = "\033[0;30m"
BROWN = "\033[0;33m"

RED = "\033[0;31m"
YELLOW = '\u001b[0;33m'
BLUE = "\033[0;34m"
GREEN = "\033[0;32m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
MAGENTA = '\u001b[0;35m'

L_GRAY = "\033[0;37m"
L_RED = "\033[1;31m"
L_GREEN = "\033[1;32m"
L_BLUE = "\033[1;34m"
L_PURPLE = "\033[1;35m"
L_CYAN = "\033[1;36m"
L_WHITE = "\033[1;37m"

BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
REVERSE = "\033[7m"
STRIKE = "\033[9m"
COLOR_END = "\033[0m"

RESET = '\u001b[0m'


# A list of ANSI escape code effects that can be exported to other programs.
EFFECT_CONSTANTS = [
    WHITE,
    GRAY,
    BLACK,
    BROWN,
    RED,
    YELLOW,
    BLUE,
    GREEN,
    PURPLE,
    CYAN,
    MAGENTA,
    L_GRAY,
    L_RED,
    L_GREEN,
    L_BLUE,
    L_PURPLE,
    L_CYAN,
    L_WHITE,
    BOLD,
    FAINT,
    ITALIC,
    UNDERLINE,
    BLINK,
    REVERSE,
    STRIKE,
    RESET
    ]


# Some experiments using ANSI escape codes in normal printing.
# ANSI formatting will take until reset, so remember to do this.
print("This will be in red.", RED)
print("This is now reset.", RESET)


# A function to allow easier special printing operations by supplying the code.
# When using a '*arg', you don't need to define a default value as python \
# automatically assigns the default value as None.
def print_special(
        provided_text: str,
        *effect: str
) -> None:
    """
    Allows printing using ANSI escape code formatting.

    Automatically resets the formatting after each call. *arg can accept
    multiple or no arguments.

    :param provided_text: The text fed to this function.
    :param effect: The ANSI formatting escape code.
    """
    print_string = ""
    for arg in effect:
        print_string += arg
    print_string += provided_text
    print(print_string, RESET, sep="")


# The 'colorama' package needs to be initialised before use.
colorama.init()

# Experiments with the 'special_print()' function.
print_special("My name is Michael", L_RED)
print_special("And I live in a Pichael.", MAGENTA)

print_special("I like cheese.", L_GRAY)

print_special("Hello World!", L_CYAN, UNDERLINE, REVERSE)

# The 'colorama' package needs to be de-initialised after use.
colorama.deinit()
