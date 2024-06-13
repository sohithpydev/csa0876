def main():
    
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    quotient_result = num1 // num2  # Integer division
    remainder_result = num1 % num2

    
    print("Sum:", sum_result)
    print("Difference:", difference_result)
    print("Product:", product_result)
    print("Quotient:", quotient_result)
    print("Remainder:", remainder_result)

if __name__=="__main__":
 main()
