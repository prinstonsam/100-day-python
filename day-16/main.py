from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()

    menu = Menu()

    is_on = True

    while is_on:
        options = menu.get_items()
        choice = input(options)

        if choice == "off":
            is_on = False
        elif coffee_maker == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):
                money_machine.make_payment(drink.cost)


if __name__ == "__main__":
    main()
