import math

# find the area and circumference of the circle
# formula for the circumference 2 * pi * r & area pi *r^2

radius = float(input("Enter radius: "))

circumrerence = 2 * math.pi * radius
area = math.pi * (radius ** 2)
print(f"The area of the circle is: {area}")
print(f"The circumference of the circle is: {circumrerence}")