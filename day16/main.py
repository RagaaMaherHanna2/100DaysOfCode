from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def make_order():
    menu = Menu()
    order = input(f"What would you like? (espresso/latte/cappuccino/):")
    item = menu.find_drink(order)
    if item:
        coffee_order = CoffeeMaker()
        order_pay = MoneyMachine()
        if coffee_order.is_resource_sufficient(item):
            if order_pay.make_payment(3):
                coffee_order.make_coffee(item)


def turn_off():
    return True


def make_report():
    return True


if __name__ == '__main__':
    maker = CoffeeMaker()
    choices = {'1': 'Make Order',
               '2': 'Report',
               '3': 'Turn Off'}

    for k, v in choices.items():
        print(k, ": ", v)
    choice = input(f"Choose your service \n ")

    if choice == '1':
        make_order()
    elif choice == '2':
        make_report()
    elif choice == '3':
        turn_off()
    else:
        print('Sorry entered invalid choice')







