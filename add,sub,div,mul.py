def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Example usage:
num1 = 10
num2 = 5

result_add = add(num1, num2)
result_subtract = subtract(num1, num2)
result_multiply = multiply(num1, num2)
result_divide = divide(num1, num2)

print(f"Addition: {num1} + {num2} = {result_add}")
print(f"Subtraction: {num1} - {num2} = {result_subtract}")
print(f"Multiplication: {num1} * {num2} = {result_multiply}")
print(f"Division: {num1} / {num2} = {result_divide}")
