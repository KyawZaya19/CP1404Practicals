# odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=" ")
print()

# a. count in 10s from 0 to 100
for a in range(0, 101, 10):
    print(a, end=" ")
print()

# b. count down from 20 to 1
for b in range(20, 1, -1):
    print(b, end=" ")
print()

# c. Ask the user for a number, then print that many stars all on one line
number = int(input("Number of stars : "))
for n in range(number):
    print("*", end="")
print()
# d. print n lines of increasing stars
for n in range(1, number + 1):
    print("*" * n)
print()




