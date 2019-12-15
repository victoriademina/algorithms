def recursive_sum(n):
    """Calculates sum from 1 to n.

    :param n: integer to which to sum
    :return: sum of integers from 1 to n
    """
    if n == 0:
        return n
    else:
        return n + recursive_sum(n - 1)


def fibonacci(n):
    """Calculates n-th Fibonacci number.

    :param n: index of a Fibonacci number
    :return: value of the n-th Fibonacci number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
