"""
CP1404/CP5632 Practical
Unreliable Car class derived from the Car class
"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Represent an unreliable Car object."""

    def __init__(self, name, fuel, reliability):
        """
        Initialise an unreliable Car instance.

        reliability: float, references the percentage chance that the car will actually drive
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Drive the car based on the reliability.

        random_number: int, references a randomly selected integer from 1 to 100
        distance_driven: int, references how far the car has driven
        """
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
