# Kainoa Bal
# 09/14/2026
# P2LAB1
# Calculations for a circle

# Import the value for pi
from math import pi
print(pi)

# Get radius from user

radius = input("Enter the radius: ")

# Convert radius to a float
radius = float(radius)

print()
# Show the data type of the radius
print(type(radius))

# Calculate the diameter
diameter =  2 * radius

# Display diameter
print(diameter)

# Display diameter using f-string
print(f"The diameter of the circle is {diameter:.1f}")
print()

# Display the circumference of the circle.
circumference = 2 * pi * radius
print(f"The circumference of the circle is {circumference:.2f}")
(print)

# Display the area of the circle.
area = pi * radius**2
print(f"The area of the circle is {area:.3f}")