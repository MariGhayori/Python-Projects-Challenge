from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

ON = True

theMenu = Menu()
makerCoffee = CoffeeMaker()
machineMoney = MoneyMachine()

while ON:
    theChoice = input(f"What Would you Like to Order? ({theMenu.get_items()})").lower()

    if theChoice == 'off':
        ON = False
    elif theChoice == 'report':
        print(makerCoffee.report())
        print(machineMoney.report())
    else:
        theOrder = theMenu.find_drink(theChoice)
        if makerCoffee.is_resource_sufficient(theOrder) == True :
            Ccost = theOrder.cost
            print(f"{theOrder.name} costs {theOrder.cost}")
            if machineMoney.make_payment(Ccost) == True:
                makerCoffee.make_coffee(theOrder)
        


