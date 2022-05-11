"""
 Test Taxi
"""

from prac_08.taxi import Taxi

taxi = Taxi("Prius", 100)
taxi.drive(40)
print(taxi)
print(f"Current fare: ${taxi.get_fare()}")

taxi.start_fare()
taxi.drive(100)
print(taxi)
print(f"Current fare: ${taxi.get_fare()}")
