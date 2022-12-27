def main():
    x = get_fraction("Fraction: ")
    print(x)


def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            if 0 <= int(x)/int(y) <= 0.1:
                return("E")
            elif 0.9 <= int(x)/int(y) <= 1:
                return("F")
            elif 0.1 < int(x)/int(y) < 0.9:
                return str(round(int(x)/int(y)*100)) + "%"
        except (ValueError, ZeroDivisionError):
            pass


main()