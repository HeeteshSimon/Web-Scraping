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
print(items[0])