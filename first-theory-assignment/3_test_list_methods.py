import pytest


@pytest.mark.me
def test_append():
    """
    This method appends (adds on) an element to the end of a list
    """
    fruit = ["apple", "orange", "banana"]
    fruit.append("pineapple")
    assert fruit == ['apple', 'orange', 'banana', 'pineapple']


def test_clear():
    """
    This method removes all items from a list
    """
    fruit = ["apple", "orange", "banana"]
    fruit.clear()
    assert fruit == []


def test_copy():
    """
    This method returns a copy of the specified list
    """
    fruit = ["apple", "orange", "banana"]
    assert fruit.copy() == ['apple', 'orange', 'banana']


def test_count():
    """
    This method counts the number of items in a list with the specified value
    """
    fruit = ["apple", "orange", "banana", "apple"]
    assert fruit.count("apple") == 2


def test_extend():
    """
    This method adds a list of items to the end of the specified list
    """
    fruit = ["apple", "orange", "banana"]
    people = ["Max", "James", "Bob"]
    fruit.extend(people)
    assert fruit == ['apple', 'orange', 'banana', 'Max', 'James', 'Bob']


def test_index():
    """
    This method returns the number where the specified value first occurs in a list
    """
    fruit = ["apple", "orange", "banana"]
    assert fruit.index("orange") == 1


def test_pop():
    """
    This methods removes (pops off) the item at the specified position in the list.
    The default value is -1, which removes the last item.
    """
    fruit = ["apple", "orange", "banana"]
    fruit.pop()
    assert fruit == ['apple', 'orange']


def test_remove():
    """
    This method removes an item from the list the first time it appears
    """
    fruit = ["apple", "orange", "banana", "apple"]
    fruit.remove("apple")
    assert fruit == ["orange", "banana", "apple"]


def test_reverse():
    """
    This method reverses the order of the items in the list
    """
    fruit = ["apple", "orange", "banana"]
    fruit.reverse()
    assert fruit == ['banana', 'orange', 'apple']


def test_sort():
    """
    This method will sort the items in the list by ascending order.
    It is possible to sort by descending using reverse=True
    """
    fruit = ["apple", "orange", "banana"]
    fruit.sort(reverse=True)
    assert fruit == ['orange', 'banana', 'apple']
