"""
Unreliable car class
"""

import random
from prac_08.car import Car


class UnreliableCar(Car):
    """ Unreliable car version. """
    def __init__(self, name, fuel, reliability):
        """ Initialise UnreliableCar"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """ Drive the car, or not based on reliability. """
        random_number = random.randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven



