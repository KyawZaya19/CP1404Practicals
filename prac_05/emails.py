"""
a program that stores users' emails and names in a dictionary
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        verification = input(f"Is your name {name}?(Y/n) ")
        if verification.upper() != "Y" and verification != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    first_word = email.split('@')[0]
    parts = first_word.split('.')
    name = " ".join(parts).title()
    return name


main()
