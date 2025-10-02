#Circumference of a circle 2 pi r
import math
r = float(input("What is circle's radius? "))
circumference = math.pi * 2 * r
print(f"The circumference of the circle is {circumference}cm²")

#Area of a circle pi r²
area = math.pi * math.pow(r,2)
print(f"The area is {area}cm²")

#Hypotenuse of a triangle a² + b² = c²
a = float(input("What is side a? "))
b = float(input("What is side b? "))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"The length of hypotenuse is {c}cm²")