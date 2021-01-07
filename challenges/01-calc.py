# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.




def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a // b

operators = {
    "add" : add,
    "sub" :  subtract,
    "mult" : multiply,
    "div" : divide
}

def getOperator():
    print("What calculation would you like to do? (add, sub, mult, div)")
    operator = input()
    if (not operators[operator]): 
        print("This is not an available option")
        getOperator()
    else: return operator


def getNumber():
    num = input()
    if (not num.isnumeric()): 
        print('please enter an integer')
    else: 
        return int(num)

def calculator():
    operator = getOperator()
    print('Enter number 1: ')
    num1 = getNumber()
    print(num1)
    print('Enter number 2: ')
    num2 = getNumber()
    result = operators[operator](num1,num2)
    print(f'Your result is {result}')


calculator()

   