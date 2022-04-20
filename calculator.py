a = int (input('insert a number '))
operator = input('insert an operator ')
b = int (input('insert a number '))

def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    result = a / b
    return result

# Runa all the calculations through a if statement

if operator == '+':
    print(add(a, b))
elif operator == '-':
    print(subtract(a, b))
elif operator == '*':
    print(multiply(a, b))
elif operator == '/':
    print(divide(a, b))
elif operator == '**':
    print(a ** b)
elif operator == '//':
    print(a // b)   
else:
    print('invalid operator')
    break


