import random as r
import os
def blackjack():

    def drawCard():
        return r.randint(2,10)
    
    def beginGame():
        return [drawCard(),drawCard()]
    
    def getScore(arr):
        total = 0
        for i in arr:
            total+=i
        return total
 
    gameOver = 'Y'
    userCards = beginGame()
    computerCards = beginGame()

    gameOver = input("Do you want to play Blackjack? (Y/N): ").upper()
  
    while gameOver == 'Y':
        os.system('cls')

        print(f'Your cards: {userCards}, Current Score: {getScore(userCards)}')
        print(f'Computer First Card: {computerCards[0]}')
        print('-------------------------------------------')
        draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if draw == 'y':
            userCards.append(drawCard())
            if getScore(computerCards) + 4 < 21:
                computerCards.append(drawCard())
        else:
            if getScore(computerCards) + 4 < 21:
                computerCards.append(drawCard())
            os.system('cls')
            print(f'Your final hand: {userCards}, Current Score: {getScore(userCards)}')
            print(f"Computer's final hand : {computerCards}, Current Score: {getScore(computerCards)}")

            if getScore(userCards) > 21 and getScore(computerCards) <= 21:
                print('You lost')
                gameOver = input("Do you want to play Blackjack again? (Y/N): ").upper()
                if gameOver == 'Y':
                    userCards = beginGame()
                    computerCards = beginGame()
                    

            if getScore(computerCards) > 21 and getScore(userCards) <= 21:
                print('Congrats! You WON')
                gameOver = input("Do you want to play Blackjack again? (Y/N): ").upper()
                if gameOver == 'Y':
                    userCards = beginGame()
                    computerCards = beginGame()
            elif getScore(userCards) <= 21 and getScore(userCards) > getScore(computerCards):
                print('Congrats! You WON')
                gameOver = input("Do you want to play Blackjack again? (Y/N): ").upper()
                if gameOver == 'Y':
                    userCards = beginGame()
                    computerCards = beginGame()
            elif getScore(userCards) <= 21 and getScore(userCards) == getScore(computerCards):
                print('Draw')
                gameOver = input("Do you want to play Blackjack again? (Y/N): ").upper()
                if gameOver == 'Y':
                    userCards = beginGame()
                    computerCards = beginGame()
            elif getScore(computerCards) > 21 and getScore(userCards) > 21:
                print("No winners this time")
                gameOver = input("Do you want to play Blackjack again? (Y/N): ").upper()
                if gameOver == 'Y':
                    userCards = beginGame()
                    computerCards = beginGame()
            else:
                print('Sorry buddy, You Lost!')
                gameOver = input("Do you want to play Blackjack again? (Y/N): ").upper()
                if gameOver == 'Y':
                    userCards = beginGame()
                    computerCards = beginGame()
                
        
         
      

       


blackjack()