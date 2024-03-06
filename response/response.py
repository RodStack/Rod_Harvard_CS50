import validators


def main():
    email = input("What's your email address? ")
    print(check_email(email))

def check_email(mail):
    if validators.email(mail):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()