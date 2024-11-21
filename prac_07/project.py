"""
Estimate: 2 hours
Start Time: 6:34 PM
Finish Time: 7:55 PM
"""
import datetime


class Project:
    """A class to represent a project."""

    def __init__(self, name, start_date, priority, estimate, completion):
        """Initialize a project with name, start date, priority, cost estimate, and completion percentage."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()  # Convert string to date
        self.priority = int(priority)
        self.estimate = float(estimate)
        self.completion = int(completion)

    def __str__(self):
        """Return a string representation of the project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.estimate:,.2f}, "
                f"completion: {self.completion}%")

    def __lt__(self, other):
        """Define less-than for sorting by priority."""
        return self.priority < other.priority

    def update(self, completion=None, priority=None):
        """Update completion and/or priority for the project."""
        if completion is not None:
            self.completion = completion
        if priority is not None:
            self.priority = priority

    def is_complete(self):
        """Check if the project is completed (completion 100%)."""
        return self.completion == 100
