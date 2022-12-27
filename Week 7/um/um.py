import re


def main():
    print(count(input("Text: ")))


def count(s):
    # Match if "um" is in the beginning (^) or end ($) of a string input
    # Match if the character before and after "um" is not alphanumeric (punctuation / space is ok)
    regex = "(^|\W)um($|\W)"
    match = re.findall(regex, s, re.IGNORECASE)
    if match:
        return(len(match))


if __name__ == "__main__":
    main()