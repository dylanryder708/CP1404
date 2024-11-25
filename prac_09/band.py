"""
CP1404/CP5632 Practical
Band class
"""


class Band:
    """Represent a Band."""

    def __init__(self, name):
        """Initialise a Band instance."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the musicians list."""
        self.musicians.append(musician)

    def play(self):
        """Return a string representation of what a musician is playing."""
        return "\n".join([musician.play() for musician in self.musicians])
