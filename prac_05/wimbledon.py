"""
wimbledon.py
Estimate: 25 minutes
Time taken: 37 minutes
"""

FILENAME = "wimbledon.csv"

def main():
    data = read_data(FILENAME)
    champion_to_win = count_champion_wins(data)
    countries, count = get_countries_in_alphabetical_order(data)
    print(f"Wimbledon Champions:")
    for champion, wins in champion_to_win.items():
        print(f"{champion} {wins}")
    print()
    print(f"These {count} countries have won Wimbledon:\n{countries}")

def read_data(filename):
    """Read wimbledon.csv file and return a list of lists"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]
        data = [line.strip().split(",") for line in lines]
    return data

def count_champion_wins(data):
    """Count how manu times the champions have won and return a dictionary"""
    champion_to_win = {}
    for row in data:
        champion = row[2]
        if champion in champion_to_win:
            champion_to_win[champion] += 1
        else:
            champion_to_win[champion] = 1
    return champion_to_win

def get_countries_in_alphabetical_order(data):
    """get countries into a set, sort into alphabetical order and join them"""
    countries = {row[1] for row in data}
    sorted_countries = (", ".join(sorted(countries)))
    count_countries = len(countries)
    return sorted_countries, count_countries

main()