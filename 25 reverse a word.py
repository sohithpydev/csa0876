def reverse_words(input_string):
    words = input_string.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string

def main():
    input_string = input("Enter a string: ")
    reversed_string = reverse_words(input_string)
    print("Reversed words in the string:", reversed_string)

if __name__ == "__main__":
    main()
