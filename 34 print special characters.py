def print_special_characters(line):
    special_characters = ""
    special_count = 0

    for char in line:
        if not char.isalnum() and not char.isspace():
            special_characters += char
            special_count += 1

    print("Special characters:", special_characters)
    print("Number of special characters:", special_count)

def main():
    input_line = input("Enter a line of text: ")
    print_special_characters(input_line)

if __name__ == "__main__":
    main()
