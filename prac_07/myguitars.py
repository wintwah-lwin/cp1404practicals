from guitar import Guitar
import csv
FILENAME = "guitars.csv"

def main():
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)
    guitars += get_new_guitars()
    guitars.sort()
    print("\nSorting guitars:")
    display_guitars(guitars)
    save_guitars(FILENAME, guitars)

def load_guitars(filename):
    """read guitar csv and return a list of Guitar objects"""
    guitars = []
    with open(filename, 'r') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name, year, cost = row[0], int(row[1]), float(row[2])
            guitars.append(Guitar(name, year, cost))
        return guitars

def display_guitars(guitars):
    """display list of Guitar objects"""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

def get_new_guitars():
    "get new guitar from user"
    guitars = []
    print("\nEnter your guitar:")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")
    return guitars

def save_guitars(filename, guitars):
    with open(filename, 'w', newline="") as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

if __name__ == "__main__":
    main()
