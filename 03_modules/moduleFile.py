
# module => python file which we can import in other file and use
pi = 3.14
triangles = ["Acute Triangle", "Right Angle Triangle", "Obtuse Triangle"]

def find_cube_volume(side):
    return side * side * side

def find_cuboid_volume(lenght, height, width):
    return lenght * width * height

def find_cylinder_volume(radius, height):
    return ( 3.14 * radius * radius * height)
