"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self):
        self.items_list = []
        self.total_price = float(0)

    def add_item(self, item_name, item_price):
        self.items_list.append({'name': item_name, 'price': item_price})
        self.total_price += item_price

    def remove_item(self, item_name):
        for item in reversed(self.items_list):
            if item_name == item['name']:
                self.items_list.remove(item)
                self.total_price -= item['price']
                print(f"The {item_name} has been removed from your shopping.")
                break

    def apply_discount(self, discount):
        discount_price = self.total_price - ((self.total_price * discount) / 100)
        print(f"Your new total after discount is: £{discount_price}.")

    def get_total(self):
        print(f"Your total is: £{self.total_price}")

    def show_items(self):
        print(f"You have purchased the following items: {', '.join([item['name'] for item in self.items_list])}")

    def reset_register(self):
        print("The register has been cleared.")
        self.items_list.clear()
        self.total_price = float(0)


# # # How code works # # #
cash_register = CashRegister()
cash_register.add_item('apple', 0.50)
cash_register.add_item('bread', 1.50)
cash_register.add_item('chocolate', 2)
cash_register.show_items()
cash_register.get_total()
cash_register.remove_item('apple')
cash_register.show_items()
cash_register.get_total()
cash_register.apply_discount(10)
cash_register.reset_register()
cash_register.show_items()
cash_register.get_total()

