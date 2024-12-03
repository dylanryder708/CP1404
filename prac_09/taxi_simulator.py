"""
CP1404/CP5632 Practical
Taxi Simulator that utilises the Taxi and SilverServiceTaxi classes
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi Simulator program to select taxis, drive it and calculate the total bill."""
    taxis = [Taxi('Prius', 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    selected_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f'{i} - {taxi}')
            taxi_choice = int(input("Choose taxi: "))
            try:
                selected_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "d":
            if selected_taxi:
                selected_taxi.start_fare()
                distance = float(input("Drive how far? "))
                selected_taxi.drive(distance)
                trip_fare = selected_taxi.get_fare()
                print(f"Your {selected_taxi.name} trip cost you ${trip_fare:.2f}")
                total_bill += trip_fare
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f'{i} - {taxi}')


main()
