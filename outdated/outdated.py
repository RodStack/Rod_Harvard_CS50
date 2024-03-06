
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    try:
        x, y, z = get_date("Date: ")
        print(f"{x}-{y:02d}-{z:02d}")
    except TypeError:
        x, y, z = get_date("Date: ")
def get_date(prompt):
    try:
        while True:
            date = input(prompt)
            if "/" in date:
                date = date.split("/")
                if int(date[0]) <= 12 and int(date[1]) <= 30:
                    holder = date.pop(0)
                    date.insert(1, holder)
                    date.reverse()
                    x, y, z = date
                    return int(x), int(y), int(z)
                else:
                    pass
            elif "," in date:
                date = date.replace(",", "")
                date = date.split()
                holder = date.pop(0)
                date.insert(1, holder)
                date.reverse()
                x, y, z = date
                if y in months and int(z) <= 30:
                    y = months.index(y) + 1
                    return int(x), int(y), int(z)
    except ValueError:
        pass
    except TypeError:
        pass
    except NameError:
        pass
if __name__ == "__main__":
    main()
