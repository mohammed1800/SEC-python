import math

# Function to calculate distance using Pythagorean Theorem
def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Input coordinates from the user
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

# Calculate and print the distance
distance = calculate_distance(x1, y1, x2, y2)
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f} units.")
