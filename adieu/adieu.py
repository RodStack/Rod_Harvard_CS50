import inflect


p = inflect.engine()


def main():
    result = get_goodbye()
    new_result = f"Adieu, adieu, to {p.join(result)}"
    print(new_result)

def get_goodbye():
    name_list = []
    try:
        while True:
            name = input("Name: ").strip()
            name_list.append(name)

    except EOFError:
        return name_list

if __name__ == "__main__":
    main()
