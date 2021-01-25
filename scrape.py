import requests
import csv
from bs4 import BeautifulSoup

import json
import datetime

url = ('https://leekduck.com/events/')
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data, 'html.parser')

h2 = soup.find_all('h2')
event_item_wrapper = soup.find_all("event-item-wrapper")

event_text = soup.find_all("event-text")

for i in event_text:
    children = i.findChildren("p", recursive=True)

    for child in children:
        item = child.text
        print(item)

print(soup.title.text)

# for el in h2:
#     print(el)
