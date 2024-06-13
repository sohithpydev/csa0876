from statistics import mean, median, mode

def calculate_mean_median_mode(numbers):
    # Calculate mean, median, and mode using built-in functions
    mean_value = mean(numbers)
    median_value = median(numbers)
    
    try:
        mode_value = mode(numbers)
    except StatisticsError:
        mode_value = "No unique mode"

    return mean_value, median_value, mode_value

def main():
    # Example array of numbers
    numbers = [2, 3, 1, 4, 3, 5, 2, 6, 4, 8, 3]

    mean_value, median_value, mode_value = calculate_mean_median_mode(numbers)

    print("Array of numbers:", numbers)
    print("Mean:", mean_value)
    print("Median:", median_value)
    print("Mode:", mode_value)

if __name__ == "__main__":
    main()
