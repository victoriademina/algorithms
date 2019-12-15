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

