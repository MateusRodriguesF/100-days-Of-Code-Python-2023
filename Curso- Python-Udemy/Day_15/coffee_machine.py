from coffe_data import MENU, resources

coffee_menu = MENU
coffee_resources = resources
is_on = True
profit = 0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry not enough {item}.")
            return False
        return True
    
def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_sucessful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, theres not enough money. money refunded.")
        return False
    
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ Enjoy!")

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {coffee_resources['water']} ml")
        print(f"Milk: {coffee_resources['milk']} ml")
        print(f"Coffe: {coffee_resources['coffee']} ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice] # Bebida é o valor escolhido no input >  Menu[choice = dicionario]
        if is_resource_sufficient(drink["ingredients"]):# ex: cappuccino["ingedients"]]
            payment = process_coins()
            if is_transaction_sucessful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
