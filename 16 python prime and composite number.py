def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Get user input
numbers = input("Enter a list of numbers separated by spaces: ").split()

# Initialize counters
prime_count = 0
composite_count = 0

# Count prime and composite numbers
for num in numbers:
    num = int(num)
    if is_prime(num):
        prime_count += 1
    else:
        composite_count += 1

# Display the result
print("Number of prime numbers:", prime_count)
print("Number of composite numbers:", composite_count)
