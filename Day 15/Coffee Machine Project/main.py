MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 3.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 5.0,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 4.0,
    }
}

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 200,
}

def get_ingredients(selection):
    if selection == '0':
        return MENU["espresso"]["ingredients"]
    elif selection == '1':
        return MENU["latte"]["ingredients"]
    elif selection == '2':
        return MENU["cappuccino"]["ingredients"]
    else:
        return None

def get_price(selection):
    if selection == '0':
        return MENU["espresso"]["cost"]
    elif selection == '1':
        return MENU["latte"]["cost"]
    else:
        return MENU["cappuccino"]["cost"]

resources_enough = True
profit = 0
is_on = True
while is_on:
    coins_inserted = 0
    user_choice = input("Select from Espresso (0), Latte (1) or Cappuccino (2). ")
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        print(f"Water: {resources["water"]} - Milk: {resources["milk"]} - Coffee: {resources["coffee"]} ")
        print(f"Profit: {'£{:,.2f}'.format(profit)}")
    else:
        choice_ingredients = get_ingredients(user_choice)
        if user_choice != '0':
            if choice_ingredients["milk"] > resources["milk"]:
                print(f"There is not enough milk to make your drink.")
                resources_enough = False
            else:
                resources["milk"] -= choice_ingredients["milk"]
        if choice_ingredients["water"] > resources["water"]:
            print(f"There is not enough water to make your drink.")
            resources_enough = False
        else:
            resources["water"] -= choice_ingredients["water"]
            if choice_ingredients["coffee"] > resources["coffee"]:
                print(f"There is not enough coffee to make your drink.")
                resources_enough = False
            else:
                resources["coffee"] -= choice_ingredients["coffee"]

        drink_cost = get_price(user_choice)
        attempts = 0
        if resources_enough:
            while coins_inserted < drink_cost and attempts < 5:
                attempts += 1
                remaining = drink_cost - coins_inserted
                try:
                    coins = float(input(f"Please enter {'£{:,.2f}'.format(remaining)} in coins. "))
                except ValueError:
                    print("Please enter only valid coins (numerical digits) ")
                    coins = float(input(f"Please enter {'£{:,.2f}'.format(remaining)} in coins. "))
                coins_inserted += coins
            if coins_inserted > drink_cost:
                remaining = coins_inserted - drink_cost
                print(f"Your change is {'£{:,.2f}'.format(remaining)}. Please collect your drink and change. Thank you.")
                profit += drink_cost
            elif coins_inserted == drink_cost:
                print(f"Please take your drink ☕. Thank you.")
                profit += drink_cost
            else:
                print(f"You did not enter enough coins. Your money will now be refunded.")