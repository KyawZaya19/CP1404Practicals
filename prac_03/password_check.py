"""
A simple program for password check
"""

MIN_LENGTH = 6
password = input("Type a password : ")
while len(password) < MIN_LENGTH:
    print("Your password is too short")
    password = input("Type a password : ")
for x in password:
    print("*", end="")