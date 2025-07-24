from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """object inherits from class Taxi which inherits from Car"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness
        self.fanciness = fanciness

    def get_fare(self):
        """calculate base fare and add flagfall"""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """returns a string of the base information plus flagfall"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"