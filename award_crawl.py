import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Obtain website from Chrome's webdriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"C:\Users\yaokuo\Documents\Personal - DO NOT BACKUP\Git\AwardCrawl\chromedriver_win32\chromedriver.exe")
driver.get("https://www.marriott.com/default.mi")
"""
try:
    loc = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "destinationAddress.destination")))
except:
    print("cannot find destination input")
"""
driver.implicitly_wait(3)

# Obtain field prefix
input_div = driver.find_element_by_css_selector(".tile-hsearch-homepage.m-homepage-hsearch.l-hsearch-2.l-hsearch-takeover.l-hsearch-cntnr.l-hsearch-bottom")
prefix = input_div.get_attribute("data-id-prefix")

# Obtain location field
loc_input_field_name = prefix + "_search-location"
loc_input_field = driver.find_element_by_id(loc_input_field_name)
loc_input_field.send_keys("Maldives")

# Obtain start date field
from_date_field_name = prefix + "_hotel-fromDate"
from_date_field = driver.find_element_by_id(from_date_field_name)
from_date_field.clear()
from_date_field.send_keys("Tue, Aug 6, 2019")

# Obtain end date field
to_date_field_name = prefix + "_hotel-toDate"
to_date_field = driver.find_element_by_id(to_date_field_name)
to_date_field.clear()
to_date_field.send_keys("Sun, Aug 11, 2019")

#driver.quit()
