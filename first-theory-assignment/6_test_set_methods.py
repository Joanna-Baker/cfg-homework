import pytest


@pytest.mark.me
def test_add():
    """
    This method adds an element to the set, unless the element already exists
    """
    fruit = {"apple", "banana", "oranges"}
    fruit.add("pineapple")
    assert fruit == {'apple', 'banana', 'oranges', 'pineapple'}


def test_clear():
    """
    This method removes all the items from a set
    """
    fruit = {"apple", "banana", "oranges"}
    fruit.clear()
    assert fruit == set()


def test_copy():
    """
    This method copies the set
    """
    fruit = {"apple", "banana", "oranges"}
    fruit.copy()
    assert fruit == {'apple', 'banana', 'oranges'}


def test_difference():
    """
    This method compares two sets and returns a set with items that only appear in the first set
    """
    fruit_bowl_1 = {"apple", "banana", "oranges"}
    fruit_bowl_2 = {"apple", "pear", "oranges", "pineapple"}
    different_fruit = fruit_bowl_1.difference(fruit_bowl_2)
    assert different_fruit == {'banana'}


def test_intersection():
    """
    This method compares two sets and returns a set of items that appear in both sets
    """
    fruit_bowl_1 = {"apple", "banana", "oranges"}
    fruit_bowl_2 = {"apple", "pear", "oranges", "pineapple"}
    different_fruit = fruit_bowl_1.intersection(fruit_bowl_2)
    assert different_fruit == {'apple', 'oranges'}


def test_issubset():
    """
    This method compares two sets and if all items in the set appear in the specified set it returns True,
    otherwise it returns False
    """
    fruit_bowl_1 = {"apple", "banana", "oranges"}
    fruit_bowl_2 = {"apple", "pear", "oranges", "pineapple", "banana"}
    comparison = fruit_bowl_1.issubset(fruit_bowl_2)
    assert comparison == True


def test_issuperset():
    """
    This method is similar to issubset() in that it compares two sets, however, this method returns True
    if all the items in the specified set are in the original set, otherwise it returns False
    """
    fruit_bowl_1 = {"apple", "banana", "oranges"}
    fruit_bowl_2 = {"apple", "pear", "oranges", "pineapple", "banana"}
    comparison = fruit_bowl_1.issuperset(fruit_bowl_2)
    assert comparison == False


def test_pop():
    """
    This method removes a random item from the set
    """
    fruit_bowl = {"apple", "banana", "oranges"}
    fruit_bowl.pop()
    assert fruit_bowl


def test_remove():
    """
    This method removes a specified item from the set, if the item doesn't exist it will raise an error
    """
    fruit_bowl = {"apple", "banana", "oranges"}
    fruit_bowl.remove("banana")
    assert fruit_bowl == {'apple', 'oranges'}


def test_symmetric_difference():
    """
    This method compares two sets and returns the items that are not present in both
    """
    fruit_bowl_1 = {"apple", "banana", "oranges", "cherry"}
    fruit_bowl_2 = {"apple", "pear", "oranges", "pineapple"}
    difference = fruit_bowl_1.symmetric_difference(fruit_bowl_2)
    assert difference == {'banana', 'cherry', 'pear', 'pineapple'}


def test_union():
    """
    This method returns a set containing all items from the original set and all items from the specified set(s).
    If an item appears multiple times it will only appear once in the returned set
    """
    fruit_bowl_1 = {"apple", "banana", "oranges", "cherry"}
    fruit_bowl_2 = {"apple", "pear", "oranges", "pineapple"}
    fruit_bowl_3 = {"kiwi"}
    new_bowl = fruit_bowl_1.union(fruit_bowl_2, fruit_bowl_3)
    assert new_bowl == {'cherry', 'kiwi', 'banana', 'apple', 'pineapple', 'pear', 'oranges'}


def test_update():
    """
    This method adds items from one set to another set, if the item appears in both sets it only appears once
    in the new set
    """
    fruit_bowl_1 = {"apple", "banana", "oranges", "cherry"}
    fruit_bowl_2 = {"apple", "pear", "oranges", "pineapple"}
    fruit_bowl_1.update(fruit_bowl_2)
    assert fruit_bowl_1 == {'apple', 'banana', 'oranges', 'cherry', 'pear', 'pineapple'}