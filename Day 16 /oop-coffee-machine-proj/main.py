from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


Machine_ON = True
while Machine_ON:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: \n")

    if choice == "off":
        Machine_ON = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)

        if drink is None:
            continue

        if coffee_maker.is_resource_sufficient(drink) == True:
            if money_machine.make_payment(drink.cost) == True:
                coffee_maker.make_coffee(drink)

    
