def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is even and print the result
if is_even(num):
    print(f"{num} is an even number.")
else:
    print(f"{num} is not an even number.")
