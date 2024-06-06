from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_menu = Menu()
payment = MoneyMachine()
make_coffee = CoffeeMaker()


run = 'Y'
while run == 'Y':
    
    userReq = input(f'Please, make your order: {my_menu.get_items()}: ').lower()
    
    if userReq == 'report':
        make_coffee.report()
        payment.report()

    elif my_menu.find_drink(userReq) :
        drink = my_menu.find_drink(userReq)
        if make_coffee.is_resource_sufficient(drink) and payment.make_payment(drink.cost):
            make_coffee.make_coffee(drink)
           
    

    
    run = input('Would you like to make another order? (y/n) : ').upper()
    

