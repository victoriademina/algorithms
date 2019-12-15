import pytest
import algorithms


@pytest.mark.parametrize(
    'arr,expected',
    [
        ([1, 2, 3], 1),
        ([1], 1),
        ([3, 2, 1], 1),
        ([100, -10, -10], -10),
    ]
)
def test_find_min(arr, expected):
    assert algorithms.search.find_min(arr) == expected


@pytest.mark.parametrize(
    'arr,expected',
    [
        ([1, 2, 3], 3),
        ([1], 1),
        ([3, 2, 1], 3),
        ([100, 100, 100], 100),
    ]
)
def test_find_max(arr, expected):
    assert algorithms.search.find_max(arr) == expected


@pytest.mark.parametrize(
    'arr,expected',
    [
        ([1, 2, 3], 6),
        ([1], 1),
        ([-10, 10], 0),
        ([], 0),
    ]
)
def test_sum_list(arr, expected):
    assert algorithms.search.sum_list(arr) == expected


@pytest.mark.parametrize(
    'arr,x,expected',
    [
        ([1, 2, 3, 4, 5], 2, 1),
        ([1, 2, 3], 1, 0),
        ([1], 1, 0),
        ([1, 2, 3], 3, 2),
    ]
)
def test_binary_search(arr, x, expected):
    assert algorithms.search.binary_search(arr, x) == expected


@pytest.mark.parametrize(
    'arr,expected',
    [
        ([1, 2, 3], 6),
        ([1], 1),
        ([-10, 10], -100),
        ([], 1),
    ]
)
def test_multiplication(arr, expected):
    assert algorithms.search.multiplication(arr) == expected
