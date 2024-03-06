def main():
    total = get_fuel("Fraction: ")
    if total > 98:
        print("F")
    elif total < 2:
        print("E")
    else:
        print(f"{total}%")

def get_fuel(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            x, y = int(x), int(y)
            if x <= y:
                total = round(x / y * 100)
                return total
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
