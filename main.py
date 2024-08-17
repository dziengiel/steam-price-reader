import requests
from bs4 import BeautifulSoup

link = str(input('paste steam link '))

r = requests.get(link)

soup = BeautifulSoup(r.content, 'html.parser')

name = soup.find('div', class_='apphub_AppName')

s = soup.find('div', class_='discount_final_price')

if s == None:
    s = soup.find('div', class_='game_purchase_price price')

s = s.prettify()

name = name.prettify()

name = name.splitlines()[1]

price = s.splitlines()[1]

print(f'Name: {name}\n'
      f'Price:{price}')