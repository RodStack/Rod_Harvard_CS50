from datetime import date
import inflect
import sys
import operator

p = inflect.engine()

def main():
    bdate = input("Date of Birth: ")
    try:
        days_diff = operator.sub(date.today(), date.fromisoformat(bdate))
        print(days_min_to_words(days_diff.days))
    except ValueError:
        sys.exit("Invalid date")

def days_min_to_words(days):
    mins =  days * 24 * 60
    words = p.number_to_words(mins, andword="")
    return f"{words.capitalize()} minutes"

if __name__ == "__main__":
    main()