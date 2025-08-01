from prac_09.car import Car
import random
class UnreliableCar(Car):
    """specialized version of car that includes reliability"""
    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but only drive if random number is less than car reliability."""
        if random.randint(0,101) < self.reliability:
            return super().drive(distance)
        return 0