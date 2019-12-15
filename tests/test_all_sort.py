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
    assert algorithms.quick_sort(l) == expected