
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
    total = get_price("Item: ")
    print(f"Total: ${total:.2f}")

def get_price(prompt):
    total = 0
    while True:
        try:
            product = input(prompt).title()
            price = menu[product]
            total += price
            print(f"Total: ${total:.2f}")
        except NameError:
            pass
        except ValueError:
            pass
        except KeyError:
            pass
        except EOFError:
            return total
main()