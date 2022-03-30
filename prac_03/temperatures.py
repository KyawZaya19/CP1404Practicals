""" Programs for converting Celsius
to Fahrenheit and vice versa
"""


def main():
    """ Get celsius and display fahrenheit """
    celsius = float(input(" Celsius : "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("Fahrenheit:", fahrenheit)


def celsius_to_fahrenheit(celsius):
    """ Convert celsius to fahrenheit """
    return celsius * 1.8 + 32.0


main()


def main():
    """ Get fahrenheit and display celsius """
    fahrenheit = float(input(" Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print("Celsius:", celsius)


def fahrenheit_to_celsius(fahrenheit):
    """ Convert fahrenheit to celsius """
    return fahrenheit - 32 * 5/9


main()
