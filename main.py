import requests
from bs4 import BeautifulSoup

link = str(input('paste steam link '))

r = requests.get(link)

soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='discount_final_price')

if s == None:
    s = soup.find('div', class_='game_purchase_price price')

s = s.prettify()

price = s.splitlines()[1]

print(price)