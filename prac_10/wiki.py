"""
CP1404/CP5632 Practical
Program that gets data from Wikipedia using their API
"""

import wikipedia


def main():
    """Get user input, then attempt to return data from that page on Wikipedia."""
    title = input("Enter page title: ")
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f"Page id {title} does not match any pages. Try another id!")
        title = input("Enter page title: ")
    print("Thank you.")


main()
