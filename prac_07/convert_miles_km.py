"""
GUI program for converting miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_MILES_TO_KM = 1.60934


class MilesConverter(App):
    """Kivy App for converting miles to kilometres"""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculation"""
        miles = self.convert_to_float(text)
        self.result(miles)

    def handle_increment(self, text, change):
        """Handle up and down button press, update the new value"""
        miles = self.convert_to_float(text) + change
        self.root.ids.input_miles.text = str(miles)

    def result(self, miles):
        """Calculating result and change it into string"""
        self.output_km = str(miles * FACTOR_MILES_TO_KM)

    @staticmethod
    def convert_to_float(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverter().run()
