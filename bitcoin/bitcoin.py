import requests
import sys


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
res = response['bpi']['USD']['rate_float']
num_res = float(res)

try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2:
        total = num_res * float(sys.argv[1])
        print(f"${total:,.4f}")



except requests.RequestException:
    sys.exit("Command-line argument is not a number")
except ValueError:
    sys.exit("Command-line argument is not a number")
