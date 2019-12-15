def recursive_sum(n):
    """Calculates sum from 1 to n.

    :param n: integer to which to sum
    :return: sum of integers from 1 to n
    """
    if n == 0:
        return n
    else:
        return n + recursive_sum(n - 1)
