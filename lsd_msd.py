# Given number
number = int(input("enter a number:"))
# Convert number to string to easily access digits
number_str = str(number)

# Least Significant Digit (LSD) is the last digit
lsd = number_str[-1]

# Most Significant Digit (MSD) is the first digit
msd = number_str[0]

print("Least Significant Digit (LSD):", lsd)
print("Most Significant Digit (MSD):", msd)
