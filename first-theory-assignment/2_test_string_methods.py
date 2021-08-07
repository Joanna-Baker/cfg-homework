import pytest


@pytest.mark.me
def test_capitalize():
    """
    Turns text into sentence case - capital letter for the first word and the rest lowercase
    """
    assert "HELLO".capitalize() == 'Hello'


def test_casefold():
    """
    Turns all characters lowercase
    """
    assert "HELLO".casefold() == 'hello'


def test_center():
    """
    Centres the string in the middle of the specified number of characters
    """
    assert "hello".center(20) == '       hello        '


def test_count():
    """
    Counts specified elements
    """
    text = "apples are the best fruit in the world, everyone should eat apples...apples"
    assert text.count("apple") == 3


def test_endswith():
    """
    Gives True or False if a string does or does not end with a specified value
    """
    text = "Hello there"
    assert text.endswith("ere") == True


def test_find():
    """
    Finds the character number for the start of the specified value
    """
    text = "Hello there"
    assert text.find("there") == 6


def test_format():
    """
    Insert the specified value into the curly brackets {}. This can be done using .format or fstrings
    """
    apples = 5
    cost_per_apple = 0.50
    total_cost = apples * cost_per_apple
    assert (f"{apples} apples cost £{total_cost}") == ("5 apples cost £2.5")


def test_index():
    """
    Returns the position of a word in a string or a value in a list
    """
    fruit = ["apple", "apple", "cherry"]
    assert fruit.index("cherry") == 2


def test_isalnum():
    """
    Returns True or False if all characters are or are not alphanumeric e.g. a-z, 0-9
    """
    text = "Boo!"
    assert text.isalnum() == False


def test_isalpha():
    """
    Returns True or False if all characters are or are not alphabetical e.g. a-z
    """
    text = "5"
    assert text.isalpha() == False


def test_isdigit():
    """
    Returns True or False if all characters are or are not digits e.g. 0-9
    """
    text = "5050"
    assert text.isdigit() == True


def test_islower():
    """
    Returns True or False if all characters are or are not lowercase
    """
    text = "Hello"
    assert text.islower() == False


def test_isnumeric():
    """
    Returns True or False if all chacters are or are not numeric. Decimals return False due to the decimal point
    """
    text = "1"
    assert text.isnumeric() == True


def test_isspace():
    """
    Returns True or False if all characters in a string are whitespace
    """
    text = " "
    assert text.isspace() == True


def test_istitle():
    """
    Returns True or False on whether all words start with a capital and the rest are lowercase.
    Symbols & numbers are ignored
    """
    text = "Hello There"
    assert text.istitle() == True


def test_isupper():
    """
    Returns True or False if all characters are or are not uppercase
    """
    text = "HELLO"
    assert text.isupper() == True


def test_join():
    """
    Joins all the values separated by a comma. e.g. in a list, tuple or string. A joining character can be inserted.
    """
    text = "a", "b", "c"
    assert "#".join(text) == 'a#b#c'


def test_lower():
    """
    Returns a string where all the characters are lowercase
    """
    text = "Hello, WHAT IS YOUR NAME?"
    assert text.lower() == 'hello, what is your name?'


def test_lstrip():
    """
    Removes any leading characters. Space is the default, but characters can be specified
    """
    text = "£$%^&*()Hello there"
    assert text.lstrip("£$%^&*()") == 'Hello there'


def test_replace():
    """
    This method replaces a specified phrase with another specified phrase
    """
    text = "An orange a day keeps the doctor away"
    assert text.replace("orange", "apple") == 'An apple a day keeps the doctor away'


def test_rsplit():
    """
    This method splits a string starting from the right side. It uses the specified separator to separate the string.
    """
    text = "apple, pineapple, cherry"
    assert text.rsplit(", ") == ['apple', 'pineapple', 'cherry']


def test_rstrip():
    """
    This method removes characters at the end of a string. Space is the default but characters can be specified
    """
    text = "Hello there)(*&^%$£"
    assert text.rstrip(")(*&^%$£") == 'Hello there'


def test_split():
    """
    This method splits a string into a list. The separator can be specified, the default is whitespace
    """
    text = "Hello there, welcome to your first day"
    assert text.split() == ['Hello', 'there,', 'welcome', 'to', 'your', 'first', 'day']


def test_splitlines():
    """
    This method splits a string into a list at line breaks
    """
    text = "Hello there\nWelcome to your first day"
    assert text.splitlines() == ['Hello there', 'Welcome to your first day']


def test_startswith():
    """
    This method returns True or False if the string does or does not start with the specified value
    """
    text = "Hello there"
    assert text.startswith("Hello") == True


def test_strip():
    """This method removes leading and trailing characters from a string.
    Space is the default but characters can be specified
    """
    text = "12345Hello there12345"
    assert text.strip("12345") == 'Hello there'


def test_swapcase():
    """
    This method swaps upper case characters to lower case and lower case characters to upper case
    """
    text = "hELLO tHERE"
    assert text.swapcase() == 'Hello There'


def test_title():
    """
    This method returns a string where the first character in every word is upper case
    """
    text = "this is the title of a book"
    assert text.title() == 'This Is The Title Of A Book'


def test_upper():
    """
    This method returns a string where all characters are upper case
    """
    text = "hello there"
    assert text.upper() == 'HELLO THERE'
