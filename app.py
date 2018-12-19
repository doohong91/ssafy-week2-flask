from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup as bs
import time

app = Flask(__name__)

@app.route('/index')
def index():
    print('hi')
    print('welcome')
    return """
    <h1>슬픈 개구리</h1>
    <img src = "http://image.chosun.com/sitedata/image/201705/08/2017050801699_0.jpg">
    <h3>$5.0에 팝니다</h3>
    """
@app.route('/naver_toon') ## camel case(url, parameter 에서 주로 사용)
def naver_toon(): ## snake case
    
    today = time.strftime('%a').lower()
    url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=' + today
    responce = requests.get(url).text
    soup = bs(responce,'html.parser')
    toons = []
    li = soup.select('.img_list li')  
    url_base = 'https://comic.naver.com'
    
    for item in li:
      toon = {
        'title': item.select('dt a')[0]['title'],
        'url':url_base + item.select('dt a')[0]['href'],
        'img':item.select('.thumb img')[0]['src']
      }
      toons.append(toon)

    return render_template('naver_toon.html', t = toons)
    
@app.route('/daum_toon')
def daum_toon():
    
    today  = time.strftime('%a').lower()
    url = 'http://webtoon.daum.net/data/pc/webtoon/list_serialized/'+today+'?timeStamp=1545117020341'
    data = requests.get(url).json()['data']
    
    url_base = 'http://webtoon.daum.net/webtoon/view/'
    toons = []
    
    for i in range(len(data)):
      toon = {
        'title': data[i]['title'],
        'url': url_base + data[i]['nickname'],
        'img': data[i]['pcHomeImage']['url']
      }
      toons.append(toon)
      
    return render_template('daum_toon.html',t = toons)