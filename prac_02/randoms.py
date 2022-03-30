import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# line 1 : smallest = 5 , largest = 19
# line 2 : smallest = 3 , largest = 9 It cannot produce 4
# line 3 : smallest = 2.5 , largest = 5.499999999

print(random.randint(1, 101))