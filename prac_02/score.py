import random


def main():
    score = int(input("Enter score: "))
    print(get_score(score))
    score = random.randint(1, 100)
    print(f"Random Score: {score}")
    print(get_score(score))


def get_score(score):
    while score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent."
    elif score >= 50:
        return "Pass."
    else:
        return "Bad."


main()
