# CONVERSION OF GIVEN VALUE TO AN INTEGER
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print(result)
except ZeroDivisionError:
    print("Denominator value must be non-zero")
except ValueError:
    print("Values must be integers")