MENU = "(G)et Valid Score\n(P)rint Result\n(S)how Stars\n(Q)uit"


def main():
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter score: "))
            get_valid_score(score)
        elif choice == "P":
            print(get_score(score))
        elif choice == "S":
            for i in range(1, score + 1):
                print("*", end="")
            print()
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Choice: ").upper()
    print("Goodbye.")


def get_valid_score(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))


def get_score(score):
    if score >= 90:
        return "Excellent."
    elif score >= 50:
        return "Pass."
    else:
        return "Bad."


main()
