def main():
    total_fuel = input("Fraction: ")
    percentage = convert(total_fuel)
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x, y = int(x), int(y)
            if x <= y:
                total = round(x / y * 100)
                return total
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def gauge(percentage):
    if percentage > 98:
        return "F"
    elif percentage < 2:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()