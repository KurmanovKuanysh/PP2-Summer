#Calculate the Area of a Regular Polygon
def area_of_polygon(num_sides, side_length):
    # Formula: (num_sides * side_length^2) / (4 * tan(pi / num_sides))
    return (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))

# Input values
num_sides = 4
side_length = 25

area = area_of_polygon(num_sides, side_length)

print("Input number of sides:", num_sides)
print("Input the length of a side:", side_length)
print("The area of the polygon is:", area)
