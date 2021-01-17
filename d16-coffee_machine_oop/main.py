from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def run():
    global machine_on
    global coin_box

    # prompt user
    choice = input(f"What would you like? {menu.get_items()}: ")
    
    # turn off cofee machine with off command
    if choice == "off":
        print("Turning coffee machine off\n")
        machine_on = False

    # print report
    elif choice == "report":
        coffeemaker.report()
     
    # Check for sufficient resources
    elif menu.find_drink(choice) != None:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink):
            # process coins
            if moneymachine.make_payment(drink.cost):
                #process transaction (enough money, make change, update coinbox)
                coffeemaker.make_coffee(drink)

machine_on = True
coin_box = 0

# instantiate objects
menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

while machine_on:
    run()