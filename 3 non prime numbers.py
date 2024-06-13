def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_non_prime_numbers(start, end):
    non_prime_numbers = [num for num in range(start, end+1) if not is_prime(num)]
    print(f"Non-prime numbers between {start} and {end}: {non_prime_numbers}")

# Input: Replace 10 and 50 with your desired range (A and B)
A = 10
B = 50

print_non_prime_numbers(A, B)
