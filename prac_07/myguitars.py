from guitar import Guitar
import csv
FILENAME = "guitars.csv"

def main():
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)

    guitars.sort()

    print("\nSorting guitars:")
    display_guitars(guitars)

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

main()
