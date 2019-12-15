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
