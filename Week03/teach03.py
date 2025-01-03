import math


# square_side = float(input('What is length of a side of the square? '))
# print(f'The area of the square is: {square_side ** 2}')

# rectangle_length = float(input('What is the length of the rectangle? '))
# rectangle_width = float(input('What is the width of the rectangle? '))
# print(f'The area of the rectangle is: {rectangle_length * rectangle_width}')

# radius = float(input('What is the radius of the circle? '))
# print(f'The area of the circle is: {math.pi * radius ** 2}')

# length = float(input('What is the common length? '))
# print(f'The area of a square is: {length ** 2}')
# print(f'The area of a circle is: {math.pi * length ** 2}')
# print(f'The volune of a cube is: {length ** 3}')
# print(f'The volume of a sphere is: {4 / 3 * math.pi * length ** 3}')

square_side = float(input('What is length of a side of the square (cm)? '))
print(f'The area of the square is: {square_side ** 2} cm^2')
print(f'The area of the square is: {square_side ** 2 / 10000} m^2')

rectangle_length = float(input('What is the length of the rectangle (cm)? '))
rectangle_width = float(input('What is the width of the rectangle (cm)? '))
print(f'The area of the rectangle is: {rectangle_length * rectangle_width} cm^2')
print(f'The area of the rectangle is: {rectangle_length * rectangle_width / 10000} m^2')

radius = float(input('What is the radius of the circle (cm)? '))
print(f'The area of the circle is: {math.pi * radius ** 2} cm^2')
print(f'The area of the circle is: {math.pi * radius ** 2 / 10000} m^2')
