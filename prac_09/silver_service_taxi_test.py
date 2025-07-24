from silver_service_taxi import SilverServiceTaxi

fancy_taxi = SilverServiceTaxi("Fancy car", 300, 2)
fancy_taxi.start_fare()
fancy_taxi.drive(18)
assert fancy_taxi.get_fare() == 48.78
print(fancy_taxi)
print(f"The fare is ${fancy_taxi.get_fare():.2f}")