#Convert Degree to Radian
import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

# Input degree
degree = 15
radian = degree_to_radian(degree)

print("Input degree:", degree)
print("Output radian:", radian)
