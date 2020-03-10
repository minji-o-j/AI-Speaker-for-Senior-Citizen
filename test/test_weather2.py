from urllib.request import urlopen, Request
import urllib
import bs4
from bs4 import BeautifulSoup as bs
import requests
import re

##페이지 정보 받아오기==============================================================
url1 = requests.get('https://search.naver.com/search.naver?query=날씨')
soup1 = bs(url1.text,'html.parser')
#data1 = soup1.find('div',{'class':'detail_box'})
data1=soup1.find('div',class_='detail_box')
data2 = data1.findAll('dd')
##==================================================================================
#온도
temp=soup1.find('p', class_='info_temperature').find('span', class_='todaytemp').text
#미세먼지
fine_dust=data2[0].find('span',class_='num').text
#초미세먼지
ultra_fine_dust = data2[1].find('span',class_='num').text
#지역
location=soup1.find('div',class_='select_box').find('span',class_='btn_select').text

##네이버에서 습도 받아오기====================================================================
humidity_loc=urllib.parse.quote(location+' 습도')
url2=requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query='+humidity_loc)
soup2=bs(url2.text,'html.parser')

#url2=requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=현재+습도')

#습도
PoP=soup2.find('div',class_='info_list humidity _tabContent').find('dd',class_='weather_item _dotWrapper').text
print(PoP)
##미세먼지 숫자로만==================================================================================
fine_dust_num=int(re.findall('\d+',fine_dust)[0])
ultra_fine_dust_num=int(re.findall('\d+',ultra_fine_dust)[0])

##출력==============================================================
print('현재 '+ location +' 날씨는 ' + temp + '도 입니다.')
print('현재 '+ location +' 미세먼지는 ' + fine_dust + '입니다.')
print('현재 '+ location +' 초미세먼지는 ' + ultra_fine_dust + '입니다.')
