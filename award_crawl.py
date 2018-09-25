import requests
import argparse
from bs4 import BeautifulSoup

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Add command-line arguments
    parser.add_argument('destination', help='Enter destination')
    parser.add_argument('check_in', help='Enter check-in date(YYYY/MM/DD)')
    parser.add_argument('check_out', help='Enter check-out date(YYYY/MM/DD)')
    args = parser.parse_args()
    
