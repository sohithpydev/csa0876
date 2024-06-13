def print_numbers_with_skip(m, n, k):
    for i in range(m, n + 1, k + 1):
        print(i, end=" ")

# Get input from the user
start_number = int(input("Enter the starting number (M): "))
end_number = int(input("Enter the ending number (N): "))
skip_number = int(input("Enter the number of elements to skip (K): "))

# Print numbers with skip
print_numbers_with_skip(start_number, end_number, skip_number)
