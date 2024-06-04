import random as r
import os
import emoji
import time

def blackjack():

    

    def drawCard():
        return r.randint(2,10)
    
    def beginGame():
        return [drawCard(),drawCard()]
    
    def getScore(arr):
        total = 0
        for i in arr:
            total+=int(i)
        return total
    def getComputerCardsHidden(cards):
        hiddenCards = [str(cards[0])]
        [hiddenCards.append("?") for _ in range(len(cards) - 1)]
        return hiddenCards

    

    
    def displayMidResults():
        print(f'Your cards: {userCards}, Current Score: {getScore(userCards)}')
        print(f'Computer First Card: {getComputerCardsHidden(computerCards)}')
        print('-------------------------------------------')
        
    def displayFinalResults():
        os.system('cls')
        time.sleep(1)
        print(f'Your final hand: {userCards}, Current Score: {getScore(userCards)}')
        time.sleep(1)
        print(f"Computer's final hand : {computerCards}, Current Score: {getScore(computerCards)}")

        if winner == 'user':
            print(f"Congrats. You won! {emoji.emojize(':beaming_face_with_smiling_eyes:')}")
        elif winner == 'draw':
            print(f"Draw! No winners this time {emoji.emojize(':winking_face:')}")
        else:
            print(f"You Lost {emoji.emojize(':smiling_face_with_tear:')}")

    
    userCards = beginGame()
    computerCards = beginGame()
    winner = ""
        

    play = input(f"Do you want to play Blackjack? {emoji.emojize(':club_suit:')} (Y/N): ").upper()

    os.system('cls')
    print('shuffling cards .')
    time.sleep(1)
    os.system('cls')
    print('shuffling cards ..')
    time.sleep(1)
    os.system('cls')
    print('shuffling cards ...')
    time.sleep(1)
    os.system('cls')

    while play == 'Y':
        os.system('cls')

        displayMidResults()
        getNewCard = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        os.system('cls')

        #user draws cards as long as needs
        while getNewCard == 'y':
            if getNewCard == 'y':
                userCards.append(drawCard())
                #computer player also takes cards if needed
                if getScore(computerCards) + 4 <= 21:
                    computerCards.append(drawCard())
                    print(f"Computer player drew one more card {emoji.emojize(':thinking_face:')}")
                    time.sleep(1)

            displayMidResults()
            getNewCard = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            os.system('cls')
            
        #check if the computer player needs more cards - to make the game more fair
        while getScore(computerCards) + 4 <= 21:
            computerCards.append(drawCard())
            print(f"Computer player drew one more card {emoji.emojize(':thinking_face:')}")
            time.sleep(1)

        #COMPUTE RESULTS
        if getScore(userCards) <= 21 and getScore(computerCards) <= 21:

            if getScore(userCards) > getScore(computerCards):
                winner = 'user'
            elif getScore(userCards) == getScore(computerCards):
                winner = 'draw'
            else:
                winner = 'computer'

        elif getScore(userCards) <= 21 and getScore(computerCards) > 21:
            winner = 'user'
        elif  getScore(userCards) > 21 and getScore(computerCards) > 21:
            winner = 'draw'
        else:
            winner = 'computer'


        #DISAPLAY THE RESULTS 
        displayFinalResults()

        play = input('Would you like to play again? (y/n) :').upper()

        #RESET
        userCards = beginGame()
        computerCards = beginGame()
        winner = ""



                
        
         
      

       


blackjack()