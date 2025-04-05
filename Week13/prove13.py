def compute_windchill(temperature, windspeed):
        return 35.74 + 0.6215 * temperature - 35.75 * windspeed ** 0.16 + 0.4275 * temperature * windspeed ** 0.16

def convert_celsius_to_fahrenheit(celsius):
    return round(celsius * 9 / 5 + 32, 2)

if __name__ == '__main__':
    temperature = float(input("What is the temperature? "))
    scale = input("Fahrenheit or Celsius (F/C)? ").upper()

    if scale == 'C':
        temperature = convert_celsius_to_fahrenheit(temperature)
    
    windspeed = 5
    while windspeed <= 60:
        windchill = compute_windchill(temperature, windspeed)
        print(f"At temperature {temperature}F, and windspeed {windspeed} mph, the windchill is: {windchill:.2f}F")
        windspeed += 5
