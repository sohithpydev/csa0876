def count_special_characters(statement):
    special_characters = 0
    for char in statement:
        if not char.isalnum() and char != ' ':
            special_characters += 1
    return special_characters

# Sample Input
given_statement = "Modi Birthday @ September 17, #&$% is the wishes code for him."

# Count special characters
num_special_characters = count_special_characters(given_statement)

# Display the result
print("Number of special characters:", num_special_characters)
