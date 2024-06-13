def nth_largest_number(numbers, n):
    sorted_numbers = sorted(set(numbers), reverse=True)

    if 1 <= n <= len(sorted_numbers):
        return sorted_numbers[n - 1]
    else:
        return None

def main():
    try:
        numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
        n = int(input("Enter the value of N to find the Nth largest number: "))

        result = nth_largest_number(numbers, n)

        if result is not None:
            print(f"The {n}th largest number in the list is: {result}")
        else:
            print("Invalid value of N. Please enter a valid positive integer.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
