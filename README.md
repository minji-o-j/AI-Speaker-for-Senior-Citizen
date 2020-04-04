# AI Speaker for Senior Citizen
# (독거)노인들을 위한 AI 스피커
![images](https://img.shields.io/github/license/minji-o-j/AI-Speaker-for-Senior-Citizen?style=social)
![image](https://img.shields.io/badge/language-Python-blueviolet?style=social&logo=Python)
![image](https://img.shields.io/badge/Tool-n?style=social&logo=Raspberry-Pi)

[요약](#요약)  
[개발 기간](#개발-기간)  
[개발자](#개발자)  
[사용 하드웨어](#사용-하드웨어)  
[사용 프로그램](#사용-프로그램)  
[사용 기술](#사용-기술)  -[음성 분석/합성](#음성-분석합성), [웹 크롤링](#웹-크롤링) 
[참고 자료](#참고-자료)

---
## 요약
 - 독거노인을 위한 AI 스피커
 
 - 일반 AI 스피커와는 다르게 사용자가 있는 환경을 주기적으로 측정하여 온/습도의 개선을 돕는다.
 
 - 환경 개선을 돕는 솔루션과 개인 솔루션을 제공한다.
 
 - 그 외 대화 기능, 유튜브 노래 재생 기능 등이 가능하다.
 
 ---
## 개발 기간
- 2019/09/25 ~ 2019/12/05
---
## 개발자

- 윤대호([@DaeHoo-Yun @201810788](https://github.com/201810788)), 이혜인([@hyeinlee725](https://github.com/hyeinlee725)), 정민지([@minji-o-j](https://github.com/minji-o-j))
---
## 목적 및 필요성
![image](https://user-images.githubusercontent.com/45448731/78457876-68258100-76e8-11ea-926c-19ff1f53cff8.png)

- 노인들은 체온 조절이 원활하지 않아 __온열질환에 노출될 위험이 큼__

- 온·습도를 주기적으로 측정하여 적절한 온·습도 환경을 만드는 __환경 솔루션 및 개인 솔루션을 제공함__

- 폭염과 한파와 같은 상황에서 적절한 대처를 할 수 있어서 여름과 겨울을 안정적으로 보낼 수 있을 것으로 예상됨
---
## 차별화된 점
#### 기존의 AI 스피커
![image](https://user-images.githubusercontent.com/45448731/78458001-55f81280-76e9-11ea-915b-1d16bafa6821.png)  
<br>

#### 우리의 스피커
![image](https://user-images.githubusercontent.com/45448731/78458003-57c1d600-76e9-11ea-9bd0-dd7b80ecf651.png)
<br>

- 기존의 AI 스피커의 기능 뿐 아니라 사용자가 찾지 않아도 __스스로 솔루션 제공__ 및 __사용자와 상호 소통 가능__  

---

## 사용 하드웨어
- 라즈베리파이 B  

- 소형 브레드보드

- DHT 22  
![image](https://user-images.githubusercontent.com/45448731/78458192-580ea100-76ea-11ea-8edb-4a465dfb2da3.png)  
  - 8자리 이상의 미세한 온도와 습도까지 측정이 가능하다.  
  
- KT AI Makers Kit

---
## 사용 프로그램
- python 3.8

- Thonny

- VNC Viewer  
  - 라즈베리파이를 연결하기 위해 VNC server의 IP address를 확인 한 후 노트북에서 VNC viewer를 실행하는 과정 필요.

- AMK (KT에서 개발한 인공지능 시스템)
![image](https://user-images.githubusercontent.com/45448731/78458570-55fa1180-76ed-11ea-97cf-a6214a699b67.png)  
> AMK의 작동 원리  

---
## 사용 기술
### 음성 분석/합성
![image](https://user-images.githubusercontent.com/45448731/78458237-c6ebfa00-76ea-11ea-8fdc-e9862c63adf1.png)
<br>

### 실내 온·습도 받아오기
1. DHT 22를 소형 브레드보드에 연결  

2. DATA 연결하는 부분: GPIO 4번 핀

<br>

### 웹 크롤링
- 현재 위치/미세먼지/외부 온·습도 받아오기


---

## 알고리즘
---
## 참고 자료
#### 출처
> [clova 스피커 사진](https://clova.ai/ko/products/)   
> [픽토그램](https://www.flaticon.com/)  
> [내맘대로 AI 메이커스](http://miraes.co.kr/product/detail.html?product_no=16341&cate_no=226&display_group=1)  
> [구현 코드 출처](https://s3.ap-northeast-2.amazonaws.com/mechaimage/book/KT_AMK_Menual_Python.pdf)  
> [AMK 작동 원리](https://s3.ap-northeast-2.amazonaws.com/mechaimage/book/KT_AMK_Menual_Python.pdf)  
> [DHT 22](http://techshenzhen.com/goods/goods_view.php?goodsNo=1000000453&inflow=naver&NaPm=ct%3Dk32tfzi8%7Cci%3Ddf4e9237b4c1cee4c66d4f94904db3d41e6a4af8%7Ctr%3Dsls%7Csn%3D991855%7Chk%3D9212be6c4b097ae572428578578c19cb811acc43)  
> [미세먼지, 초미세먼지 분류표](http://ansan.ekfem.or.kr/archives/8912)  
<br>

#### 기준 참고
> [내 몸이 웃는 온도…내복 착용해 맞추세요](http://www.hani.co.kr/arti/society/health/462155.html)  
>[건강한 사람에게 적정 실내온도 20℃, 만성 질환자는?](http://health.chosun.com/site/data/html_dir/2011/01/28/2011012801574.html)  
>[여름 건강관리, 특히 신경써야 할 ‘고위험자’는?](http://www.samsunghospital.com/home/healthInfo/content/contenView.do?CONT_SRC_ID=29073&CONT_SRC=HOMEPAGE&CONT_ID=4582&CONT_CLS_CD=001027)  
>[습도 60% 넘으면 땀 잘 안 말라… 체온 조절 안 돼 열탈진](http://health.chosun.com/site/data/html_dir/2017/07/11/2017071102089.html)

----
