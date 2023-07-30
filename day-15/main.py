menu = {
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
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

cappuccino = "cappuccino"
expresson = "espresso"
latte = "latte"

coffees = ["cappuccino", "espresso", "latte"]


def report(val_remaining_resources):
    print(f"remaining_resources['water'] {val_remaining_resources['water']}")
    print(f"remaining_resources['milk'] {val_remaining_resources['milk']}")
    print(f"remaining_resources['coffee'] {val_remaining_resources['coffee']}")


def decrease_resources(val_remaining_resources, spent_ingredients, cost):
    result = {}
    for inner_key in spent_ingredients:
        result[inner_key] = val_remaining_resources[inner_key] - spent_ingredients[inner_key]
    return result


def check_available_resources(val_remaining_resources):
    if val_remaining_resources["water"] < 0 or val_remaining_resources["milk"] < 0 or val_remaining_resources["coffee"] < 0:
        return False
    return True


report(resources)
continue_choice = "y"
remaining_resources= resources

while continue_choice == "y":

    choice = input("what would you like? expresso/latte/cappuccino")
    if choice == "report":
        report(remaining_resources)
    else:
        ingredients = {}
        cost = 0
        main_key = choice
        for key in menu[main_key]["ingredients"]:
            ingredients[key] = menu[main_key]["ingredients"][key]
            cost = menu[main_key]["cost"]

        remaining_resources = decrease_resources(remaining_resources, ingredients, cost)

        if not check_available_resources(resources):
            print("You dont have available resources")
            choice = "n"

    continue_choice = input("Do you want continue?")
