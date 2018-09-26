import requests
import argparse
from datetime import datetime
from bs4 import BeautifulSoup

def parse(destination, check_in, check_out):
    # Use autocomplete search to look for possible destinations
    """
    TODO: find a way to retrieve session ID; from cookie?
    auto_comp_query_para = [
            'https://www.marriott.com/aries-search/v2/autoComplete.comp?',
            'searchTerm={0}&'.format(destination),
            'suggestionSortOrder=city%2Cproperty%2Cairport%2Cpoi%2Cstate%2Ccountry&',
            'latitude=0&',
            'longtitude=0']
    auto_comp_url = ''.join(auto_comp_query_para)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}
    auto_comp_response = requests.get(auto_comp_url, headers = headers).json()
    print(auto_comp_url)
    print(auto_comp_response)
    """
    day_of_week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    month_of_year = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
    hotel_search_query_para = [
            'https://www.marriott.com/search/submitSearch.mi?',
            'recordsPerPage=20&',
            'destinationAddress.types=&', #country%2Cpolitical
            'isInternalSearch=true&',
            'vsInitialRequest=false&',
            'searchType=InCity&',
            'searchRadius=&',
            'singleSearchAutoSuggest=Unmatched&',
            'destinationAddress.placeId=&',
            'is-hotelsnearme-clicked=false&',
            'for-hotels-nearme=Near&',
            'pageType=editsearch&',
            'destinationAddress.country=&',
            'destinationAddress.address={0}&'.format(destination),
            'collapseAccordian=is-hidden&',
            'singleSearch=true&',
            'destinationAddress.mainText={0}&'.format(destination),
            'isTransient=true&',
            'initialRequest=true&',
            'flexibleDateSearchRateDisplay=false&',
            'isSearch=true&',
            'isRateCalendar=false&',
            'destinationAddress.destination={0}&'.format(destination),
            'fromToDate={0}%2C+{1}+{2}%2C+{3}&'.format(day_of_week[check_out.weekday()], month_of_year[check_out.month], '%02d'%check_out.day, check_out.year),
            'fromToDate_submit={0}%2F{1}%2F{2}&'.format('%02d'%check_out.month, '%02d'%check_out.day, '%d'%check_out.year),
            'fromDate={0}%2F{1}%2F{2}&'.format('%02d'%check_in.month, '%02d'%check_in.day, '%d'%check_in.year),
            'toDate={0}%2F{1}%2F{2}&'.format('%02d'%check_out.month, '%02d'%check_out.day, '%d'%check_out.year),
            'lengthOfStay={0}&'.format(str(check_out.day - check_in.day)),
            'roomCountBox=1+Room&',
            'roomCount=1&',
            'guestCountBox=2+Adult+Per+Room&',
            'numAdultsPerRoom=2&',
            'childrenCountBox=0+Children+Per+Room&',
            'childrenCount=0&',
            'clusterCode=none&',
            'useRewardsPoints=true']
    hotel_search_url = ''.join(hotel_search_query_para)
    print(hotel_search_url)
    hotel_search_response = requests.get(hotel_search_url)
    print(hotel_search_response)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Add command-line arguments
    parser.add_argument('destination', help='Enter destination')
    parser.add_argument('check_in', help='Enter check-in date(YYYY/MM/DD)')
    parser.add_argument('check_out', help='Enter check-out date(YYYY/MM/DD)')
    args = parser.parse_args()
    # Extract arguments
    destination = args.destination
    check_in = datetime.strptime(args.check_in, "%Y/%m/%d")
    check_out = datetime.strptime(args.check_out, "%Y/%m/%d")
    today = datetime.now()
    # Compare today's date with both check-in and check-out dates
    if today < check_in and check_in < check_out:
        print("\nStarting award night crawling...\n")
        parse(destination, check_in, check_out)
    elif today > check_in or today > check_out:
        print("Please enter future check-in and check-out dates")
    elif check_in > check_out:
        print("Please enter a check-out date later than the check-in date")
