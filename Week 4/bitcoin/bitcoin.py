import sys
import requests


def main():
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
            print(btc_price(n))
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")


def btc_price(num):
    try:
        response = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json")
        result = response.json()
        price = result["bpi"]["USD"]["rate_float"]
        total = price * num
        return f"${total:,.4f}"
    except requests.RequestException:
        return None


main()