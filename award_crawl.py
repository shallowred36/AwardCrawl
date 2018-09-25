import requests
import argparse
from datetime import datetime
from bs4 import BeautifulSoup

def parse(destination, check_in, check_out):
    # Construct award search url


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Add command-line arguments
    parser.add_argument('destination', help='Enter destination')
    parser.add_argument('check_in', help='Enter check-in date(YYYY/MM/DD)')
    parser.add_argument('check_out', help='Enter check-out date(YYYY/MM/DD)')
    args = parser.parse_args()
    # Extract arguments
    destination = args.destination
    check_in = datetime.strptime(args.chec_in, "%Y/%m/%d")
    check_out = datetime.strptime(args.chec_out, "%Y/%m/%d")
    today = datetime.now()
    # Compare today's date with both check-in and check-out dates
    if today < check_in and check_in < check_out:
        print("Starting award night crawling...")
        parse(destination, check_in, check_out)
    elif today > check_in or today > check_out:
        print("Please enter future check-in and check-out dates")
    elif check_in > check_out:
        print("Please enter a check-out date later than the check-in date")
