"""Time estimate - 45 minutes
Time taken - 52 minutes"""

from project import Project
import datetime

FILENAME = "projects.txt"
MENU = """- (L)oad projects
    - (S)ave projects
    - (D)isplay projects
    - (F)ilter projects by date
    - (A)dd new project
    - (U)pdate project
    - (Q)uit"""

def main():
    """main function with menu options"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice. Please select a valid menu option.")
        print(MENU)
        choice = input(">>> ").lower()
    if choice == "q":
        choice_save = input(f"Would you like to save to {FILENAME}? ").lower()
        if choice_save in ["yes", "y"]:
            save_projects(FILENAME, projects)
        print("Thank you for using custom-built project management software.")

def load_projects(filename):
    """load projects from file"""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            name, start_date, priority, cost, percent = parts
            project = Project(name, start_date, priority, cost, percent)
            projects.append(project)
    return projects

def save_projects(filename, projects):
    """save projects to file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for p in projects:
            file.write(f"{p.name}\t{p.start_date.strftime('%d/%m/%Y')}\t{p.priority}\t{p.cost_estimate:.2f}\t{p.percent_complete}\n")

def display_projects(projects):
    """display projects sorted by priority"""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])

    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")

def filter_projects_by_date(projects):
    """filter projects by the date"""
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered = sorted([p for p in projects if p.start_date > filter_date], key=lambda x: x.start_date)
    for p in filtered:
        print(p)


def add_new_project(projects):
    """add new project to projects from user"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: $")
    percent = input("Percent complete: ")
    new_project = Project(name, start_date, priority, cost, percent)
    projects.append(new_project)

def update_project(projects):
    """update project completion and priority"""
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    try:
        index = int(input("Project choice: "))
        project = projects[index]
        print(project)
        new_percent = input("New Percentage: ")
        new_priority = input("New Priority: ")
        project.update(new_percent, new_priority)
    except (ValueError, IndexError):
        print("Invalid input.")

if __name__ == "__main__":
    main()
