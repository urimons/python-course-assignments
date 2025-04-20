import math

print("Hello, I'm Uri's code")
print("I understood you need to calculate a circle area and circumeference")
radius = float(input("What is the radius of the circle you want to calculate?"))
area = math.pi * radius ** 2
circumeference = 2 * math.pi * radius
print(f"The area of your circle is:{area}, and the circumeference is {circumeference}")
