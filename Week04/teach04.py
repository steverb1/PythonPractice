import math


def calculate_velocity(m, g, t, p, A, C):
    c = .5 * p * A * C
    velocity = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))

    return c, velocity

if __name__ == '__main__':
    print('Welcome to the velocity calculator. Please enter the following:')
    print()
    m = float(input('Mass (in kg): '))
    g = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
    t = int(input('Time (in seconds): '))
    p = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
    A = float(input('Cross sectional area (in m^2): '))
    C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

    c, velocity = calculate_velocity(m, g, t, p, A, C)
    print(f'The inner value of c is: {c:.3f}')
    print(f'The velocity after {t} seconds is: {velocity:.3f} m/s')
