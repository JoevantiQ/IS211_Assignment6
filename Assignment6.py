import unittest
from assignement6 import *


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

    # Add similar test cases for other conversions...


if __name__ == '__main__':
    unittest.main()