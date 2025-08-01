from unreliable_car import UnreliableCar

unreliable_car = UnreliableCar("Test car", 100, 30)
results = []
for i in range(0,100):
    results.append(unreliable_car.drive(1)) #car drives 1 km each time
print(f"{unreliable_car.name} drove {sum(results)} km out of 100 attempts")