from art import logo
import os
def operation(operands_list, operation):
   
    try:
        output = operands_list[0]
        for n in operands_list[1:]:
            code = f'{output} {operation} {n}'
            output = eval(code)
    except:
        print('Error')
    return output

def calculator():
    
    perform = 'Y'
    while perform == 'Y':
        print(logo)
        numbers = input('Enter each operand followed by space:  ')
        op = input('Enter operation ypu would like to performe ( + - / * ): ')
        num_list = numbers.split()

        print(f'{operation(num_list, op)}')
        perform = input('Perfome another operation? (Y/N): ').upper()


calculator()


