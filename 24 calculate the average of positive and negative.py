def calculate_average(numbers):
    if not numbers:
        return 0  # Avoid division by zero if the list is empty
    return sum(numbers) / len(numbers)

def main():
    positive_numbers = []
    negative_numbers = []

    while True:
        num = float(input("Enter a number (-1 to stop): "))

        if num == -1:
            break

        if num > 0:
            positive_numbers.append(num)
        elif num < 0:
            negative_numbers.append(num)

    average_positive = calculate_average(positive_numbers)
    average_negative = calculate_average(negative_numbers)

    print(f"Average of positive numbers: {average_positive}")
    print(f"Average of negative numbers: {average_negative}")

if __name__ == "__main__":
    main()
