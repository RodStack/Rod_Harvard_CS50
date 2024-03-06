
import random


def main():
    level = get_level()
    score = 0
    rounds = 1
    while rounds <= 10:
        try:
            tries = 0
            x, y = generate_integer(level)
            resp = int(input(f"{x} + {y} = "))
            if resp != (x + y):
                while tries < 3:
                    print("EEE")
                    tries += 1
                    resp = int(input(f"{x} + {y} = "))
                    if resp == (x + y):
                        score += 1
                        pass
                    else:
                        tries += 1
                print("EEE")
                print(f"{x} + {y} = {x+y}")
            else:
                score += 1
            rounds += 1
        except:
            print("EEE")
            rounds += 1
            pass

    print(f"score: {score}")

def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl in [1, 2, 3]:
                return lvl
        except:
            pass



def generate_integer(level):

    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y



if __name__ == "__main__":
    main()