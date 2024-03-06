
vowels = ["a", "e", "i", "o", "u", "A", "E", "I","O","U"]

def main():
    tweet = input("Input: ")
    result = shorten(tweet)
    print(result)

def shorten(word):
    new_word = ""
    for letter in word:
        if letter in vowels:
            new_word += ""
        else:
            new_word += letter

    return new_word


if __name__ == "__main__":
    main()