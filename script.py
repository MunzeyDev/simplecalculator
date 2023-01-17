def main():

    num1 = int(input("What is your first number?: "))
    print()
    print("ADDITION = (+) | SUBTRACTION = (-) | MULTIPLICATION = (*) | DIVISION = (/)")
    op1 = input("Enter an operator: ")
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
    print("")
    Repeat = input("Would you like to try it again?").lower()
    if Repeat == "yes":
        print()
        main()
    else:
        print("")
        print("Goodbye")
        exit()
main()
