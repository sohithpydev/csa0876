def main():
    
    word = input("Enter the word: ")

    sorted_word = ''.join(sorted(word, reverse = True))
                          
    print("Alphabetical Order:", sorted_word )

if __name__ == "__main__":
    main()

