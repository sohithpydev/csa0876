def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    try:
        number = int(input("Enter a non-negative integer to calculate factorial: "))
        if number >= 0:
            result = factorial(number)
            print(f"The factorial of {number} is: {result}")
        else:
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")

if __name__ == "__main__":
    main()
