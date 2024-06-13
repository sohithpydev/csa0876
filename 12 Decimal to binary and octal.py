def decimal_to_binary(decimal_number):
    binary_representation = bin(decimal_number)[2:]
    return binary_representation

def decimal_to_octal(decimal_number):
    octal_representation = oct(decimal_number)[2:]
    return octal_representation

# Get input from the user
decimal_input = int(input("Enter a decimal number: "))

# Convert to binary and octal
binary_result = decimal_to_binary(decimal_input)
octal_result = decimal_to_octal(decimal_input)

# Display the results
print(f"Binary equivalent: {binary_result}")
print(f"Octal equivalent: {octal_result}")
