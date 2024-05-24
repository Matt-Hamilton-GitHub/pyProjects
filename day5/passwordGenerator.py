import random as r

lettersSpace = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbersSpace = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbolsSpace = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

totalList = [
    [nr_letters, lettersSpace], 
    [nr_symbols, symbolsSpace], 
    [nr_numbers, numbersSpace]
]

optionsAvailable = []
if nr_letters > 0:
    optionsAvailable.append(0)
if nr_symbols > 0:
    optionsAvailable.append(1)
if nr_numbers > 0:
    optionsAvailable.append(2)

print(r.choice(numbersSpace))
print(r.shuffle(symbolsSpace))
print(symbolsSpace)
print(r.shuffle(symbolsSpace))

print(symbolsSpace)
password = ""
while len(optionsAvailable) > 0:
    rand = r.randint(0, len(optionsAvailable) - 1)
    randomPick = optionsAvailable[rand]
    #decrease the number 
    totalList[randomPick][0] = totalList[randomPick][0] - 1
    if totalList[randomPick][0] == 0:
        optionsAvailable.remove(randomPick)
    
    print(randomPick, totalList[randomPick][0] )
    randomListChar = r.randint(0, len(totalList[randomPick][1]) - 1)
    print(randomListChar,totalList[randomPick][1][randomListChar] )
    password += totalList[randomPick][1][randomListChar]

if len(password) < 6 : print('WARNING: Your password is too short')
print(f'Your password: {password}')
    
    
    





