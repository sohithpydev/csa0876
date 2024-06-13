def calculate_power(x, n):
    return x ** n

def calculate_addition(x, n):
    return x + n

def calculate_subtraction(x, n):
    return x - n

def calculate_multiplication(x, n):
    return x * n

def calculate_division(x, n):
    if n != 0:
        return x / n
    else:
        return "Cannot divide by zero."

def main():
    x = float(input("Enter the value of x: "))
    n = float(input("Enter the value of n: "))

    print("\nSelect operation:")
    print("1. Power")
    print("2. Addition")
    print("3. Subtraction")
    print("4. Multiplication")
    print("5. Division")

    choice = int(input("Enter choice (1/2/3/4/5): "))

    result = 0

    if choice == 1:
        result = calculate_power(x, n)
    elif choice == 2:
        result = calculate_addition(x, n)
    elif choice == 3:
        result = calculate_subtraction(x, n)
    elif choice == 4:
        result = calculate_multiplication(x, n)
    elif choice == 5:
        result = calculate_division(x, n)
    else:
        print("Invalid choice. Please choose a valid operation.")

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
