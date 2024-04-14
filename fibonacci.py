# Practice writing a sequence to iterate through the Fibonacci sequence.


def fibonacci(n: int) -> int:
    """
    Generates a cumulative printed addition using the Fibonacci sequence.

    Numbers will add together as per the sequence and print out the number each
    iteration of the sequence.

    :param: n: The number of times you want to iterate through the sequence.
    :return: 'result'.
    """

    if 0 <= n <= 1:
        return n

    n_minus_1, n_minus_2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus_2 + n_minus_1
        n_minus_2 = n_minus_1
        n_minus_1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))
