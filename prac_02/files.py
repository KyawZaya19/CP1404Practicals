# 1
out_file = open("name.txt", "w")
name = input("Type your name: ")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Your name is {name}")

# 3
in_file = open("numbers.txt", "r")
first_number = in_file.readline()
second_number = in_file.readline()
in_file.close()
total = int(first_number) + int(second_number)
print(f"Result = {total}")

# 4
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(f"Total = {total}")




