import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if link := re.search(r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>", s):
        return f"https://youtu.be/{link.group(2)}"
    else:
        return None


if __name__ == "__main__":
    main()