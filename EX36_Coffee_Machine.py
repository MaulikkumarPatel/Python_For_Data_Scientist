from Coffee_Machine_data import MENU, resources

profit = 0


def check_resources(order_ingredients):
    """Return true when order can be made, False if ingredients insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coin():
    """ This function gives the total of entered coins. """
    print("Please insert the coins.")
    total = int(input("How many quarters? : ")) * 0.25
    total += int(input("How many dimes? : ")) * 0.10
    total += int(input("How many nickles? : ")) * 0.05
    total += int(input("How many pennies? : ")) * 0.01

    return total


def is_transaction_successful(money_rec, drink_cost):
    """Return true when the payment is accepted, or False if money is insufficient."""
    if payment >= drink_cost:
        change = abs(round(money_rec - drink_cost, 2))
        print(f"Here is £{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Payment refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your drink {drink_name}. Enjoy!!!")


while True:
    choice = input(f"What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}mg")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coin()
            is_transaction_successful(payment, drink["cost"])
            make_coffee(choice, drink["ingredients"])