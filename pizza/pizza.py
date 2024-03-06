from tabulate import tabulate
import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a python file")
    else:
        print(display_menu(sys.argv[1]))

def display_menu(cart): 
    try:
        menu = []
        with open(cart, "r") as file:
            for line in file:
                row = line.rstrip().split(",")
                menu.append(row)
            header = menu[0]
            menu.pop(0)
            return tabulate(menu, header, tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()






