try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero.")
else:
    print("Division successful. The result is:", result)
finally:
    print("Execution of try..except block is complete.")
