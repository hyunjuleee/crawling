from dotenv import load_dotenv

load_dotenv() # .env를 환경변수 공간에 load

import os

KOBIS_API_KEY = os.getenv('KOBIS_API_KEY') # 변수 가져오기 요청

URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'

WEEKLY_URL = f'{URL}?key={KOBIS_API_KEY}&targetDt=20240701'
#print(WEEKLY_URL)

import requests

res = requests.get(WEEKLY_URL)
data = res.json() # dict 형태로 변환

movie_list = data['boxOfficeResult']['weeklyBoxOfficeList']

movie_dict = {}

for movie in movie_list:
    movie_dict[movie['movieCd']] = {
        '영화명': movie['movieNm'],
        '누적관객수': movie['audiAcc'],
    }

# movie.dict를 ./data/weekly.json 저장
output_dir = './data'
output_file = os.path.join(output_dir, 'weekly.json') # = ./data/weekly.json

if not os.path.exists(output_dir): # output_dir 폴더가 없으면
    os.makedirs(output_dir) # 만들기

import json

with open(output_file, 'w', encoding='utf-8') as f: # f = open(output_file), with문이 닫힐 때까지 파일을 열고 있음?, write 형식으로 열기, 한글 encoding
    json.dump(movie_dict, f, ensure_ascii=False) # dict > json으로 바꾸기 & f에다가 넣기

# movie_dict를 ./data/weekly.csv 저장
output_file = os.path.join(output_dir, 'weekly.csv')

import csv

with open(output_file, 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['대표코드', '영화명', '누적관객수'])

    for movie in movie_list:
        csv_writer.writerow([movie['movieCd'], movie['movieNm'], movie['audiAcc']])