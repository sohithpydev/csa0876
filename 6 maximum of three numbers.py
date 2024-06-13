def find_maximum(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    # Get three numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Find and print the maximum of the three numbers
    maximum_number = find_maximum(num1, num2, num3)
    print(f"The maximum of {num1}, {num2}, and {num3} is: {maximum_number}")

if __name__ == "__main__":
    main()
