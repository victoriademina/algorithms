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


def bubble_sort(arr):
    """Sorts list using the Bubble Sort algorithm.

    :param arr: list which elements should be sorted
    :return: sorted list
    """
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def merge_sort(arr):
    """Sorts list using the Merge Sort algorithm

    :param arr: list which elements should be sorted
    :return: sorted list
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return __merge_arr(left, right)
    return arr


def __merge_arr(left, right):
    new_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_arr.append(left[i])
            i = i + 1
        else:
            new_arr.append(right[j])
            j = j + 1
    while i < len(left):
        new_arr.append(left[i])
        i = i + 1

    while j < len(right):
        new_arr.append(right[j])
        j = j + 1
    return new_arr
