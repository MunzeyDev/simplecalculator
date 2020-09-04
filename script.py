print("ADDITION = (+) | SUBTRACTION = (-) | MULTIPLICATION = (*) | DIVISION = (/)")
print("")
op1 = input("Enter an operator: ")
num1 = int(input("What is your first number?: "))
num2 = int(input("What is your second number?: "))
print("")
print("Your answer is: ")
if op1 == "+":
    print(num1 + num2)
elif op1 == "-":
    print(num1 - num2)
elif op1 == "*":
    print(num1 * num2)
elif op1 == "/":
    print(num1 / num2)
