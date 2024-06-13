def check_eligibility(age):
    voting_age = 18

    if age >= voting_age:
        print("You are eligible to vote.")
    else:
        years_left = voting_age - age
        print(f"You are not eligible to vote. You need to wait for {years_left} more years.")

def main():
    # Get the age of the person from the user
    age = int(input("Enter your age: "))

    # Check eligibility and print the result
    check_eligibility(age)

if __name__ == "__main__":
    main()
