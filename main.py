from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

customer_to_serve=True
coffee_maker = CoffeeMaker()
menu=Menu()
money_machine=MoneyMachine()

while customer_to_serve:
# TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    user_input = input(f'What would you like? ({menu.get_items()}): ')
    if user_input == "off":
# TODO 2: Turn off the Coffee Machine by entering “ off ” to the prompt.
        customer_to_serve = False
    elif user_input == "report":
#  TODO 3: report.
        coffee_maker=CoffeeMaker()
        coffee_maker.report()
    elif user_input != ' ':
        menu_item=menu.find_drink(user_input)
        if menu_item!= None:
# TODO 4. Check resources sufficient?
            if coffee_maker.is_resource_sufficient(menu_item):
# TODO 5. Process coins
                money_machine = MoneyMachine()
                money_machine.report()
# TODO 6. Check transaction successful?

                if money_machine.make_payment(menu_item.cost):
                    coffee_maker.make_coffee(menu_item)
                    coffee_maker.report()
                    money_machine.report()


