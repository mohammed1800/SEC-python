# Ask the user for a number
number = int(input("Enter a number to start the countdown: "))

# Validate that the input is a positive integer
if number <= 0:
    print("Please enter a positive integer.")
    exit()

# Initialize a countdown variable
countdown = number

# Countdown loop using a while loop
while countdown >= 0:
    print(countdown)
    countdown -= 1  # Decrease countdown by 1 in each iteration

print("Blast off!")  # Printed after the countdown reaches zero
