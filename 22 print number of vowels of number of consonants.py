def count_vowels_and_consonants(statement):
    vowels = "aeiouAEIOU"
    statement = statement.lower()  # Convert the statement to lowercase for case-insensitivity
    vowel_count = 0
    consonant_count = 0

    for char in statement:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

def main():
    statement = input("Enter a statement: ")
    vowel_count, consonant_count = count_vowels_and_consonants(statement)

    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)

    if vowel_count > consonant_count:
        print("Vowels are greater.")
    elif consonant_count > vowel_count:
        print("Consonants are greater.")
    else:
        print("Equal number of vowels and consonants.")

if __name__ == "__main__":
    main()
