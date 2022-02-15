from cmath import rect
from data import MENU, resources, profit, logo
from os import system
def clear():
    command = 'cls'
    system(command)

def report():

    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = profit["money"] 
    return print(f"Water: {water}ml\nMilk: {milk}g\nCoffee: {coffee}g\nMoney: ${money:.2f}")
 
def check_resources(answer):
     
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    ingredients = MENU[answer]["ingredients"]
    
    for resource in resources:
        for ingredient in ingredients:
            if ingredient == resource and ingredients[ingredient] > resources[resource]:
                print(f"Sorry there is not enough {resource}")
                return False

    # if answer == "espresso":
    #     if MENU["espresso"]["ingredients"]["water"] > water:
    #         print("Sorry there is not enough water")
    #         return False
    #     if MENU["espresso"]["ingredients"]["coffee"] > coffee:
    #         print("Sorry there is not enough coffee")
    #         return False    
    # if answer == "latte":
    #     if MENU["latte"]["ingredients"]["water"] > water:
    #         print("Sorry there is not enough water")
    #         return False
    #     if MENU["latte"]["ingredients"]["coffee"] > coffee:
    #         print("Sorry there is not enough coffee")
    #         return False               
    #     if MENU["latte"]["ingredients"]["milk"] > milk:
    #         print("Sorry there is not enough milk")
    #         return False  

    # if answer == "cappuccino":
    #     if MENU["cappuccino"]["ingredients"]["water"] > water:
    #         print("Sorry there is not enough water")
    #         return False
    #     if MENU["cappuccino"]["ingredients"]["coffee"] > coffee:
    #         print("Sorry there is not enough coffee")
    #         return False               
    #     if MENU["cappuccino"]["ingredients"]["milk"] > milk:
    #         print("Sorry there is not enough milk")
    #         return False 
        
    return True

def insert_coin():
   print("Please Insert Coin")
   quarters = int(input("How many quarters?  "))
   dimes = int(input("How many dimes?  "))
   nickles = int(input("How many nickles?  "))
   pennies = int(input("How many pennies?  "))
   total_amount = round(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01, 2)
   return total_amount 


def check_coins(total_amount, answer):
    change = total_amount - MENU[answer]["cost"]
    if total_amount < MENU[answer]["cost"]:
        print(f"Sorry that's not enough money for {answer}. ${total_amount:.2f} refunded.")
        return False
    elif total_amount > MENU[answer]["cost"]:
        print(f"Here is ${change:.2f} dollars in change.")
        return True
    else:
        return True
    
def make_coffee(answer):
    resources["water"] -= MENU[answer]["ingredients"]["water"]
    resources["milk"] -= MENU[answer]["ingredients"]["milk"]
    resources["coffee"] -= MENU[answer]["ingredients"]["coffee"]
    profit["money"] += MENU[answer]["cost"]
    print(f"Here is your {answer}. Enjoy!")
    
clear()
print(logo)
is_need_reinforce = 0 

while True:
    print(f"Espresso: ${1.50:.2f}  Latte: ${2.50:.2f}  Cappuccino: ${3.00:.2f}")
    answer = input("What would you like? (espresso/latte/cappuccino):  ").lower()    
    if answer == "off":
        print("!!!Maintenace Mode!!!")
        break
    elif answer == "report":
        report()
    elif answer in ("espresso", "latte", "cappuccino"):

        is_enough_resources = check_resources(answer)
        if not is_enough_resources:
            is_need_reinforce += 1
            if is_need_reinforce == 3:
                print("The Machine Need Reinforcement. Please Come Back Later!!!")
                break
            continue
        total_amount = insert_coin()
        is_enough_coin = check_coins(total_amount, answer)
        if not is_enough_coin:
            continue
        make_coffee(answer)
    else:
        print("Wrong Choice!!! Try Again!!!")
        