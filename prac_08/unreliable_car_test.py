"""
Unreliable car testing
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    reliable_car = UnreliableCar("Reliable car", 100, 100)
    unreliable_car = UnreliableCar("Unreliable car", 100, 10)

    for i in range(1, 10):
        print(f"---Attempt to drive {i} km---")
        print(f"{reliable_car.name:.17} drove {reliable_car.drive(i):2} km")
        print(f"{unreliable_car.name:.17} drove {unreliable_car.drive(i):2} km")
    print(reliable_car)
    print(unreliable_car)


main()
