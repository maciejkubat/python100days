from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def run_machine():
    is_on = True
    menu = Menu()
    coffe_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    while is_on:
        available_items = menu.get_items()
        user_input = input(f"What would you like? ({available_items}) ").lower()
        if user_input == "off":
            is_on = False
        elif user_input == "report":
            coffe_maker.report()
            money_machine.report()
        elif menu.find_drink(user_input) is not None:
            ordered_item = menu.find_drink(user_input)
            if coffe_maker.is_resource_sufficient(ordered_item):
                payment_processed = money_machine.make_payment(ordered_item.cost)
                if payment_processed:
                    print("Making coffe")
                    coffe_maker.make_coffee(ordered_item)


run_machine()