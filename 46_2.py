def divide(a, b):
    try:
        result = a / b
    except:
        print("An error occurred!")
        result = None
    return result

print(divide(10, 0))  # Output: An error occurred! \n None
print(divide(10, 'a'))  # Output: An error occurred! \n None
