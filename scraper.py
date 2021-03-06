#import modules
import requests
import pandas as pd
from bs4 import BeautifulSoup
#To get the URL for scraping
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=43.1743&lon=-74.5125#.XpfFacgzaMo')
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
#print(items[0].find(class_='period-name').get_text())
#to get the short description of period
#print(items[0].find(class_='short-desc').get_text())
#to get the temp of that period
#print(items[0].find(class_='temp').get_text())
#Using list comprehension to get all the rest of the periods
period_names=[items.find(class_='period-name').get_text() for items in items]
#getting all the short desc
short_description=[items.find(class_='short-desc').get_text() for items in items]
#getting all the temp
temp=[items.find(class_='temp').get_text() for items in items]
#print It
#print(period_names)
#print(short_description)
#print(temp)
#Used pandas to print the data in Tabular form
weather = pd.DataFrame(
    {
        'Period':period_names,
        'Short_description':short_description,
        'Temperature':temp,
     })
print(weather)
#Extracted data is converted into a csv file
weather.to_csv('weather_report.csv')
