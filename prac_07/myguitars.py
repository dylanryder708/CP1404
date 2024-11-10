import csv
from guitar import Guitar


def main():
    # Read guitars from the CSV file
    filename = 'guitars.csv'
    guitars = read_guitars_from_file(filename)

    # Display the unsorted guitars
    print("Unsorted Guitars:")
    display_guitars(guitars)

    # Sort the guitars by year (oldest to newest)
    guitars.sort()

    # Display the sorted guitars
    print("\nSorted Guitars (by year):")
    display_guitars(guitars)


def read_guitars_from_file(filename):
    """Reads guitar data from a CSV file and returns a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            # Create a new Guitar object and append it to the list
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display the guitars in a list."""
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
