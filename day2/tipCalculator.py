import math

print('Welcome to the Tip Calculator')
bill = float(input('What was the total bill? $\n'))
tip = float(input('How much tip would you like to give? (%) \n'))
splitBetween = int(input('How many people to split the bill \n'))

if splitBetween == 0: splitBetween = 1

result = bill + bill * (tip * 0.01)
print(f'Each person should pay: ${round(result/splitBetween, 2)}')
