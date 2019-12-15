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
