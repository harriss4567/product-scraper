# Import Python Packages
from itertools import product
from bs4 import BeautifulSoup
import requests
import re

# Determine what product user is looking for 
product = print('What product would you like to search for? ')
url = f'https://www.newegg.ca/p/pl?d={product}'

# Obtain HTML information from the URL
page_info = requests.get(url).text
soup = BeautifulSoup(page_info, 'html_parser')
search_page = soup.find(class_='item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell')
search_items = search_page.find_all(text=re.compile(product))

