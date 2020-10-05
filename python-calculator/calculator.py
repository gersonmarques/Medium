''' 
This function does the math, it receive the parameters: 
operation: 1 (+), 2(-), 3(*) or 4(/)
n1: the first number to be calculate
n2: the second number to be calculate
 
'''
def calculator(operation, n1, n2):
    if operation == 1:
        return 1 + 1
    
    if operation == 2:
        return n1 - n2
    
    if operation == 3:
        return n1 * n2
    
    elif operation == 4:
        return n1 / n2

# printing the title of my calculator
print("\n******************* Gerson Python Calculator *******************")
print("\n")

# asking the first number to be calculated
firstNumber = int(input("Please, inform the first number: "))
print("\n")

# asking which operation is going to be done
print("Now inform what operation you want to do, according to the options below: ");
print("\n")

# one for sum, two for subtract, 3 for multiply and four for divide
print("1 - Sum");
print("2 - Subtract");
print("3 - Multiply");
print("4 - Divide");
print("\n")

# here, we get the operation
operation = int(input("What operation do want to do? "))
print("\n")

# asking the second number to be calculated
secondNumber = int(input("Now, inform the second number: "))
print("\n")

''' 
here is all the magic start to happen: we send our three parameters (operation, first number and second number) 
to the function 'calculator'. In the variable 'result' will be the result.
'''
result = calculator(operation, firstNumber, secondNumber)

# now all we have to do is inform the result to the user
print("The result is %r" %(result))

# breaking a line
print("\n")

