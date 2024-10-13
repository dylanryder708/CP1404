"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_subject_data()
    print_subjects(subjects)


def load_subject_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject.append(parts)
    input_file.close()
    return subject


def print_subjects(subjects):
    """Print subject data in clean format."""
    for subject in subjects:
        print(f"{subject[0]}s lecturer is {subject[1]:12} and the subject currently has {subject[2]:3} students")


main()
