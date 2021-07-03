from unittest.mock import patch
import pytest
from week4.exception_handling_atm_machine import check_pin_code
from week4.exception_handling_atm_machine import validate_pin
from week4.exception_handling_atm_machine import validate_withdrawal_amount
from week4.exception_handling_atm_machine import withdrawal

"""
Write at least 5 unit tests to test the functions used in the atm machine program

If input is not an integer, raise an error.
If input is not the correct number.
If pin is entered incorrectly more than 3 times.
If withdrawal input is not an integer.
If withdrawal is more than available balance.
"""

@patch('builtins.input', lambda *args: 'asdf')
def test_check_pin_code_non_integer_input():
    with pytest.raises(Exception) as exception_info:
        check_pin_code()
    assert "too many times" in str(exception_info.value)


def test_validate_pin_raises_exception():
    with pytest.raises(Exception):
        pin = 3456
        validate_pin(pin)


def test_validate_pin_passes():
    try:
        pin = 1234
        validate_pin(pin)
    except:
        pytest.fail("The pin number is incorrect")


@patch('builtins.input', lambda *args: '12345')
def test_check_pin_code_number_of_entries():
    with pytest.raises(Exception) as exception_info:
        check_pin_code()
    assert "too many times" in str(exception_info.value)


@patch('builtins.input', lambda *args: 'asdf')
def test_withdrawal_non_integer_input(capsys):
    withdrawal(40)
    captured = capsys.readouterr()
    assert "Please enter a number." in str(captured.out)


def test_validate_withdrawal_amount_raises_exception():
    with pytest.raises(Exception):
        withdrawal_amount = 105
        account_balance = 100
        validate_withdrawal_amount(withdrawal_amount, account_balance)


def test_validate_withdrawal_amount_passes():
    try:
        withdrawal_amount = 50
        account_balance = 100
        validate_withdrawal_amount(withdrawal_amount, account_balance)
    except:
        pytest.fail("The withdrawal amount is more than account balance")






