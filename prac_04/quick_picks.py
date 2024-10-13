import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("Number of quick picks? "))
    while number_of_quick_picks < 0:
        print("You need at least one quick pick!")
        number_of_quick_picks = int(input("Number of quick picks? "))

    for i in range(1, number_of_quick_picks + 1):
        quick_picks = []
        for j in range(1, NUMBERS_PER_LINE + 1):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_picks:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join(f"{number:2}" for number in quick_picks))


main()
