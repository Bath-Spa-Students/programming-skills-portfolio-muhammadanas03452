import math

def calculate_area(radius):
    return math.pi * radius ** 2
radius= float(input("Enter Radius of Circle: "))
area = calculate_area(radius)
print("Area of Circle with Radius: ",radius,"is:",area)