"""
Docstring for Day 15.the_coffee_machine_project
In this virtual coffee machine you can get espresso,latte or cappuccino. Pay in coins and with each order the resources are recalculated.
After the resources are gone, you can't order anymore.
By prompting "report" you can get an overview of the available resources.
By prompting "off", the coffee machine will be turned off.
"""

from data import resources
from data import menu_item
from data import COIN_VALUES


def show_report(resources):
    for key in resources:
        print(f"{key} : {resources[key]}")



def resource_check(resources,menu_item,user_choice):
    for item in menu_item:
        if item["name"] == user_choice:
            for key in resources:
                if resources[key] < item[key]:
                    print(f"Not enough {key}")
                    return False
            return True
        

def calculate_coins(coin_values,user_choice,menu_item,quarter,dime,nickel,pennies):
    payment = (quarter * float(coin_values["quarters"])) + (dime * float(coin_values["dimes"])) + (nickel * float(coin_values["nickles"])) + (pennies * float(coin_values["pennies"]))

    for item in menu_item:
        if item["name"] == user_choice:
            return payment-float(item["cost"])
        
def resource_lowering(resources,menu_item,user_choice):
    for item in menu_item:
        if item["name"] == user_choice:
            for key in resources:
                resources[key] -= item[key]

def get_cost(menu_item, user_choice):
    for item in menu_item:
        if item["name"] == user_choice:
            return item["cost"]

    
Machine_ON = True

while Machine_ON:

    user_choice = input("What would you like?  (espresso,latte or cappuccino) \n")

    coffee_choices = ["espresso","latte","cappuccino"]
    

    if user_choice in coffee_choices:
        has_resources = resource_check(resources,menu_item,user_choice)
        if has_resources == True:
            cost = get_cost(menu_item, user_choice)
            print(f"Please insert coins: {cost}$")
            quarter = float(input("Quarters: "))
            dime = float(input("Dimes: "))
            nickel = float(input("Nickles: "))
            pennies = float(input("Pennies: "))
            calc_payment = calculate_coins(COIN_VALUES,user_choice,menu_item,quarter,dime,nickel,pennies)
            if calc_payment < 0:
                print(f"Sorry,that is not enough money: {calc_payment}")
            else:
                print(f"Thank you for your purchase, here is your change: {round(calc_payment,2)}")
                print(f"Your {user_choice} is ready for drinking.")
                resource_lowering(resources,menu_item,user_choice)

        else:
            print("Sorry, there are not enough resources")
    elif user_choice == "report":
        show_report(resources) 

    elif user_choice =="off":
        Machine_ON = False




                

        
# TODO-1 - Machine_ON = True , and when input "off" - Machine_ON = False
# TODO-2 - If ON, Ask what the user wants?
# TODO-1 - Print report 
# TODO-2 - Check if there are sufficient resources
# TODO-3 - Process coins
# TODO-4 - Check if the transaction is successful  
# TODO-5 - Make Coffee and recalculat the resources 