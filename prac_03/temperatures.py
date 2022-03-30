""" Program for converting Celsius
to Fahrenheit and vice versa
"""


def main():
    celsius = float(input(" Celsius : "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(fahrenheit)


def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32.0


main()
