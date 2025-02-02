"""

Bitcoin is a form of digital currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network,
otherwise known as a blockchain, to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins,
, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object,
among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:

"""
import json
import sys
import requests
def main():
    print(f"${bitcoin_converter():,.4f}")

def bitcoin_converter():
    try:
        money_in_bitcoin = float(sys.argv[1])
        if money_in_bitcoin == False or len(sys.argv) != 2:
            sys.exit()
        money_in_dollars = money_in_bitcoin * bitcoin_prize()
        return money_in_dollars
    except ValueError:
        return "Command-line argument is not a number"
    except IndexError:
        return "Missing command-line argument"
def bitcoin_prize():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        bc_in_float = data["bpi"]["USD"]["rate_float"]
        return float(bc_in_float)
    except requests.RequestException:
        pass

if __name__ == "__main__":
    main()
