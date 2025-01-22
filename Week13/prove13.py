def compute_windchills(temperature):
    
    windspeed = 5
    windspeeds = []
    while windspeed <= 60:
        windchill = 35.74 + 0.6215 * temperature - 35.75 * windspeed ** 0.16 + 0.4275 * temperature * windspeed ** 0.16
        windspeeds.append(round(windchill, 2))
        windspeed += 5
    return windspeeds

def convert_celsius_to_fahrenheit(celsius):
    return round(celsius * 9 / 5 + 32, 2)

if __name__ == '__main__':
    temperature = float(input("What is the temperature? "))
    scale = input("Fahrenheit or Celsius (F/C)? ").upper()

    if scale == 'C':
        temperature = convert_celsius_to_fahrenheit(temperature)
    
    windchills = compute_windchills(temperature)
    
    windspeed = 5
    for windchill in windchills:
        print(f"At temperature {temperature}F, and windspeed {windspeed} mph, the windchill is: {windchill}F")
        windspeed += 5
