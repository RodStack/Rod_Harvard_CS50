def main():
    word = input("camelCase: ")
    return get_camel_case(word)
    

def get_camel_case(word):
    result = ""
    for letter in word:
        if letter.isupper():
            result += "_" + letter.lower()
        else:
            result += letter
    print(result)
main()