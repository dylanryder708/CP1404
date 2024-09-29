def main():
    conversion_choice = input("Convert C to F(C)\nF to C(F)\nQuit(Q)\nConversion: ").upper()
    while conversion_choice != "Q":
        if conversion_choice == "C":
            celsius = int(input("Degrees Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} degrees celsius is {fahrenheit:.2f} degrees fahrenheit")
        elif conversion_choice == "F":
            fahrenheit = (int(input("Degrees Fahrenheit: ")))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} degrees fahrenheit is {celsius:.2f} degrees celsius")
        else:
            print("Invalid choice")
        conversion_choice = input("Convert C to F(C)\nF to C(F)\nQuit(Q)\nConversion: ").upper()
    print("Goodbye")


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9 / 5)) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


main()
