MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

uom = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
}
coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01,
}
# TODO 3  report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

def print_report():
    for key, value in resources.items():
        print(key.capitalize()  + " " + str(value) + " " + uom[key])
    print(profit)
# TODO 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “ Sorry there is not enough water. ”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
def resources_sufficient(drink):
    enough=True

    for key,value in MENU.items():

        if key == drink:

            if drink != 'espresso':
               if resources["milk"] - MENU[drink]["ingredients"]["milk"] <0:
                print('Sorry there is not enough milk.')
                enough=False

            if (resources["water"] - MENU[drink]["ingredients"]["water"] < 0):
                print('Sorry there is not enough water.')
                enough=False

            if (resources["coffee"] - MENU[drink]["ingredients"]["coffee"] < 0):
                print("Sorry there is not enough water.")
                enough=False

    return enough



#TODO 5. Process coins
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52


def count_coins():

    print("Please insert coins")
    quarters= float(input("How many quarters did you insert?"))
    dimes = float(input("How many dimes did you insert?"))
    nickels= float(input("How many nickels did you insert?"))
    pennies = float(input("How many penniess did you insert?"))

    total =(quarters * 0.25) +(dimes * 0.1) + (nickels * .05 ) + (pennies * .01)
    return total


# TODO 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “ Sorry that's not enough money. Money refunded. ”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

def check_transaction(drink,total):
    transaction_ok =True

    cost= float(MENU[drink]["cost"])
    if total >=  cost:
        if total == cost:
            print("no change required")
        elif total >cost:
            print(f'Here is ${(round(total-cost,2))} in change')
        else:
            print(' Sorry that"s not enough money. Money refunded. ')
            transaction_ok = False
    return transaction_ok

#TODO 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.


def make_coffee(drink):
    print("before making coffee")
    print_report()
    if resources_sufficient(drink):
        print(f'Here is your {drink}.Enjoy!')
    if drink != 'espresso':
        resources["milk"] = resources["milk"] - MENU[drink]["ingredients"]["milk"]

    resources["water"]=resources["water"] - MENU[drink]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
    global profit
    profit += float(MENU[drink]["cost"])
    print_report()


# TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”

# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.


    customer_to_serve=True
    profit = 0

    while customer_to_serve:


        user_input= input('What would you like? (espresso/latte/cappuccino): ')


# TODO 2: Turn off the Coffee Machine by entering “ off ” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
    if user_input=="off":
        customer_to_serve=False

#  TODO 3: report.
# a. When the user enters “report” to the prompt, a report should be generated that shows

    elif user_input == "report":
        print_report()
    elif  user_input != "":
        total = count_coins()
        if check_transaction(user_input,total):
           make_coffee(user_input)


