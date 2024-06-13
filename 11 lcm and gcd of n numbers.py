from math import gcd

def gcd_of_list(numbers):
    result_gcd = numbers[0]
    for i in range(1, len(numbers)):
        result_gcd = gcd(result_gcd, numbers[i])
    return result_gcd

# Example usage:
numbers = [12, 18, 24]
result_gcd = gcd_of_list(numbers)
print(f"GCD of {numbers}: {result_gcd}")
