import algorithms
import pytest


@pytest.mark.parametrize(
    'l,expected',
    [
        ([4, 7, 6, 2, 0], [0, 2, 4, 6, 7]),
        ([5], [5]),
        ([33, 11, 9], [9, 11, 33]),
        ([], []),
    ]
)
def test_quick_sort(l, expected):
    assert algorithms.all_sort.quick_sort(l) == expected


@pytest.mark.parametrize(
    'arr,expected',
    [
        ([1, 2, 3], [1, 2, 3]),
        ([1, 5, 3], [1, 3, 5]),
        ([10, -10], [-10, 10]),
    ]
)
def test_selection_sort(arr, expected):
    assert algorithms.all_sort.selection_sort(arr) == expected
