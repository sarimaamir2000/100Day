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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True

def resource_sufficient(drink):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in drink['ingredients']:
        if drink['ingredients'][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total



while is_on:
    """Ask user for input and return it"""
    choice = input("What would you like? (espresso/latte/cappuccino/report): ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resource_sufficient(drink):
            payment = process_coins()
            if payment >= drink['cost']:
                profit += drink['cost']
                for item in drink['ingredients']:
                    resources[item] -= drink['ingredients'][item]
                print(f"Here is your {choice} ☕ Enjoy!")
                print(f"Here is ${round(payment - drink['cost'], 2)} in change.")
            else:
                print("Sorry that's not enough money. Money refunded.")


