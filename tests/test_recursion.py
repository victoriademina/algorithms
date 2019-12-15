import pytest
import algorithms


@pytest.mark.parametrize(
    'n,expected',
    [
        (2, 3),
        (5, 15),
        (3, 6),
        (0, 0),
    ]
)
def test_recursive_sum(n, expected):
    assert algorithms.recursion.recursive_sum(n) == expected


@pytest.mark.parametrize(
    'n,expected',
    [
        (2, 1),
        (1, 1),
        (7, 13),
        (0, 0),
    ]
)
def test_fibonacci(n, expected):
    assert algorithms.recursion.fibonacci(n) == expected


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
    assert algorithms.recursion.sum_list(arr) == expected
