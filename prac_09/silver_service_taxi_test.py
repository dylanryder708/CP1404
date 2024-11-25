"""
CP1404/CP5632 Practical
Silver Service Taxi class test
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def run_tests():
    """Test Silver Service Taxi class."""
    my_taxi = SilverServiceTaxi("Best Taxi", 100, 2)
    my_taxi.drive(18)
    print(my_taxi)
    assert my_taxi.get_fare() == 48.78
    print(my_taxi.get_fare())


run_tests()
