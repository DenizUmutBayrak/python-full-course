#Calculator


number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

operator = input("Enter one operator(+ - / *)")

if operator == "+":
    result = number1 + number2
    print(round(result, 3))
elif operator == "-":
    result = number1 - number2
    print(round(result,3))
elif operator == "*":
    result = number1 * number2
    print(round(result, 3))
elif operator == "/":
    result = number1 / number2
    print(round(result, 3))
else:
    print("Invalid operator")
