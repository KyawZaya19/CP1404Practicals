""" Program for converting Celsius
to Fahrenheit and vice versa
"""


def main():
    celsius = float(input(" Celsius : "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("Fahrenheit:", fahrenheit)


def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32.0


main()


def main():
    fahrenheit = float(input(" Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print("Celsius:", celsius)


def fahrenheit_to_celsius(fahrenheit):
    return fahrenheit - 32 * 5/9


main()
