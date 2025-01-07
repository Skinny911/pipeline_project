# Calculator functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

# Interactive calculator logic
def main():
    print('Welcome to this calculator!')
    print('Add, subtract, multiply, and divide numbers')

    # Collect user inputs
    num1 = int(input('First number: '))
    sign = input('Sign? +, -, /, or *: ')
    num2 = int(input('Second number: '))

    # Preform calculations
    if sign == '+':
        print(add(num1, num2))
    elif sign == '-':
        print(subtract(num1, num2))
    elif sign == '*':
        print(multiply(num1, num2))
    elif sign == '/':
        print(divide(num1, num2))
    else:
        print("Invalid operator. Please use +, -, /, or *.")

if __name__ == "__main__":
    main()
