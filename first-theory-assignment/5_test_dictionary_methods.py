import pytest


@pytest.mark.me
def test_clear():
    """
    This method removes all the items from a dictionary
    """
    fruit_bowl = {"apple": 5, "banana": 4, "oranges": 2}
    fruit_bowl.clear()
    assert fruit_bowl == {}


def test_copy():
    """
    This method returns a copy of the specified dictionary
    """
    fruit_bowl = {"apple": 5, "banana": 4, "oranges": 2}
    fruit_bowl.copy()
    assert fruit_bowl == {'apple': 5, 'banana': 4, 'oranges': 2}


def test_fromkeys():
    """
    This method creates a dictionary from the specified keys and value. The default value is None.
    """
    fruit = ("apple", "pear", "orange")
    amount = 5
    fruit_bowl = dict.fromkeys(fruit, amount)
    assert fruit_bowl == {'apple': 5, 'pear': 5, 'orange': 5}


def test_get():
    """
    This method returns the value of the item from the specified key
    """
    fruit_bowl = {"apple": 5, "banana": 4, "oranges": 2}
    assert fruit_bowl.get("apple") == 5


def test_items():
    """
    This method creates a view object that contains the key-value pairs as tuples in a list.
    If any changes are made to the dictionary, they are reflected in the view object.
    """
    fruit_bowl = {"apple": 5, "banana": 4, "oranges": 2}
    fruit_bowl_items = fruit_bowl.items()
    assert list(fruit_bowl_items) == [('apple', 5), ('banana', 4), ('oranges', 2)]


def test_keys():
    """
    Similar to the items() function, this returns a view object, however this only contains
    the keys of the dictionary as a list. If any changes are made to the dictionary, they are
    reflected in the view object.
    """
    fruit_bowl = {"apple": 5, "banana": 4, "oranges": 2}
    bowl_keys = fruit_bowl.keys()
    assert list(bowl_keys) == ['apple', 'banana', 'oranges']


def test_pop():
    """
    This method removes the specified item from the dictionary
    """
    fruit_bowl = {"apple": 5, "banana": 4, "oranges": 2}
    fruit_bowl.pop("banana")
    assert fruit_bowl == {'apple': 5, 'oranges': 2}


def test_popitem():
    """
    This method removes the item that was last added to the dictionary
    """
    fruit_bowl = {"apple": 5, "banana": 4, "oranges": 2}
    fruit_bowl.popitem()
    assert fruit_bowl == {"apple": 5, "banana": 4}


def test_setdefault():
    """
    This method returns the value of the specified key and if it doesn't exist it inserts it
    """
    fruit_bowl = {"apple": 5, "banana": 4, "oranges": 2}
    fruit_bowl.setdefault("pineapple", 1)
    assert fruit_bowl == {'apple': 5, 'banana': 4, 'oranges': 2, 'pineapple': 1}


def test_update():
    """
    This method inserts the specified items into the dictionary
    Items can be in a dictionary or an iterable object with key: value pairs
    """
    fruit_bowl = {"apple": 5, "banana": 4, "oranges": 2}
    fruit_bowl.update({"pineapple": 1})
    assert fruit_bowl == {'apple': 5, 'banana': 4, 'oranges': 2, 'pineapple': 1}


def test_values():
    """
    Similar to items() and keys(), this method returns a view object,
    however, it contains the values of the dictionary as a list.
    """
    fruit_bowl = {"apple": 5, "banana": 4, "oranges": 2}
    bowl_values = fruit_bowl.values()
    assert list(bowl_values) == [5, 4, 2]
