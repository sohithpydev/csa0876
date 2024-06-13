def main():
    
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))


    bitwise_and = num1 & num2
    bitwise_or = num1 | num2
    bitwise_xor = num1 ^ num2
    left_shift = num1 << num2
    right_shift = num1 >> num2


    print("Bitwise AND:", bin(bitwise_and))
    print("Bitwise OR:", bin(bitwise_or))
    print("Bitwise XOR:", bin(bitwise_xor))
    print("Left Shift:", bin(left_shift))
    print("Right Shift:", bin(right_shift))

if __name__ == "__main__":
    main()
