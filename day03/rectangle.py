import math
import sys

height = float(sys.argv[1])
width = float(sys.argv[2])

area = height * width
perimeter = 2 * (width + height)

print(f"The area of your rectangle is: {area}, and the perimeter is: {perimeter}")

