import requests
import csv
from bs4 import BeautifulSoup

import json
import datetime

url = ('https://leekduck.com/events/')
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data, 'html.parser')


event_texts = soup.find_all("event-text")
event_text = soup.find("event-text")

#selector for the overall event tile
event_item_link = soup.find_all("event-item-link")

print(event_item_link)

containers = soup.find_all("div", {"class" : "event-text"})
counter = 1

for el in containers:
	title = el.findChildren("h2", recursive=False)
	date_time = el.findChildren("p", recursive=False)
	print(f'{counter}: ')
	for i in title:
		print(i.text)
		print(i.parent.name)
	# print(title)
	for i in date_time:
		print(i.text)
	# print(date_time)
	counter +=1
print('prop')