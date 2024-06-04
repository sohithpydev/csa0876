# -*- coding: utf-8 -*-
"""max_consecutives

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qiSVRD1fuasel8Pd97kV8WGyCfHEGUxp

A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly. Given an integer n, return true if n is a perfect number, otherwise return false.

Test Case 1:

Input: num = 28

Output: true

Test Case 2:

Input: num = 7

Output: false
"""

def is_perfect_number(num):
    if num <= 1:
        return False

    divisor_sum = 1  # Start with 1 as every number is divisible by 1

    # Find divisors from 2 to sqrt(num)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisor_sum += i
            if i != num // i:  # Avoid counting the same divisor twice for perfect squares
                divisor_sum += num // i

    # Check if the sum of divisors equals the number
    return divisor_sum == num

# Test cases
print(is_perfect_number(28))  # Output: True
print(is_perfect_number(7))   # Output: False