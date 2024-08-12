import requests
from pprint import pprint
from bs4 import BeautifulSoup

URL = 'https://dhlottery.co.kr/common.do?method=main'

res = requests.get(URL)

soup = BeautifulSoup(res.text, 'html.parser')

# balls = soup.select('span.ball_645')
# for ball in balls:
#     print(ball.text)


# print(soup.select('span.bonus + span'))

# print(soup.select('a#numView > span'))

# print(soup.select('a[href*="/gameResult"]'))