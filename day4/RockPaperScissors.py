
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

actionsSpace = [rock, paper, scissors]
again = True

while again:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))
    
    print(actionsSpace[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer chose: ")
    print(actionsSpace[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print('You WIN!')
    elif user_choice == 1 and computer_choice == 0:
        print('You WIN!')
    elif user_choice == 2 and computer_choice == 1:
        print('You WIN!')
    else:
        print('You LOSE!')

    if user_choice == computer_choice:
        print('DRAW')
    else:
        c = input("Wanna Play agin? (Y/N)").upper()
        if c == 'N':
            again = False

    
    
        
