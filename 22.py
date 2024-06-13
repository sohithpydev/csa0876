def reverse_integer(x: int) -> int:
    # Constants for 32-bit integer range
    INT_MIN = -2 ** 31
    INT_MAX = 2 ** 31 - 1

    # Check if x is negative
    is_negative = x < 0
    # Take the absolute value of x
    abs_x = abs(x)

    # Reverse the digits of abs_x
    reversed_x = int(str(abs_x)[::-1])

    # If x was negative, make the reversed_x negative
    if is_negative:
        reversed_x *= -1

    # Check if reversed_x is within the range of a 32-bit signed integer
    if INT_MIN <= reversed_x <= INT_MAX:
        return reversed_x
    else:
        return 0


# Example usage:
x = 123
print(reverse_integer(x))  # Output: 321

x = -123
print(reverse_integer(x))  # Output: -321

x = 120
print(reverse_integer(x))  # Output: 21
