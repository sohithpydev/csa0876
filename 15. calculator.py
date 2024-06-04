def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero.")
            return None
        else:
            return num1 / num2
    else:
        print("Invalid operator.")
        return None

while True:
    num1 = float(input("Enter a number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter another number: "))
    result = calculate(num1, operator, num2)
    if result is not None:
