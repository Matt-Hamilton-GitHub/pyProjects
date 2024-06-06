from info import MENU, DRINKS_IDX
from keys import KEY
import time
import os


RESOURCES = 'resources.txt'
ING_IDX_DIC = {"water": 0, 'milk': 1, 'coffee': 2}
#commands
REPORT = 'report'
ADD_WATER = 'add water'
ADD_MILK = 'add milk'
ADD_COFFEE = 'add coffee'
WITHDRAW_COINS = 'withdraw coins'
ADD_COINS = 'add coins'


def printMenu():
    print("############################################")
    print("---------------TODAY'S MENU-----------------")
    i = 0
    for k in MENU.keys():
        print(str(i) + ") " +k.upper())
        i+=1
    print("--------------------------------------------")

def printReport():
    os.system('cls')
    print('GENERATION THE REPORT.')
    time.sleep(1)
    os.system('cls')
    print('GENERATION THE REPORT..')
    time.sleep(1)
    os.system('cls')
    print('GENERATION THE REPORT...')
    time.sleep(1)
    os.system('cls')

    with open(RESOURCES, 'r') as file:
        data = [int(x) for x in next(file).split()]
    file.close()

    print("############################################")
    print("---------------- RESOURCES -----------------")
    print(f"Water level {data[0]} ml")
    print(f"Milk level {data[1]} ml")
    print(f"Coffee level {data[2]} g")
    print("                      ------                 ")
    print(f"Amount of Quarters: {data[3]} qty")
    print(f"Amount of Dimes: {data[4]} qty")
    print(f"Amount of Nickles: {data[5]} qty")
    print(f"Amount of Pennies: {data[6]} qty")
    print("--------------------------------------------")
    print("############################################")


def calculateTotalAmount(q, d, n, p):
    return q*.25 + d*0.1 + n*.05 + p*.01

def updateResources(action, w, m, c):
    with open(RESOURCES, 'r') as file:
        data = [int(x) for x in next(file).split()]

    # data = file.read().split()
    res = data[0:3]
    coins = data[3:7]
    file.close()


    if action == 'remove':
        res[0] -= w
        res[1] -= m
        res[2] -= c
    else:
        res[0] += w
        res[1] += m
        res[2] += c
    
    file = open(RESOURCES, 'w')
    for x in res + coins:
        file.write(str(x) + ' ')
    file.close()

    # print('UPDATING RESOURCES . ')
    # time.sleep(1)
    # print('UPDATING RESOURCES . . ')
    # time.sleep(3)
    # print('UPDATING RESOURCES . . .')
    # time.sleep(5)

    # print(f"RESOURCES SUCCESSFULLY REPLENISHED ")

def checkResources(r, drink):
   
    with open(RESOURCES, 'r') as file:
        data = [int(x) for x in next(file).split()]
    data = data[0:3]
    file.close()
    print(data)
    print(MENU[drink]['ingredients']['coffee'])

    ing = [i for i in MENU[drink]['ingredients'].items()]
    print(ing)

    for k in ing:
        print(k)
        if data[ING_IDX_DIC[k[0]]] < MENU[drink]['ingredients'][k[0]]:
             return 1 
       

    return 0    
        
def getChange(coast, q, d, n, p):
    
    change = round(calculateTotalAmount(q, d, n, p) - coast, 2)
    remaining = change
    print(change, remaining, q, d, n, p)
    
   
    if q != 0:
        while remaining > 0.25  and q != 0:
            q-=1
            remaining-=0.25
    if d != 0:
        while remaining > 0.10 and d != 0:
            d-=1
            remaining-=0.10
    if n != 0:
        while remaining > 0.050  and n != 0:
            n-=1
            remaining-=0.050
    if p != 0:
        while remaining > 0.0095 and p != 0:
            p-=1
            remaining-=0.01

    print(change, remaining, q, d, n, p)
    return change , q, d, n, p

    
    
def addCoins(q,d,n,p):
    with open(RESOURCES, 'r') as file:
        data = [int(x) for x in next(file).split()]

    # data = file.read().split()
    res = data[0:3]
    coins = data[3:7]

    coins[0] += q
    coins[1] += d
    coins[2] += n
    coins[3] += p
    file.close()
    
    
    file = open(RESOURCES, 'w')
    for x in res + coins:
        file.write(str(x) + ' ')
    file.close()


def removeCoins(q,d,n,p):
    with open(RESOURCES, 'r') as file:
        data = [int(x) for x in next(file).split()]

    # data = file.read().split()
    res = data[0:3]
    coins = data[3:7]

    coins[0] -= q
    coins[1] -= d
    coins[2] -= n
    coins[3] -= p
    file.close()
    
    
    file = open(RESOURCES, 'w')
    for x in res + coins:
        file.write(str(x) + ' ')
    file.close()
    

# def withdrawCoins():
def makeDrink(drinkName):
    drink = MENU[drinkName]
    print(drink)

    if checkResources('drink', drinkName) == 1:
        return 1
    return 0

def adminMenu():
    run = "Y"
    while run == 'Y':

        os.system('cls')
        print('############### Welcome Master ###############')
        print('1) PRINT REPORT ')
        print('2) REPLENISH RESOURCES')
        print('3) ADD COINS')
        print('4) WITHDRAW COINS')
    
        command = int(input('Please, select your command: '))

        if command == 1:
            printReport()
        elif command == 2:
            inputRes = input("Enter amount of resources for [water] [milk] [coffee]: ")
            addRes = inputRes.split()
            updateResources('add', int(addRes[0]), int(addRes[1]), int(addRes[2]))
        elif command == 3:
            inputCoins = input("Enter amount of coins for: [QUARTERS] [DIMES] [NICKLES] [PENNIES]: ")
            coins = inputCoins.split()
            addCoins(int(coins[0]), int(coins[1]), int(coins[2]), int(coins[3]))
            print(f"COINS SUCCESSFULLY ADDED ")
        elif command == 4:
            inputCoins = input("Enter amount of coins to withdraw: [QUARTERS] [DIMES] [NICKLES] [PENNIES]: ")
            coins = inputCoins.split()
            removeCoins(int(coins[0]), int(coins[1]), int(coins[2]), int(coins[3]))
            print(f"COINS SUCCESSFULLY REMOVED")


        run = input("Would you like to run more commands? (y/n): ").upper()
    
   

def interface():

    order = 'Y'
    while order == 'Y':
        printMenu()
        commandInput = int(input('What Would You Like? Enter Number from the MENU: '))
        
        print("#########################################")

        if commandInput < len(MENU.items()):
            drink = DRINKS_IDX[commandInput]

            print("Please, insert coins: ")
            q = int(input('How many quarters?: '))
            d = int(input('How many dimes?: '))
            n = int(input('How many nickles?: '))
            p = int(input('How many pennies?: '))

            if makeDrink(drink) != 0:
                print(f"Sorry, we ran out of resources. Refunded: ${calculateTotalAmount(q,d,n,p)}")
            else:
                if calculateTotalAmount(q,d,n,p) < MENU[drink]['cost']:
                     print(f"Sorry, you're missing some coins. Refunded: ${calculateTotalAmount(q,d,n,p)}")
                else:
                    change, qn,dn,nn,pn = getChange(MENU[drink]['cost'], q, d, n, p)
                    addCoins(qn,dn,nn,pn)

                    updateResources('remove',  MENU[drink]['ingredients']['water'], MENU[drink]['ingredients']['milk'], MENU[drink]['ingredients']['coffee'])
                    if change != 0.0:
                        print(f"Here is your change: ${change}")
                    print(f'Enjoy your {drink}')

        elif commandInput == 55:
           adminMenu()
           exit()
        else:
            print(f"Sorry, we have only {len(MENU.items())} items.")
        
        order = input('Would you like to order again? (Y/N): ').upper()
        os.system('cls')


interface()
