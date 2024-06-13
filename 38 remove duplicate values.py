def remove_duplicates(sorted_array):
    unique_array = []

    for num in sorted_array:
        if not unique_array or num != unique_array[-1]:
            unique_array.append(num)

    return unique_array

def main():
    try:
        sorted_array = [int(x) for x in input("Enter a sorted array of numbers separated by space: ").split()]

        unique_array = remove_duplicates(sorted_array)

        print("Array after removing duplicates:", unique_array)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
