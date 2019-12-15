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
