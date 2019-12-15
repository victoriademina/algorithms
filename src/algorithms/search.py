def find_min(arr):
    """Find value of the minimum element in the given list.

    :param arr: list, on which search will be performed
    :return: value of the minimum element in arr
    """
    result = arr[0]
    for x in arr:
        if x < result:
            result = x
    return result


def find_max(arr):
    """Find value of the maximum element in the given list.

    :param arr: list, on which search will be performed
    :return: value of the maximum element in arr
    """
    result = arr[0]
    for x in arr:
        if x > result:
            result = x
    return result


def sum_list(arr):
    """Return sum of all elements in the given list.

    :param arr: list to sum elements
    :return: sum of the elements in list arr
    """
    result = 0
    for x in arr:
        result = result + x
    return result
