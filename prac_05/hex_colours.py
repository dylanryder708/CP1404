COLOUR_CODES = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "black": "#000000", "blond": "#faf0be",
                "bone": "#e3dac9", "brass": "#b5a642", "camel": "#c19a6b", "emerald": "#50c878", "fawn": "#e5aa70"}

colour_name = input("Colour name: ").lower()
while colour_name != "":
    print(f"{colour_name}'s colour code is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Colour name: ").lower()
