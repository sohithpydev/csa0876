def count_characters(file_path):
    space_count = 0
    line_count = 0
    vowel_count = 0
    consonant_count = 0

    vowels = "aeiouAEIOU"

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line_count += 1
                for char in line:
                    if char.isspace():
                        space_count += 1
                    elif char.isalpha():
                        if char in vowels:
                            vowel_count += 1
                        else:
                            consonant_count += 1

    except FileNotFoundError:
        print("File not found.")
        return None

    return space_count, line_count, vowel_count, consonant_count

def main():
    file_path = input("Enter the file path: ")

    counts = count_characters(file_path)

    if counts is not None:
        space_count, line_count, vowel_count, consonant_count = counts

        print(f"Number of spaces: {space_count}")
        print(f"Number of lines: {line_count}")
        print(f"Number of vowels: {vowel_count}")
        print(f"Number of consonants: {consonant_count}")

if __name__ == "__main__":
    main()
