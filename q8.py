import math

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_primes(limit):
    prime_sum = 0
    for num in range(2, limit):
        if is_prime(num):
            prime_sum += num
    return prime_sum

def fibonacci_sequence(limit):
    fib_sequence = [1, 2]  # Starting with 1 and 2
    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Set the limit for the Fibonacci sequence and primes
fib_limit = 2000000
prime_limit = 2000000

# Calculate the sum of all primes below two million
prime_sum = sum_of_primes(prime_limit)
print(f"Sum of all primes below two million: {prime_sum}")

# Generate Fibonacci sequence up to the limit
fib_sequence = fibonacci_sequence(fib_limit)
print(f"Fibonacci sequence up to {fib_limit}: {fib_sequence}")
