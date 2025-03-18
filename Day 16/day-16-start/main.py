from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinks_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

is_on = True
while is_on:
    user_choice = input(f"Select from {drinks_menu.get_items()}").lower()
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        print(my_coffee_maker.report())
        print(my_money_machine.report())
    else:
        drink_choice = drinks_menu.find_drink(user_choice)
        if drink_choice is not None:
            if my_coffee_maker.is_resource_sufficient(drink_choice):
                print(f"Please enter {my_money_machine.CURRENCY}{drink_choice.cost:.2f} now")
                if my_money_machine.make_payment(drink_choice.cost):
                    my_coffee_maker.make_coffee(drink_choice)