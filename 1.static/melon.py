import requests
from pprint import pprint
from bs4 import BeautifulSoup

URL = 'https://www.melon.com/chart/index.htm'

res = requests.get(URL)

soup = BeautifulSoup(res.text, 'html.parser')

print(soup)