
def main():
    greet = input("Greeting: ")
    print(f"${value(greet)}")

def value(greeting):

    if "Hello" in greeting:
        return 0
    elif greeting[0] == "H":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()