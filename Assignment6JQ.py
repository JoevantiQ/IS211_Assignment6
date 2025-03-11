#conversion.py

def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = celsius + 273.15
    return kelvins


def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def convertFahrenheitToCelsius(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def convertFahrenheitToKelvin(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Kelvins"""
    kelvins = (fahrenheit - 32) * 5/9 + 273.15
    return kelvins


def convertKelvinToCelsius(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Celsius"""
    celsius = kelvin - 273.15
    return celsius


def convertKelvinToFahrenheit(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

import unittest
from assignement6 import *

#Test.py

class TestConversions(unittest.TestCase):
    def test_convertCelsiusToKelvin(self):
        self.assertAlmostEqual(convertCelsiusToKelvin(0), 273.15)
        self.assertAlmostEqual(convertCelsiusToKelvin(100), 373.15)
        self.assertAlmostEqual(convertCelsiusToKelvin(-273.15), 0)
        self.assertAlmostEqual(convertCelsiusToKelvin(300), 573.15)
        self.assertAlmostEqual(convertCelsiusToKelvin(37), 310.15)

    def test_convertCelsiusToFahrenheit(self):
        self.assertAlmostEqual(convertCelsiusToFahrenheit(0), 32)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(100), 212)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(-40), -40)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(37), 98.6)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(300), 572)

if __name__ == '__main__':
    unittest.main()

#conversion.py

    def convert(fromUnit, toUnit, value):
        """Converts between supported units. Raises ConversionNotPossible if conversion is invalid."""
        conversions = {
            "Celsius": {"Kelvin": lambda c: c + 273.15, "Fahrenheit": lambda c: (c * 9 / 5) + 32},
            "Kelvin": {"Celsius": lambda k: k - 273.15, "Fahrenheit": lambda k: (k - 273.15) * 9 / 5 + 32},
            "Fahrenheit": {"Celsius": lambda f: (f - 32) * 5 / 9, "Kelvin": lambda f: (f - 32) * 5 / 9 + 273.15},
            "Miles": {"Yards": lambda m: m * 1760, "Meters": lambda m: m * 1609.34},
            "Yards": {"Miles": lambda y: y / 1760, "Meters": lambda y: y * 0.9144},
            "Meters": {"Miles": lambda me: me / 1609.34, "Yards": lambda me: me / 0.9144}
        }

        if fromUnit == toUnit:
            return value

        try:
            return conversions[fromUnit][toUnit](value)
        except KeyError:
            raise ConversionNotPossible(f"Cannot convert {fromUnit} to {toUnit}")