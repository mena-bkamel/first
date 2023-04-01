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
money = 0
stop = False
while not stop:

    take_an_order = input("What would you like? (espresso/latte/cappuccino): ")
    print("Insert coin.")

    quarters = float(input("How many quarters?"))
    dimes = float(input("How many dimes?"))
    nickles = float(input("How many nickles?"))
    pennies = float(input("how many pennies?"))


    def drink_price(drink):
        return MENU[drink]["cost"]


    drink_price0 = drink_price(take_an_order)


    def coins_paid(quarters, dimes, nickles, pennies):
        quarters * 0.25
        dimes * 0.10
        nickles * 0.5
        pennies * 0.1
        return quarters + dimes + nickles + pennies


    total_coins = coins_paid(quarters, dimes, nickles, pennies)
    money += total_coins

    def compare_money(drink_price, paid):
        if drink_price > paid:
            return print("Sorry that's not enough.Money refunded.")
        elif drink_price < paid:
            change = total_coins - drink_price
            return print(f"Here is {change} in change.\nHere is your latte ☕. Enjoy!")

    compare = compare_money(drink_price, total_coins)

    list =  ["water", "milk", "coffee", "cost"]
    a = resources[list[0]]
    b = resources[list[1]]
    c = resources[list[2]]

    if take_an_order == "off":
        stop = True
    elif take_an_order == "report":
        print(f"water: {a}")
        print(f"milk: {b} ")
        print(f"coffee: {c}")
        print(f"money: {money}")
    # TODO: 8. check the resource sufficient by making a function to compare real resource with the ingredients required.


    # TODO: 9. if the resources insufficient you should print Sorry there is no enough something (water ,milk, coffe).

    # TODO 10. If there are sufficient resources you have to insert prompt coins (TODO 2).

    # TODO 11. check if the user has insert enough money to purchase the drink, if he don't , (print TODO 4)
