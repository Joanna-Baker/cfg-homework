"""
Tasks:
1. Prompt user for a pin code

2. If the pin code is correct then proceed to the next step,
otherwise ask a user to type in a password again. You can give a user a maximum of 3 attempts and then exit a program.

3. Set account balance to 100.

4. Now we need to simulate cash withdrawal

5. Accept the withdrawal amount

6. Subtract the amount from the account balance and display the remaining balance
(NOTE! The balance cannot be negative!)

7. However, when a user asks to ‘withdraw’ more money than they have on their account, then you need to raise an
error and exit the program.
"""


def check_pin_code():
    count = 0
    while count < 3:
        try:
            count += 1
            validate_pin(int(input("Please enter your 4 digit pin number: ")))
            return
        except ValueError:
            print("Invalid input. You have entered something that isn't a number!")
        except:
            print("You have entered an incorrect pin.")
            if count < 3:
                print("Please try again.")
    raise Exception("Sorry, you have attempted to enter your pin incorrectly too many times.")


def validate_pin(pin):
    if pin != 1234:
        raise Exception


def withdrawal(account_balance):
    amount = None
    number_of_tries = 0
    while amount is None and number_of_tries <= 3:
        try:
            amount = validate_withdrawal_amount(int(input("Please enter your withdrawal amount: ")), account_balance)
            return amount
        except ValueError:
            number_of_tries += 1
            print("Invalid input. Please enter a number.")
        except:
            print("Sorry you do not have the required funds.")
            raise Exception


def validate_withdrawal_amount(withdrawal_amount, account_balance):
    if withdrawal_amount > account_balance:
        raise Exception
    return withdrawal_amount


def atm_machine():
    try:
        check_pin_code()
        account_balance = int(100)
        print(f"Account balance is £{account_balance}")
        amount = withdrawal(account_balance)
        account_balance -= amount
        print(f"Your account balance is now £{account_balance}")
    except:
        print("Goodbye")


atm_machine()
