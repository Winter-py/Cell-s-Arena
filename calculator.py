a = int (input('insert a number '))
operator = input('insert an operator ')
b = int (input('insert a number '))

def add(a,b):
    result = a + b
    print(result)

def subtract(a, b):
    result = a - b
    print(result)

def multiply(a, b):
    result = a * b
    print(result)

def divide(a, b):
    result = a / b
    print(result)

def power(a, b):
    result = a ** b
    print(result)

def unknown(a, b):
    result = a // b
    print(result)

# Run all the calculations through a if statement

if operator == '+':
    add(a,b)
elif operator == '-':
    subtract(a,b)
elif operator == '*':
    multiply(a,b)
elif operator == '/':
    divide(a,b)
elif operator == '**':
    power(a,b)
elif operator == '//':
    unknown(a,b)   
else:
    print('invalid operator')
    

