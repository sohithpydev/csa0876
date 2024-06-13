try:
    ip1 = int(input("Enter input 1: "))
    ip2 = int(input("Enter input 2: "))
    result = ip1 / ip2
    print (result)
except ZeroDivisionError:
    print("Divisor is zero")
except ValueError:
    print("Please provide an integer!")
else:
    print("Check your input!")