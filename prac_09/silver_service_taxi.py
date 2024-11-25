"""
CP1404/CP5632 Practical
Silver Service Taxi class derived from the Taxi class
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a Silver Service Taxi object."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a Silver Service Taxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the current fare."""
        return self.flagfall + super().get_fare()
