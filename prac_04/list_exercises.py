# 1 Basic list operations
numbers = []
for n in range(5):
    number = int(input("Number :"))
    numbers.append(number)
print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of numbers is", sum(numbers) / len(numbers))


# 2 Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter user name : ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")


# 3 List comprehension
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",
              "Ada Lovelace"]

#  list of full_names in lowercase
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
#  list of integers
numbers = [int(almost_number) for almost_number in almost_numbers]
print(numbers)


#  list of only the numbers that are greater than 9 from the numbers above
greater_numbers = [number for number in numbers if number > 9]
print(greater_numbers)




