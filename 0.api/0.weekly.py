import os
import csv
import json
import requests
from dotenv import load_dotenv

load_dotenv()
KOBIS_API_KEY = os.getenv('KOBIS_API_KEY')
URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
WEEKLY_URL = f'{URL}?key={KOBIS_API_KEY}&targetDt=20240701'
# print(WEEKLY_URL)

res = requests.get(WEEKLY_URL)
data = res.json()

movie_list = data['boxOfficeResult']['weeklyBoxOfficeList']

movie_dict = {}

for movie in movie_list:
    movie_dict[movie['movieCd']] = {
        '영화명': movie['movieNm'],
        '누적관객수': movie['audiAcc'],
    }


# moive_dict를 ./data/weekly.json저장
output_dir = './data'
output_file = os.path.join(output_dir, 'weekly.json')

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(movie_dict, f, ensure_ascii=False)


# movie_dict를 ./data/weekly.csv저장
output_file = os.path.join(output_dir, 'weekly.csv')

with open(output_file, 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['대표코드', '영화명', '누적관객수'])
    for movie in movie_list:
        csv_writer.writerow([movie['movieCd'], movie['movieNm'], movie['audiAcc']])


