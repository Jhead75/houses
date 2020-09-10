from sys import argv, exit
import csv
from cs50 import SQL


def main():

    db = SQL("sqlite:///students.db")

    if len(argv) != 2:
        print("Usage: import.py [charachters.csv]")
        exit(1)

    #testhouse = argv[1]

    student = db.execute(f"SELECT first, middle, last, birth FROM students WHERE house == \"{argv[1]}\" ORDER BY last, first;")

    count = len(student)

    for i in student:
        if i["middle"] != None:
            print(i["first"], i["middle"], i["last"]+", born", i["birth"])
        else:
            print(i["first"], i["last"]+", born", i["birth"])


main()