def quick_sort(arr):
    """Sorts list using the Quick Sort algorithm.

    :param arr: list which elements should be sorted
    :return: sorted list
    """
    if len(arr) < 2:
        return arr
    else:
        less = []
        more = []
        pivot = arr[0]
        for i in arr[1:]:
            if i >= pivot:
                more.append(i)
            else:
                less.append(i)
        return quick_sort(less) + [pivot] + quick_sort(more)


def __find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    """Sorts list using the Selection Sort algorithm.

    :param arr: list which elements should be sorted
    :return: sorted list
    """
    new_arr = []
    for i in range(len(arr)):
        smallest = __find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr
