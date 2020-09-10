from sys import argv, exit
import csv
from cs50 import SQL


def main():

    db = SQL("sqlite:///students.db")

    if len(argv) != 2:
        print("Usage: import.py [charachters.csv]")
        exit(1)

    # Open csv file
    with open(f"{argv[1]}", 'r') as characters:

        # Create DictReader
        reader = csv.DictReader(characters)

        # Iterate through rows of CSV
        for row in reader:

            name = row["name"].split()

            if len(name) == 3:
                first = name[0]
                mid = name[1]
                last = name[2]
            else:
                first = name[0]
                mid = None
                last = name[1]

            db.execute("INSERT INTO students (First, Middle, Last, House, Birth) VALUES(?, ?, ?, ?, ?)",
                       first, mid, last, row["house"], row["birth"])


main()