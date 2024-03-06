
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        mins_start = 0
        mins_end = 0
        if time := re.search(r"^(1[0-2]|[1-9]):?([0-5]?[0-9]?)? ([AP][M]+) to (1[0-2]|[1-9]):?([0-5]?[0-9]?)? ([AP][M]+)$", s):
            hour_start = int(time.group(1))
            hour_end = int(time.group(4))
            if time.group(2).isdigit():
                mins_start = int(time.group(2))
                mins_end = int(time.group(5))
                zone_start = time.group(3)
                zone_end = time.group(6)
            else:
                zone_start = time.group(3)
                zone_end = time.group(6)

        if zone_start == "AM":
            if hour_start == 12:
                hour_start = 0
            start = f"{hour_start:02d}:{mins_start:02d}"
        elif zone_start == "PM":
            hour_start += 12
            if hour_start == 24:
                hour_start = 12
            start = f"{hour_start:02d}:{mins_start:02d}"
        if zone_end == "AM":
            if hour_end == 12:
                hour_end = 0
            end = f"{hour_end:02d}:{mins_end:02d}"
        elif zone_end == "PM":
            hour_end += 12
            if hour_end == 24:
                hour_end = 12
            end = f"{hour_end:02d}:{mins_end:02d}"

        return f"{start} to {end}"
    except:
        sys.exit("ValueError")

if __name__ == "__main__":
    main()