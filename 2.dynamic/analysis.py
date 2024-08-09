import os
import numpy as np
import pandas as pd
from konlpy.tag import *
from kiwipiepy import Kiwi
from kiwipiepy.utils import Stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_excel('기후위기_20200701_to_20210630.xlsx')
df_title = df['title']
df_body = df['body']

hannanum = Hannanum()
kkma = Kkma()
komoran = Komoran()
okt = Okt()

test = okt.morphs(df_body[0])
print(test)