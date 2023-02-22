from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# print report
# check sufficient resources
# process coins
# check if transaction is success
# make coffee


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()



is_on = True

while is_on:
    options = menu.get_items() # string of all coffee types
    choice = input(f"What would you like to drink? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        


