from art import logo
import os




def getWinner(dic):
        winner = next(iter(dic))
        for k, v in dic.items():
            if dic[winner] < v:
                winner = k

        return winner

def auction():

    print(logo)
    print('Welcome to the secret auction program')
    
    
    bidsDic = {}
    again = 'YES'
    while again == 'YES':
        username = input('What is your name ?: ')
        bid = float(input('What is yout bid: $'))
        bidsDic[username] = bid

        again = input("Are there any other bidders? Type 'yes' or 'no'. \n").upper()
        os.system("cls")
    winner = getWinner(bidsDic)
    return f'{winner} WINS with a bid of ${bidsDic[winner]})'


print(auction())