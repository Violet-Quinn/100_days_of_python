MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":200,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }
}

profit=0
resources={
    "water":300,
    "milk":200,
    "coffee":100,
}
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item} ")
            return False
    return True

def process_coins():
    print("Please insert coins: ")
    total = int(input("how many quarters? "))*0.25
    total += int(input("how many dimes? ")) * 0.1
    total += int(input("how many nickels? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.01
    return total

def check_transaction(money_received,drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is ${change} in change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Insufficient Money, money refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")

machine_on=True

#TODO: 1. Prompt user by asking What would you like? (espresso/latte/cappuccino)
while machine_on:
    choice=input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if choice=="off":
        print("Coffee Machine shutting down")
        machine_on=False

# TODO: 3. Print report.
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")

#TODO: 4. Check resources sufficient?
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
#TODO: 5. Process coins.
            payment=process_coins()
#TODO: 6. Check transaction successful?
            if check_transaction(payment,drink["cost"]):
#TODO: 7. Make Coffee,  tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.
                make_coffee(choice,drink["ingredients"])