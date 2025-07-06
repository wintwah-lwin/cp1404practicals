from guitar import Guitar

guitars = []
print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.\n")
    name = input("Name: ")

print("\nThese are my guitars:")
max_guitar_length = max(len(guitar.name) for guitar in guitars)
for i in range(len(guitars)):
    guitar = guitars[i]
    vintage = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>{max_guitar_length}} ({guitar.year}), worth $ {guitar.cost:10,.2f} {vintage}")