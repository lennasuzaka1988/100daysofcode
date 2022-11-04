from coffee_machine_data import resources
from coffee_machine_data import MENU

coffee_dispensed = True
total_revenue = 0


def if_enough_resources(coffee_type, ingredient):
    if resources["water"] - MENU[coffee_type]["ingredients"][ingredient] < 0:
        print(f"Sorry, there is not enough {ingredient}.")
    else:
        resources["coffee"] -= MENU[coffee_type]["ingredients"][ingredient]

    return resources


def remove_resources(coffee_type):
    if coffee_type == "espresso":
        if_enough_resources(coffee_type, "water")
        if_enough_resources(coffee_type, "coffee")
    else:
        if_enough_resources(coffee_type, "water")
        if_enough_resources(coffee_type, "milk")
        if_enough_resources(coffee_type, "coffee")
    return resources


def coins():
    penny = 0.01
    nickel = 0.05
    dime = 0.10
    quarter = 0.25
    return (penny * int(input("How many pennies will you use? "))) + \
           (nickel * int(input("How many nickles will you use? "))) + \
           (dime * int(input("How many dimes will you use? "))) + \
           (quarter * int(input("How many quarters will you use? ")))


def refund(coffee_type):
    coins_total = coins()
    if coins_total < MENU[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return coins_total
    else:
        us_dollars = "${:.2f}".format(coins_total - MENU[coffee_type]['cost'])
        print(f"Here is {us_dollars} in change.")
        print(f"Here is your {list(MENU.keys())[0]} ☕. Enjoy!")


while coffee_dispensed:
    coffee_query = input("What would you like? (espresso/latte/cappuccino) ")
    if coffee_query == "report":
        print(resources)
    elif coffee_query == "off":
        print("Machine is off.")
        break
    elif coffee_query == "espresso":
        remove_resources("espresso")
        refund("espresso")
        total_revenue += MENU["espresso"]["cost"]
    elif coffee_query == "latte":
        remove_resources("latte")
        refund("latte")
        total_revenue += MENU["latte"]["cost"]
    elif coffee_query == "cappuccino":
        remove_resources("cappuccino")
        refund("cappuccino")
        total_revenue += MENU["cappuccino"]["cost"]

