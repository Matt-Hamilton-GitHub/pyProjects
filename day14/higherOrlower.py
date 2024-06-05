from art import vs, logo
from gameData import data
import random as r
import os
import time




def HigherORLower():
    SCORE = 0

    def getRandomIntNotEqual(range, notE):
        num = notE
        while num == notE:
            num = r.randint(0, range)
        
        return num
    

    print(logo)
    print('Compare which celebrity has more followers on Instagram')

    tryAgain = 'Y'
    
    while tryAgain == 'Y':


        aIdx = r.randint(0, len(data) - 1)
        bIdx = r.randint(0, len(data) - 1)
        correct = True

        while correct:
             
            os.system('cls')
            print(f"------------------ SCORE: {SCORE} ------------------")
            print(f"Compare A: {data[aIdx]['name']}, {data[aIdx]['description']}, from {data[aIdx]['country']}")
            print(vs)
            print(f"Compare B: {data[bIdx]['name']}, {data[bIdx]['description']}, from {data[bIdx]['country']}")
            print("---------------------------------------------------")
            choice = input("Who has more followers on Instagram? Type 'A' or 'B': ").upper()

            if data[aIdx]['follower_count'] > data[bIdx]['follower_count']:
                if choice == 'A':
                    SCORE+=1
                    print(f"You're right. Your score went up - {SCORE}")
               
                    aIdx = bIdx
                    bIdx = getRandomIntNotEqual(len(data) - 1, aIdx)
                    time.sleep(2)
                    
                else:
                    print(f'Sorry, You Lost with score {SCORE}')
                    print(f" {data[aIdx]['name']}: {data[aIdx]['follower_count']}")
                    print(vs)
                    print(f"{data[bIdx]['name']}: {data[bIdx]['follower_count']}")
                    correct = False
            elif data[aIdx]['follower_count'] < data[bIdx]['follower_count']:
                if choice == 'B':
                    SCORE+=1
                    print(f"You're right. Your score went up - {SCORE}")
                   
                    bIdx = getRandomIntNotEqual(len(data) - 1, aIdx)
                    time.sleep(2)
                else:
                    print(f'Sorry, You Lost with score {SCORE}')
                    print(f" {data[aIdx]['name']}: {data[aIdx]['follower_count']}")
                    print(vs)
                    print(f"{data[bIdx]['name']}: {data[bIdx]['follower_count']}")
                    correct = False

        tryAgain = input("Whould you like to try again? (Y/N)").upper()
        SCORE = 0


HigherORLower()