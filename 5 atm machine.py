def calculate_total_amount(denominations, notes):
    total_amount = 0
    for denomination, count in zip(denominations, notes):
        total_amount += denomination * count
    return total_amount

def main():
    # Denominations available in the ATM
    available_denominations = [2000, 500, 200, 100]

    # Get the denomination priority and total number of notes from the user
    notes = []
    for denomination in available_denominations:
        count = int(input(f"Enter the number of {denomination}-rupee notes: "))
        notes.append(count)

    # Calculate and print the total available balance
    total_balance = calculate_total_amount(available_denominations, notes)
    print(f"Total available balance in the ATM: {total_balance} rupees")

if __name__ == "__main__":
    main()
