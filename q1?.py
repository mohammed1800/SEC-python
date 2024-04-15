numbers = [1, 2, 3, 4, 5]

# Incorrect indentation
try:
  for number in numbers:
    print(number)  # Incorrect indentation

except IndentationError:
  print("An IndentationError has occurred!")

# Corrected indentation
try:
  for number in numbers:
    print(number)  # Correct indentation
except IndentationError:
  pass  # This line won't be reached because the indentation is correct

