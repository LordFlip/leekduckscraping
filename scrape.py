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
div_event_text = soup.find_all('event-text')
print(soup.title.text)
# print(h2)

for el in div_event_text:
    print(el.text)