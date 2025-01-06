import math


def calculate_velocity(m, g, t, p, A, C):
    c = .5 * p * A * C
    velocity = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))

    return f'{c:.3f}', f'{velocity:.3f}'
