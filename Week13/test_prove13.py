from prove13 import compute_windchill
from prove13 import convert_celsius_to_fahrenheit

class Test_Prove:
    def test_prove_fahrenheit(self):
        temperature = 8
        windspeed = 5

        expected_windchills = [-1.11, -6.02, -9.15, -11.50, -13.40, -15.00, -16.39, -17.62, -18.73, -19.74, -20.67, -21.53]
        for i in range(12):
            windchill = compute_windchill(temperature, windspeed)
            assert round(windchill, 2) == expected_windchills[i]
            windspeed += 5

    def test_prove_celsius(self):
        temperature = 14
        windspeed = 5

        expected_windchills = [5.93, 1.42, -1.47, -3.63, -5.38, -6.85, -8.13, -9.27, -10.29, -11.22, -12.07, -12.87]
        for i in range(12):
            windchill = compute_windchill(temperature, windspeed)
            assert round(windchill, 2) == expected_windchills[i]
            windspeed += 5

    def test_prove_celsius_to_fahrenheit(self):
        celsius = -10

        fahrenheit = convert_celsius_to_fahrenheit(celsius)

        assert fahrenheit == 14