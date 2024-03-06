def main():
    plate = input("Plate: ")
    if count_num(plate):
        if is_valid(plate):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")

def count_num(s):
    check = []
    for char in s:
        if char.isdigit():
            check += char
    if len(check) > 0 and check[0] == "0":
        return False
    else:
        return True


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            if len(s) > 2:
                for i, l in enumerate(s):
                    if l.isdigit() or l.isalpha():
                        if l.isdigit():
                            for c in s[i:]:
                                if c.isalpha():
                                    return False
                    else:
                        return False
            return True
    else:
        return False


main()