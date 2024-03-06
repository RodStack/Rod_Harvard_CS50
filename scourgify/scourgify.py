import sys
import csv

def main():
    if len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in (sys.argv[1] and sys.argv[2]):
        sys.exit("Not a csv file")
    else:
        get_name(sys.argv[1], sys.argv[2])

def get_name(arg1, arg2):
    try:
        fieldnames = ["first", "last", "house"]
        with open(arg1, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            with open(arg2, "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    last, first = row['name'].split(",")
                    writer.writerow({'first': first.lstrip(), "last": last, "house": row["house"]})

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
