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


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


# order="latte"
# print (resources["water"])
# print (MENU[order]["ingredients"]["water"])
# def check_recipe(order):
#   if (resources["water"]<MENU[order]["ingredients"]["water"]):
#     return False
#   if (resources["coffee"]<MENU[order]["ingredients"]["coffee"]):
#     return False
#   if order!="espresso":
#       if (resources["milk"]<MENU[order]["ingredients"]["milk"]):
#         return False
#   else:
#     return True

# def calculate(q,d,n,p):
#   input_sum=0.01*int(q)+0.05*int(d)+0.1*int(n)+0.25*int(p)
#   return input_sum
# order=input ("What would you like? (espresso/latte/cappuccino): ")
# #check enough recipe
# result=check_recipe(order)
# if result==False:
#   print ("not enough ingredients")
# else:
#   print ("Please insert coins.")  
#   q=input ("how many quarters?: ")
#   d=input ("how many dimes?: ")
#   n=input ("how many nickles?: ")
#   p=input ("how many pennies?: ")
#   input_sum=calculate(q,d,n,p)
#   if (input_sum<MENU[order]["cost"]):
#     print ("Not enough input money")
#   else:
#     change=round(input_sum-MENU[order]["cost"],2)
#     print (f"Here is ${change} in change.")
#     print (f"Here is your {order} ☕️. Enjoy!")
#     if order!="espresso":
#       resources["milk"]=200-MENU[order]["ingredients"]["milk"]
#     resources = {
#     "water": 300-MENU[order]["ingredients"]["water"],
#     "coffee": 100-MENU[order]["ingredients"]["coffee"],
#     }