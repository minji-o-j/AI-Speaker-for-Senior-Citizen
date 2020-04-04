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
 
 - 일반 AI 스피커와는 다르게 사용자가 있는 환경을 주기적으로 측정하여 온·습도의 개선을 돕는다.
 
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

- 폭염과 한파와 같은 상황에서 적절한 대처를 할 수 있어서 여름과 겨울을 안정적으로 보낼 수 있을 것으로 예상됨.
---
## 차별화된 점
#### 기존의 AI 스피커
![image](https://user-images.githubusercontent.com/45448731/78458001-55f81280-76e9-11ea-915b-1d16bafa6821.png)  
<br>

#### 우리의 스피커
![image](https://user-images.githubusercontent.com/45448731/78458003-57c1d600-76e9-11ea-9bd0-dd7b80ecf651.png)
<br>

- 기존의 AI 스피커의 기능 뿐 아니라 사용자가 찾지 않아도 __스스로 솔루션 제공__ 및 __사용자와 상호 소통 가능__  
<br>

---

## 사용 하드웨어
- 라즈베리파이 B  

- 소형 브레드보드

- DHT 22  
![image](https://user-images.githubusercontent.com/45448731/78458192-580ea100-76ea-11ea-8edb-4a465dfb2da3.png)  
  - 8자리 이상의 미세한 온도와 습도까지 측정이 가능. 
  
- KT AI Makers Kit

---
## 사용 프로그램
- python 3.8

- Thonny

- VNC Viewer  
  - 라즈베리파이를 연결하기 위해 VNC server의 IP address를 확인 한 후 노트북에서 VNC viewer를 실행하는 과정 필요

- AMK (KT에서 개발한 인공지능 시스템)  
![image](https://user-images.githubusercontent.com/45448731/78458570-55fa1180-76ed-11ea-97cf-a6214a699b67.png)  
> AMK의 작동 원리  
<br>

---
## 사용 기술
> ### 음성 분석/합성
![image](https://user-images.githubusercontent.com/45448731/78458237-c6ebfa00-76ea-11ea-8fdc-e9862c63adf1.png)
<br>

> ### 실내 온·습도 받아오기
1. DHT 22를 소형 브레드보드에 연결  

2. 온·습도를 받아오는 함수가 있는 곳에 `humidity, temperature = dht.read_retry (dht.DHT22, 4)`라는 코드를 작성  `<--DATA 연결하는 부분: GPIO 4번 핀`

3. 매우 자세하게 읽어줄 필요는 없기 때문에 소수점 첫째 자리까지 받아오도록 프로그래밍

<br>

> ### 웹 크롤링

![image](https://user-images.githubusercontent.com/45448731/78458882-c1dd7980-76ef-11ea-868b-9caf6ef576df.png)  
- 크롬에서 `개발자 도구`(F12)를 이용하면 페이지에 뜨는 정보에 대한 소스를 얻을 수 있다.
- 라즈베리파이는 GPS 기능이 없기 때문에 라즈베리파이가 연결된 __무선 인터넷__ 을 이용하여 사용자의 위치 정보를 알아내기로 하였다.
- `BeautifulSoup4` 패키지를 이용
- 같은 영역 안에 들어있는 내용은 `find()`가 아니라 __`findAll()` 함수를 이용__ 하여 __배열처럼 불러온다.__
  - cf. `find()`는 맨 위에 있는 것 하나만 반환한다.

<br>

---

## 알고리즘 
![image](https://user-images.githubusercontent.com/45448731/78459066-61e7d280-76f1-11ea-8291-c2a29c40acaa.png)  

- 솔루션 제공 순서는 `환경 개선 솔루션` -> `개인 솔루션`  

- 사용자는 스피커가 제공한 솔루션을 실행했음을 __버튼을 누름__ 으로써 스피커에게 알려준다.  

- `환경 개선 솔루션`을 실행했지만 환경의 개선이 되지 않은 경우 `개인 솔루션`을 제공한다.  
<br>  

> ### 계절 인식
- 현재 날짜를 받아와 여름 / 겨울 / 그외로 계절을 나눔

  - 이 기준을 정하기 위하여 24절기중 __하지(6/22)~처서(8/23)__ 를 여름으로, __소설(11/22)~경칩(3/6)__ 까지를 겨울로 설정.
  
  - 이 때 여름과 겨울은 '한여름', '한겨울'을 뜻하는 것으로, 폭염주의보나 한파주의보가 발생할만할 시기를 골라서 나눈 것.  
<br>  

> ### 온·습도 기준 설정
- 외부 온도를 고려하여 현재 온·습도의 높고 낮음을 판단하고자 함.

- 노인분들에게 권장하는 적정 실내 온도 (여름 26-28도, 겨울 22-26도)와 극단적 실내 온도(여름 33도 이상, 겨울 18도 이하)까지의 값 중 적절하다고 생각하는 값을 뽑아 이를 기준값으로 삼음.

- __여름 기준값: 30도__
  - 30도보다 같거나 높아지기 시작하면 솔루션 제공하기 시작함.
  
  - 사용자가 솔루션을 실천함으로써 실내온도가 극단적인 지점까지 올라가지 않도록 방지.
  
- __겨울 기준값: 22도__
  - 사용자가 '노인'이라는 점을 고려.
  
  - 노인분들은 추위에 노출되면 다른 나이대의 사람들보다 저체온증에 걸릴 위험이 더 높기 때문에 안전하게 _적정온도의 최솟값을 그대로 적용_.
<br>

> ### 외부와의 온습도 차이
- 여름에는 에어컨으로 인해 실내·외 온도 차가 발생하게 되는데, 이로 인해 우발성 저체온이나 냉방병과 같은 질환이 생길 수 있음.

- 따라서 __실내·외 온도 차가 8도__ 가 넘거나 __외부 습도가 내부 습도보다 높은__ 경우 __창문을 여는 솔루션을 제공하지 않도록 함__.

<br>

> ### 미세먼지와 초미세먼지 기준  
![image](https://user-images.githubusercontent.com/45448731/78458978-b179ce80-76f0-11ea-9a2e-e050bd663be7.png)  
- 이 중 __환경부에서 권고한 기준__ 에 따라 4단계로 분류.

- 미세먼지가 __나쁨__ 또는 __매우 나쁨__ 일 경우 __환기에 관한 솔루션을 제공하지 않음__.

<br>

> ### 사용자 피드백에 따른 솔루션 변화
![image](https://user-images.githubusercontent.com/45448731/78459611-28b16180-76f5-11ea-87c0-9b3d06948b23.png)  
- 솔루션 반복 시간 감소

- 4번까지 시도

- `환경 개선 솔루션`과 `개인 솔루션` 에 동일하게 적용. 
<br>

---

## 솔루션 List
- 솔루션 List의 이름이 실내와 실외 상황을 고려하여 선택됨.
- List 내에서 index를 이용해 `환경 개선 솔루션`과 `개인 솔루션`을 나누어 접근

```Py
##온도를 낮추는 솔루션

down_t = ["창문을 열어 환기를 시켜주세요",
          "선풍기를 집 밖을 향해서 틀어주세요",
          "커튼을 쳐주세요",
          "물을 마셔주세요",
          "따뜻한 물로 샤워해주세요"]  # 3 


##습도를 낮추는 솔루션

down_h = ["창문을 열어 환기를 시켜주세요",
          "제습기를 틀어주세요",
          "환풍기를 틀어주세요",
          "물을 마셔주세요"] # 3
  
  
##미세먼지를 고려했을 때 온도를 낮추는 솔루션

down_t_dust = ["선풍기를 집 밖을 향해서 틀어주세요",
               "커튼을 쳐주세요",
               "물을 마셔주세요",
               "따뜻한 물로 샤워해주세요"] # 2


## 미세먼지를 고려했을 때 습도를 낮추는 솔루션

down_h_dust = ["제습기를 틀어주세요",
              "환풍기를 틀어주세요",
              "물을 마셔주세요"]   # 2


##온도를 올리는 솔루션

up_t = ["난방을 틀어주세요.",
        "따뜻한 물로 샤워해주세요.",
        "따뜻한 물을 마셔주세요.",
        "내복을 입어주세요.",
        "양말을 신어주세요.",  
        "목에 손수건을 둘러주세요." ]   # 1
        
        
## 습도를 올리는 솔루션

up_h = ["가습기를 틀어주세요",
        "빨래나 물에 젖은 손수건을 널어주세요",
        "목에 손수건이 스카프를 둘러주세요",
        "물을 마셔주세요" ]   # 1

```
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
