def remove_duplicates(sorted_array):
    unique_elements = []
    for num in sorted_array:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements

# Sample Input
input_array = [15, 14, 25, 14, 32, 14, 31]

# Remove duplicates
output_array = remove_duplicates(sorted(input_array))

# Display the result
print("Sorted Array =", output_array)
