#import modules
import requests
from bs4 import BeautifulSoup
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=33.96746500000006&lon=-118.25679999999994#.Xpe2vsgzaMo')
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
print(soup.find_all('a'))