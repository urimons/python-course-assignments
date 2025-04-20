import math
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <radius>")
    sys.exit(1)

try:
    radius = float(sys.argv[1])
except ValueError:
    print("Please provide a valid number for the radius.")
    sys.exit(1)

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Print the results
print(f"The area of your circle is: {area}, and the circumference is: {circumference}")
print("I really don't see the point of this exercise")
