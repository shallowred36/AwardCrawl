import requests
from bs4 import BeautifulSoup

html_text = requests.get("https://www.marriott.com/default.mi").text
my_soup = BeautifulSoup(html_text, 'html.parser')
print(my_soup.prettify())
