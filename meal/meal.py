def main():
    time = input("What time it is: ")
    result = convert(time)
    if 7 <= result <= 8:
        print("breakfast time")
    elif 12 <= result <= 13:
        print("lunch time")
    elif 18 <= result <= 19:
        print("dinner time")
    else:
        return


def convert(time):
    hour, minute, term = time.split(":")
    minute = int(minute) / 60
    hour = int(hour) + minute
    return hour

if __name__ == "__main__":
    main()

