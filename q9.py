def fibonacci_sequence(limit):
    fib_sequence = [1, 2]  # Starting with 1 and 2
    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def sum_even_fibonacci(limit):
    fib_sequence = fibonacci_sequence(limit)
    even_sum = sum(num for num in fib_sequence if num % 2 == 0)
    return even_sum

# Set the limit for the Fibonacci sequence
fib_limit = 4000000

# Calculate the sum of even-valued terms in the Fibonacci sequence below four million
even_sum = sum_even_fibonacci(fib_limit)
print(f"Sum of even-valued terms in Fibonacci sequence below {fib_limit}: {even_sum}")
