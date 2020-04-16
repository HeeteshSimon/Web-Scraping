#import modules
import requests
from bs4 import BeautifulSoup
#To get the URL for scraping
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=33.96746500000006&lon=-118.25679999999994#.Xpe2vsgzaMo')
#Parsing the source in html
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
#print(soup.find_all('a'))
week = soup.find(id="seven-day-forecast-body")
#print(week)
#print(soup.find_all('li'))
items = soup.find_all(class_='tombstone-container')
#print(items[0])
#to get the period name only we can use get_text() coz bs4 can detect it as object
print(items[0].find(class_='period-name').get_text())
#to get the short description of period
print(items[0].find(class_='short-desc').get_text())
#to get the temp of that period
print(items[0].find(class_='temp').get_text())
