"""
A simple program for password check
"""

MIN_LENGTH = 6


def main():
    password = get_password()
    display_asterisks(password)


def get_password():
    """ Get password and verify minimum length """
    password = input("Type a password : ")
    while len(password) < MIN_LENGTH:
        print("Your password is too short")
        password = input("Type a password : ")
    return password


def display_asterisks(password):
    """ Display asterisks for password """
    for x in password:
        print("*", end="")


main()
