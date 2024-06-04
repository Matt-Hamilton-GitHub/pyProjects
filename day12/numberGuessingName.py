
from art import guessingName
import random

def setRange(diff):
    if diff == 'hard':
        return 100
    else:
        return 30

def guessingGame():
    print(guessingName + '\n')

    tryAgain = 'Y'
    

    while tryAgain == 'Y':
        difficulty = input('Wanna guess a number? Choose your difficulty easy/hard :').lower()
        numRange = setRange(difficulty)  
        number = random.randint(0, numRange)
        print(number)
        print(f'Now, geuess a number between 0 and {numRange}. Good luck!')

        attempts = 5
        while attempts > 0:
            print(f'You have {attempts} attempts remaining.')
            guess = int(input('Make a guess: '))
            attempts-=1

            if guess == number:
                print(f'Congrats! You got it right with {attempts} remainig!')
                
                break
            else:
                if guess - number > 10:
                    print('Way too high')
                elif guess - number < -10:
                    print('Way too low')
                elif guess < number:
                    print('Too Low')
                elif guess > number:
                    print('Too High')


    
        if attempts == 0:
            print("You Lost! No Attempts Left")

        tryAgain = input("Would you like like to try again? Y/N: ").upper()


guessingGame()