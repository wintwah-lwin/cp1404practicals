"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_data(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_data = []
    input_file = open(FILENAME)
    for line in input_file:
        parts = line.strip().split(',')
        parts[2] = int(parts[2])
        subject_data.append(parts)
    input_file.close()
    return subject_data

def display_subject_data(data):
    """Display subject details as readable lines"""
    for subject, lecturer, students in data:
        print(f"{subject} is taught by {lecturer:12} and has {students:3} students")
main()