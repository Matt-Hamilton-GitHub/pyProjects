import random as r
from hangman_art import heart, stages
from hangmanwords import word_list
#logic:
#1)select a random word from a list
#2)keep the word or its index while 

player_lives = [heart for _ in range(6)] 
random_word = r.choice(word_list).upper()
r_word_list = [char.upper() for char in random_word]
guessed = ['_' for _ in random_word]
#create a guested 

def diplayStats():
    print(f"WORD: {guessed}  ", end=" ")
    for x in range(len(player_lives)):
        print(player_lives[x], end=" ")

    print(stages[len(player_lives)])

while len(player_lives) > 0 and guessed != r_word_list:

    diplayStats()
    userChoice = input("\nEnter your letter: ").upper()

    if userChoice in random_word:
        for x in range(len(r_word_list)):
            if r_word_list[x] == userChoice:
                guessed[x] = userChoice.upper()   
    else:
        print(f"There's no {userChoice.upper()} in the word")   
        player_lives.pop()
                

print("----------------------------------")
if guessed == r_word_list:
    print(f"Congrats! You saved one life 🎉 \n" )
else:
    print("You LOST \n")