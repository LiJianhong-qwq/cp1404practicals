"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    export_sentence(data)


def export_sentence(data):
    for name in data :
        print(f"{name[0]} is taught by {name[1]:<13} and has {name[2]:>5} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    name_list = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        name_list.append(parts)
    input_file.close()
    return name_list


main()
