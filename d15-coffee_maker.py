import os
import logging
logger = logging.getLogger("coffee_machine")
logging.basicConfig(
    level="DEBUG"
)

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



def clear_screen():
  # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

# allows the user to use a shortcut key.
# TODO have the handler build a list from the database
def input_handler(choice):
    if choice[0] == "e":
        return "espresso"
    elif choice[0] == "l":
        return "latte"
    elif choice[0] == "c":
        return "cappuccino"
    elif choice[0] == "r":
        return "report"   
    elif choice[0] == "o":
        return "off"
    else:
        print("invalid choice. Please try again\n")
        return "invalid"
      



def check_resources(beverage):
    beverage = MENU[beverage]
    logger.debug(beverage)
    logger.debug(beverage["ingredients"])

    for ingredient in beverage["ingredients"]:
        logger.debug(ingredient)
        if beverage["ingredients"][ingredient] > resources[ingredient]:
            return [False, ingredient]
    
    return [True]


#add up money.
# TODO input handling so pressing enter doesn't kill game.
def insert_coins():
    print("Please insert coins")
    quarters = int(input ("how many quarters: ")) * .25
    dimes = int(input ("how many dimes: ")) * .10
    nickels = int(input ("how many nickles: ")) *.05
    pennies = int(input ("how many pennies: ")) * .01

    money = round(quarters + dimes + nickels + pennies, 2)

    return money


def coffee_machine():
    global machine_on
    global coin_box
    # prompt user to pick a drink from the menu
    user_choice = input("What would you like? (e)spresso/(l)atte/(c)appuccino: ")
    
    choice = input_handler(user_choice)

    #invalid input returned, do nothing
    if choice == "invalid":
        pass

    # print report that shows resources remaining
    elif choice == "report":
        print(f"""
        Water: {resources["water"]}
        Milk: {resources["milk"]}
        Coffee: {resources["coffee"]}
        Money: {coin_box}
        """)
    
    # turn off coffee machine with off command
    elif choice == "off":
        print("Turning coffee machine off")
        machine_on = False
      
    # do we have enough ingredients to make the drink?
    else:
        enough_ingredients = check_resources(choice)
        logger.debug(enough_ingredients)
        
        if not enough_ingredients[0]:
            print(f"sorry there is not enough {enough_ingredients[1]}.\n")
        
        else:
            # ask the user to insert some coins and return the sum
            money = insert_coins()

            # refund the user's money if they're short.
            if money < MENU[choice]["cost"]:
                print("Sorry, that's not enough money. Money Refunded")
            
            # update state and make the coffee
            else:
                coin_box += money
                change = round(money - MENU[choice]["cost"], 2)

                if change > 0:
                    print(f"Here is ${change} in change.")

                # loop over the ingredients and subtract from resources
                for ingredient in MENU[choice]["ingredients"]:
                    resources[ingredient] -= MENU[choice]["ingredients"][ingredient]
                
                # make the coffee!!!!! 
                print(f"Here is your {choice}. Enjoy!\n")


                
                
                

                

                



    
    # process coins



coin_box = 0
machine_on = True

while machine_on:
    coffee_machine()




# TODO Check for sufficient resources to make the drink

# TODO process coins

# TODO Check that the user has inserted enough money

# TODO Make Coffee
