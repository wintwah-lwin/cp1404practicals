from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    """convert miles to km"""
    def build(self):
        """app from file"""
        self.title = "Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """get miles and calculate to km"""
        mile = self.get_validated_miles()
        km = mile * MILES_TO_KM
        self.root.ids.output_label.text = str(km)

    def handle_increment(self, change):
        """up down increment"""
        mile = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(mile)
        self.handle_calculate()

    def get_validated_miles(self):
        """get mile"""
        try:
            mile = float(self.root.ids.input_miles.text)
            return mile
        except ValueError:
            return 0


MilesConverterApp().run()
