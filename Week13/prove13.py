def compute_windchills(temperature, scale):
    if scale == 'S':
        temperature = convert_celsius_to_fahrenheit(temperature)
    windspeed = 5
    windspeeds = []
    while windspeed <= 60:
        windchill = 35.74 + 0.6215 * temperature - 35.75 * windspeed ** 0.16 + 0.4275 * temperature * windspeed ** 0.16
        windspeeds.append(round(windchill, 2))
        windspeed += 5
    return windspeeds

def convert_celsius_to_fahrenheit(celsius):
    return round(celsius * 9 / 5 + 32, 2)
