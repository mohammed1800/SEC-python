import sys

# Check if the correct number of command-line arguments are provided
if len(sys.argv) != 3:
    print("Usage: python add.py <num1> <num2>")
    sys.exit(1)

# Extract the command-line arguments
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

# Calculate the sum
sum_result = num1 + num2

# Print the sum
print(f"The sum of {num1} and {num2} is {sum_result}")
