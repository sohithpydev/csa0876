def reverse_word(word):
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return reversed_word

def main():
    # Get the word from the user
    input_word = input("Enter a word: ")

    # Reverse the word and print the result
    reversed_result = reverse_word(input_word)
    print(f"The reversed word is: {reversed_result}")

if __name__ == "__main__":
    main()
