import collections


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


def binary_search(arr, x):
    """Find position of an element with the given value in the given sorted list.

    :param arr: sorted list, where lookup should be performed
    :param x: value to search for
    :return: position of an element in arr which has value x
    """

    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            low = mid + 1
        elif x < arr[mid]:
            high = mid - 1
    return None


def multiplication(arr):
    """Return result of multiplication of all elements in the given list.

    :param arr: list to multiply elements
    :return: multiplication of the elements in list arr
    """
    result = 1
    for x in arr:
        result = result * x
    return result


def bfs(graph, source, destination):
    """Finds if the destination is reachable from the source in the graph.

    :param graph: dictionary that represents a graph
    :param source: starting vertex in the graph
    :param destination: ending vertex in the graph
    :return: True if there is a path from the source to the destination in the graph
    """
    search_queue = collections.deque()
    search_queue.append(source)
    visited = []
    while len(search_queue) > 0:
        current = search_queue.popleft()
        if current == destination:
            return True
        for neighbour in graph.get(current, []):
            if neighbour not in visited:
                search_queue.append(neighbour)
                visited.append(neighbour)
    return False
