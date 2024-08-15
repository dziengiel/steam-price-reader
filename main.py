import requests
from bs4 import BeautifulSoup

r = requests.get('https://store.steampowered.com/app/1222680/Need_for_Speed_Heat/')


print(r)


soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='discount_final_price')