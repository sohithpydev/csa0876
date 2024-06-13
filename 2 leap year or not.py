def is_leap_year(year):
    # Leap year if divisible by 4, but not divisible by 100 unless divisible by 400
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def find_next_anniversary(current_year):
    while True:
        current_year += 1
        if is_leap_year(current_year):
            return current_year

def find_previous_anniversary(current_year):
    while True:
        current_year -= 1
        if is_leap_year(current_year):
            return current_year

# Input: Replace 2000 with the desired year for the anniversary
anniversary_year = 2000

if is_leap_year(anniversary_year):
    next_anniversary = find_next_anniversary(anniversary_year)
    print(f"{anniversary_year} is a leap year. The next anniversary in a leap year is {next_anniversary}.")
else:
    previous_anniversary = find_previous_anniversary(anniversary_year)
    print(f"{anniversary_year} is not a leap year. The previous anniversary in a leap year is {previous_anniversary}.")
