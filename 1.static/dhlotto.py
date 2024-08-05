import requests
from pprint import pprint
from bs4 import BeautifulSoup
URL = 'https://dhlottery.co.kr/common.do?method=main'

res = requests.get(URL)
# pip install beautifulsoup4
# res.text > html 코드
soup = BeautifulSoup(res.text, 'html.parser') # > python으로

balls = soup.select('span.ball_645')
for ball in balls:
    print(ball.text)

soup.select('span.bonus + span') # A + B: A 먼저 찾고, 그 안 형제 속성인 B를 찾음

soup.select('a#numView > span') # a 태그에 id가 numView 그 안에 자식

soup.select('a[href*="/gameResult"]') # a 태그 안에 herf속성에 /gameResult 문자가 포함된