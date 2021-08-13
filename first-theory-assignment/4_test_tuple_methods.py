import pytest


@pytest.mark.me
def test_count():
    """
    This method returns the number of times a specified value appears in the tuple
    """
    numbers = (1, 3, 5, 7, 9, 3, 7, 9, 7, 9, 9)
    assert numbers.count(9) == 4


def test_index():
    """
    This method finds the first time a specified value occurs in the tuple.
    If the item doesn't appear it raises an exception.
    """
    numbers = (1, 3, 5, 7, 9, 3, 7, 9, 7, 9, 9)
    assert numbers.index(5) == 2
