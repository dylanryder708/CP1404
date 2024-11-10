import csv
from guitar import Guitar


def main():
    # Read guitars from the CSV file
    filename = 'guitars.csv'
    guitars = read_guitars_from_file(filename)

    # Display the unsorted guitars
    print("Unsorted Guitars:")
    display_guitars(guitars)

    new_guitar = add_new_guitar()
    guitars.append(new_guitar)

    # Sort the guitars by year (oldest to newest)
    guitars.sort()

    # Display the sorted guitars
    print("\nSorted Guitars (by year):")
    display_guitars(guitars)

    write_guitars_to_file(filename, guitars)


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


def add_new_guitar():
    """Prompt the user to enter details for a new guitar and return a new Guitar object."""
    print("\nEnter details for a new guitar:")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    return Guitar(name, year, cost)


def write_guitars_to_file(filename, guitars):
    """Write the list of guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == "__main__":
    main()
