import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if username := re.search(r'^<iframe src="(?:https?://)?(?:www\.)?youtube\.com/embed/([a-z0-9]+)"></iframe>$', s, re.IGNORECASE):
        embed = username.group(1)
        return f"https://youtu.be/{embed}"
    else:
        return None



if __name__ == "__main__":
    main()