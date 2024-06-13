def calculate_tax(income):
    if income <= 150000:
        tax = 0
    elif 150001 <= income <= 300000:
        tax = 0.1 * (income - 150000)
    elif 300001 <= income <= 500000:
        tax = 0.1 * (300000 - 150000) + 0.2 * (income - 300000)
    else:
        tax = 0.1 * (300000 - 150000) + 0.2 * (500000 - 300000) + 0.3 * (income - 500000)
    
    return tax

def main():
    income = float(input("Enter your income: "))
    tax = calculate_tax(income)

    print(f"Tax to be paid: {tax}")

if __name__ == "__main__":
    main()
