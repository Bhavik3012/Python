import math


def circle_stats(radius):
    area = math.pi * (radius**2)
    circumference = 2 * math.pi * radius
    return area, circumference


radius = 1
print("Area: ", circle_stats(radius)[0])
print("Circumference: ", circle_stats(radius)[1])

print("Area and Circumference: ", circle_stats(radius))

a, c = circle_stats(radius)
print("Area: ", a)
print("Circumference: ", c)
