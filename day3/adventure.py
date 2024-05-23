print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
action1 = input("You have two optins to go: RIGHT or LEFT: ").upper()

if action1 != 'LEFT':
    print("You fall into a hole. GAME OVER")
    exit(0)

print("Now, you see a beauiful deep river in front of you") 
action2 = input("Do you want to SWIM to the other side or WAIT for a boat: (SWIM/WAIT): ").upper()
if action2 != 'WAIT':
    print("You were attacked by trout. GAME OVER")
    exit(0)
print("It appears that this side of the river has a tall building with 3 doors: RED, BLUE, AND YELLOW") 
action3 = input("What door do you want to open? (RED/BLUE,YELLOW)? :").upper()
if action3 == 'RED':
    print("You were BURNED by fire. GAME OVER")
    exit(0)
elif action3 == 'BLUE':
    print("You were EATEN by beasts. GAME OVER")
    exit(0)
elif action3 == 'YELLOW':
    print("You WIN. THE ALL GOLD IN THE WORLD IS YOURS NOW")
    exit(0)
else:
    print("GAME OVER")