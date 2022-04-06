"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """ Read data and display """
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_details = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        subject_data = [parts[0], parts[1], int(parts[2])]
        subject_details.append(subject_data)

    input_file.close()
    return subject_details


def display_subject_details(subject_details):
    for subject_detail in subject_details:
        print(f"{subject_detail[0]} is taught by {subject_detail[1]:13} and has {subject_detail[2]:4} students")


main()
