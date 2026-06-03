# Simple Calculator

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print("Result =", result)

elif operator == "-":
    result = num1 - num2
    print("Result =", result)

elif operator == "*":
    result = num1 * num2
    print("Result =", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)
    else:
        print("Division by zero is not allowed.")

else:
    print("Invalid operator!")
    