# An example of creating a simple function and making it configurable by /
# the user.

def multiply(provided_a, provided_b):
    """
    Multiplies two ints together and returns the result.

    parameters must be ints otherwise the function will crash.

    :param provided_a: The first int provided by the user.
    :param provided_b: The second int provided by the user.
    :return: The multiplied int value of provided_a and provided_b.
    """
    result = provided_a * provided_b
    return result


number_a = number_b = 0
print("What numbers would you like to multiply together?\n")
while True:
    try:
        number_a = int(input("What is the first number? "))
        break
    except ValueError:
        print("I am sorry, that is an invalid input, please try again.")
        continue
while True:
    try:
        number_b = int(input("What is the second number? "))
        break
    except ValueError:
        print("I am sorry, that is an invalid input, please try again.")
        continue
answer = multiply(number_a, number_b)
print("\nThe result of multiplying {0} and {1} is {2}"
      .format(number_a, number_b, answer))

print("-----------------------------------------------------------------------")

print("Two times:")
for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)

print("-----------------------------------------------------------------------")


# This function returns a True or False if a string is a palindrome or not.
def is_palindrome(provided_string):
    """
    Checks if 'provided_string' is a palindrome or not and returns True/ False.

    'provided_string' must be str otherwise the function will crash.

    :param provided_string: The string provided to the function.
    :return: True/ False depending on palindromic nature or not.
    """
    return provided_string[::-1].casefold() == provided_string.casefold()


# This function allows a sentence to be stripped down to alnum characters and /
# then checked to see if it is a palindrome using 'is_palindrome().
def is_sentence_palindrome(provided_sentence):
    """
    Creates a new sentence stripped of spaces and punctuation for checking.

    Punctuation and spaces are removed from the 'provided_string' to make
    'new_sentence'.

    :param provided_sentence: The sentence fed to this function.
    :return: 'new_sentence is fed into 'is_palindrome' to check palindromic
    nature, returns True/ False depending on the result.
    """
    new_sentence = ""
    for char in provided_sentence:
        if char.isspace():
            continue
        elif char.isalnum():
            new_sentence += char
        else:
            continue
    print(new_sentence)
    # Instead of duplicating code, we are calling 'is_palindrome()' to work /
    # out if the sentence is a palindrome or not and returning the result here.
    result = is_palindrome(new_sentence)
    return result


word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome.".format(word))
else:
    print("'{}' is not a palindrome.".format(word))

print("-----------------------------------------------------------------------")

string = "rats live on no evil star"
palindrome_result = is_palindrome(string)
print("'{}' is a palindrome?: {}".format(string, palindrome_result))

print("-----------------------------------------------------------------------")

sentence = input("Please enter a sentence to check: ")
if is_sentence_palindrome(sentence):
    print("'{}' is a palindrome.".format(sentence))
else:
    print("'{}' is not a palindrome.".format(sentence))
