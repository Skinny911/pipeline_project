print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers from 0 to 50')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))
                             
if sign == '+':
    print(num1 + num2)
elif sign == '-': 
    print(num1 - num2)
elif sign == '*': 
    print(num1 * num2)
elif sign == '/': 
    print(num1 * num2)
else: 
    print("Invalid operator. Please use +, -, or *.")

print("Thanks for using this calculator, goodbye :)")
