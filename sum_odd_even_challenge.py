# A coding challenge written for the Udemy course, this works but not /
# according to the Udemy test evaluator, which is broken as all hell.


def sum_eo(
        provided_n,
        provided_t
):
    """
    Allows the summing of all numbers even or odd up to the specified number.

    This is up to and not including the specified number.
    Contains error handling for incorrect user inputs.

    :param provided_n: User specified value for determining the number to use.
    :param provided_t: User specified value for determining odd or even process.
    :return: 'total' is returned as an int.
    """
    while True:
        if provided_n > 0:
            if provided_t.casefold() == 'e':
                number_list = []
                for i in range(0, provided_n):
                    if i % 2 == 0:
                        number_list.append(i)
                    else:
                        pass
                else:
                    break
            elif provided_t.casefold() == 'o':
                number_list = []
                for i in range(0, provided_n):
                    if i % 2 != 0:
                        number_list.append(i)
                    else:
                        pass
                else:
                    break
            else:
                total = -1
                return total
        else:
            print("That is not a valid number, please enter again.")
            exit()

    total = 0
    for item in number_list:
        total += item
    else:
        return total


n = int(input("Please enter a number: "))
t = input("Please enter letter 'e' or 'o': ")
sum_of_numbers = sum_eo(n, t)
print(sum_of_numbers)
