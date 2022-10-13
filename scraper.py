# Import Python Packages
from bs4 import BeautifulSoup
import requests
import re

# Determine what product the user is looking for
product = input("What product would you like to search for? ").lower()
url = f'https://www.newegg.ca/p/pl?d={product}'

# Obtain HTML information from the URL
page_info = requests.get(url).text.lower()
soup = BeautifulSoup(page_info, "html.parser")
search_page = soup.find(class_='item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell')
search_items = search_page.find_all(text=re.compile(product)) 

# Obtain link and price for each product on the page
for items in search_items:
    items_parent = items.parent
    if items_parent.name != 'a':
        continue
    
    price_tag = items.find_parent(class_='item-container')
    price = price_tag.find(class_='price-current').strong.string
    link = items_parent['href']

    print(link, price)
