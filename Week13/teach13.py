import math


def compute_area_square(side):
    return side * side

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * radius * radius

shape = ''
while shape != 'quit':
    shape = input("Enter the shape you have: ").lower()

    if shape == 'square':
        side = float(input("Enter the side of the square: "))
        square_area = compute_area_square(side)
        print("The area of the square is", square_area)
    elif shape == 'rectangle':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        rectangle_area = compute_area_rectangle(length, width)
        print("The area of the rectangle is", rectangle_area)
    elif shape == 'circle':
        radius = float(input("Enter the radius of the circle: "))
        circle_area = compute_area_circle(radius)
        print("The area of the circle is", circle_area)
