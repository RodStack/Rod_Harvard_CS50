
import random

def main():
    show = get_guess("Level: ")
    print(show)

def get_guess(prompt):

    try:
        lvl = int(input(prompt))
    except ValueError:
        lvl = int(input(prompt))
        
    if lvl == 0:
        get_guess("Level: ")
    target = random.randint(1, lvl)

    while True:
        try:
            user_guess = int(input("Guess: "))
            if user_guess > lvl:
                break
            elif user_guess == target:
                return "Just right!"
            elif user_guess > target:
                print("Too large!")
            else:
                print("Too small!")
        except ValueError:
            pass

if __name__ == "__main__":
    main()