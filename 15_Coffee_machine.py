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

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”a. Check the user’s input to decide what to do next.b. The prompt should show every time action has completed, e.g. once the drink isdispensed. The prompt should show again to serve the next customer.
# TODO: 2. Create method so that if user types "off" it will close the program
# TODO: 3. Print Report. When the user types "report", a report should be generated showing the current resource values. eg water:100ml, milk 50ml etc.
# TODO: 4. Check for sufficient resources. When user makes a drink, check what the current resources are. If there isn't the required amount, let the user know and don't run the order.
# TODO: 5. Process coins. Calculate the amount of coins. If enough return any change, if not, "refund money" and say not enough coins
# TODO: 6. Run Order if transaction succesful. Check if enough resources. Add profits/resources to report. Change should be rounded to 2 decimals.
# TODO: 7. If enough resources, deduct from amount and print enjoy your drink or whatever.

coffee_on = True
profit = 0
resources["money"] = profit


def print_report():
    print(f'Water: {resources["water"]} ml')
    print(f'Milk: {resources["milk"]} ml')
    print(f'Coffee: {resources["coffee"]} ml')
    print(f'Money: ${resources["money"]}')


def check_resources(order_ingredients):
    for item in order_ingredients:
        pass


while coffee_on:
    order = input("What drink would you like (espresso/latte/cappuccino)? : ").lower()
    if order == "off":
        quit()
    if order == "report":
        print_report()
    else:
        drink = MENU[order]
        print(drink)
