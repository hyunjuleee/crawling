import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



current_folder = os.path.dirname(os.path.abspath(__file__))
# print(current_folder) = C:\Users\2-20\Desktop\DMF\crawling\2.dynamic

driver_path = os.path.join(current_folder, 'chromedriver.exe')

# print(driver_path) = C:\Users\2-20\Desktop\DMF\crawling\2.dynamic\chromedriver.exe

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
# driver.get('https://google.com')

URL = 'https://www.melon.com/chart/index.htm'

driver.get(URL)
# time.sleep(3)

song_info = driver.find_elements(By.CSS_SELECTOR, 'a.btn.button_icons.type03.song_info') # elements > 조건에 맞는 모든 결과, element > 조건에 맞는 제일 첫번째 결과

for i in range(5):
    song_info[i].click()
    # time.sleep(2)

    title = driver.find_element(By.CSS_SELECTOR, 'div.song_name').text
    print(title)

    song_meta = driver.find_element(By.CSS_SELECTOR,'dl.list')
    # print(song_info)
    for child in song_meta.find_elements(By.CSS_SELECTOR, 'dt, dd'):
        if child.tag_name == 'dt':
            print(child.text, end=':')
        else:
            print(child.text)

    like_cnt = driver.find_element(By.CSS_SELECTOR, 'span#d_like_count').text
    print(like_cnt)
    driver.back()