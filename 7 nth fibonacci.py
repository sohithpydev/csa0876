def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer for N."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    # Get the value of N from the user
    n = int(input("Enter the value of N to find the Nth Fibonacci number: "))

    # Find and print the Nth Fibonacci number
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")

if __name__ == "__main__":
    main()
