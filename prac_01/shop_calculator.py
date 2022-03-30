""" a small program to calculate the total price for
a number of items each with different prices """
total = 0
number_of_item = int(input("Number of items: "))
while number_of_item < 0:
    print("Invalid number of items!")
    number_of_item = int(input("Number of items: "))
for n in range(number_of_item):
    price = float(input("Price of item: "))
    total += price
if total > 100:
    total *= 0.9
print(f"Total price for {number_of_item} items is ${total:.2f}")
print()



