def multiplication_table(m, n):
    for i in range(1, n + 1):
        result = m * i
        print(f"{m} x {i} = {result}")

# Get input from the user
number_m = int(input("Enter the number for the multiplication table: "))
up_to_n = int(input("Enter the value of 'n' for the table up to n: "))

# Print the multiplication table
multiplication_table(number_m, up_to_n)
