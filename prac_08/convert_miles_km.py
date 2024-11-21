"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KILOMETRES = 1.609


class MilesConversionApp(App):
    """
    Main Program - Kivy app for converting miles to kilometres.
    """

    def build(self):
        """
        Construct the Kivy app.
        :return: reference to root Kivy widgets
        """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def get_valid_miles(self):
        """
        Get inputted miles to and convert to float.
        :return: 0 if conversion produces an error, float version of input
        """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, change):
        """
        Handle up/down button press.
        :param change: the amount to change
        :return: None
        """
        value = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculation()

    def handle_calculation(self):
        """
        Handle calculation and output result to output label widget.
        :return: None
        """
        value = self.get_valid_miles()
        result = value * MILES_TO_KILOMETRES
        self.root.ids.output_label.text = str(result)


MilesConversionApp().run()
