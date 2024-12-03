"""
CP1404/CP5632 Practical
Unreliable Car class test
"""

from prac_09.unreliable_car import UnreliableCar


def run_tests():
    """Test Unreliable Car class."""
    excellent_car = UnreliableCar("Excellent", 100, 95)
    terrible_car = UnreliableCar("Terrible", 100, 10)
    for i in range(1, 15):
        print(f"Trying to drive {i}km:")
        print(f"{excellent_car.name} drove {excellent_car.drive(i)}km")
        print(f"{terrible_car.name} drove {terrible_car.drive(i)}km")
    print(excellent_car)
    print(terrible_car)


run_tests()
