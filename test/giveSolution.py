import random

'''
solutionList_env = ["창문을 열어 환기를 시켜주세요",
                 "제습기를 사용해보시는건 어떨까요?",
                 "난방을 틀어보세요",
                 "가습기를 사용해보세요",
                 "물이 젖은 수건을 실내에 걸어두시면 습도를 올리는데 도움이 됩니다.",
                 "환풍기를 사용해보세요",
                 "선풍기를 사용해보세요"
                 "커튼을 쳐보세요"]

solutionList_per = ["따뜻한 물을 마셔보세요",
                 "차가운 물을 마셔보세요",
                 "내복을 입어 체온을 따뜻하게 유지시켜주세요",
                 "목에 손수건을 둘러보세요",
                 "따뜻한 물로 샤워해보시는건 어떨까요?" ]
'''

down_t = ["창문을 열어 환기를 시켜주세요",
          "선풍기를 집 밖을 향해서 틀어주세요",
          "커튼을 쳐주세요",
          "물을 마셔주세요",
          "따뜻한 물로 샤워해주세요"]  # 3 

down_h = ["창문을 열어 환기를 시켜주세요",
          "제습기를 틀어주세요",
          "환풍기를 틀어주세요",
          "물을 마셔주세요"] # 3

down_t_dust = ["선풍기를 집 밖을 향해서 틀어주세요",
               "커튼을 쳐주세요",
               "물을 마셔주세요",
               "따뜻한 물로 샤워해주세요"] # 2


down_h_dust = ["제습기를 틀어주세요",
              "환풍기를 틀어주세요",
              "물을 마셔주세요"]   # 2

up_t = ["난방을 틀어주세요.",
        "따뜻한 물로 샤워해주세요.",
        "따뜻한 물을 마셔주세요.",
        "내복을 입어주세요.",
        "양말을 신어주세요.",  
        "목에 손수건을 둘러주세요." ]   # 1

up_h = ["가습기를 틀어주세요",
        "빨래나 물에 젖은 손수건을 널어주세요",
        "목에 손수건이 스카프를 둘러주세요,
        "물을 마셔주세요" ]   # 1



today_t = 0.0
today_h = 0.0
find_dust = 0.0
t = 0.0
h = 0.0
ans = ""


def giveSolution():

    if season == '여름':
        if today_t - t >= 8:
            print("현재 밖과의 온도차가 매우 큽니다.")
            print("에어컨이나 선풍기의 전원을 꺼주세요.")
        else:
            if t >= 30 and h >= 65:
                print("현재 온도는 높고 습도도 높습니다.")

                if find_dust >= 75 or today_h > h :
                    ans = down_t_dust[random.randrange(0,2)] + '그리고' + down_h_dust[random.randrange(0,2)]
                else:
                    ans = down_t[random.randrange(0,3)] + '그리고' + down_h[random.randrange(0,3)]

            elif t >= 30 and h <= 35:
                print("현재 온도는 높고 습도는 낮습니다.")
                ans = down_t[random.randrange(0,3)] + '그리고' + up_h[random.randrange(0,1)]
                
            elif t >= 30 and 35 < h < 65:
                print("현재 온도가 높습니다. ")
                 ans = down_t[random.randrange(0,3)]
                 
            elif t < 30 and h >= 65:
                print("현재 습도가 높습니다. ")
                if find_dust >= 75 or today_h > h :
                    ans = down_h_dust[random.randrange(0,2)]
                else:
                    ans = down_h[random.randrange(0,3)]

            elif t < 30 and h <= 35:
                print("현재 습도가 낮습니다. ")
                ans = up_h[random.randrange(0,1)]
                
            else:
                print("현재 온도와 습도가 모두 쾌적한 상태입니다, ")

    elif seasom == '겨울':
        if t <= 22 and h >= 65:
            print("현재 온도는 낮고 습도는 높습니다.")
            if find_dust >= 75 or today_h > h :
                ans = up_t[random.randrange(0,1)] + '그리고' + down_h_dust[random.randrange(0,2)]
            else:
                ans = up_t[random.randrange(0,1)] + '그리고' + down_h[random.randrange(0,3)]

        elif t <= 22 and h <= 35:
            print("현재 온도는 낮고 습도도 낮습니다.")
            ans = up_t[random.randrange(0,1)] + '그리고' + up_h[random.randrange(0,1)]

        elif t <= 22 and 35<h<65:
            print("현재 온도가 낮습니다.")
            ans = up_t[random.randrange(0,1)]

        elif t > 22 and h >= 65:
            print("현재 습도가 높습니다.")
            if find_dust >= 75 or today_h > h :
                ans = down_h_dust[random.randrange(0,2)]
            else:
                ans = down_h[random.randrange(0,3)]

        elif t > 22 and h <= 35:
            print("현재 습도가 낮습니다. "
            ans = up_h[random.randrange(0,1)]

        else:
            print("온도와 습도가 모두 쾌적한 상태입니다.")

    else:
        if today_t - t >= 8:
            print("현재 밖과의 온도 차이가 매우 큽니다.")
            print("에어컨이나 선풍기의 전원을 꺼주세요.")

        else:
            if 29 <= t and h >= 65:
                print("현재 온도가 높고 습도도 높습니다. ")
                if find_dust >= 75 or today_h > h :
                    ans = down_t_dust[random.randrange(0,2)] + '그리고' + down_h_dust[random.randrange(0,2)]
                else:
                    ans = down_t[random.randrange(0,3)] + '그리고' + down_h[random.randrange(0,3)]

            elif 29 <= t and h <= 35:
                print("현재 온도가 높고 습도는 낮습니다.")
                ans = down_t[random.randrange(0,3)] + '그리고' + up_h[random.randrange(0,1)]

            elif 22 >= t and h >= 65:
                print("현재 온도는 낮고 습도는 높습니다.")
                if find_dust >= 75 or today_h > h :
                    ans = up_t[random.randrange(0,1)] + '그리고' + down_h_dust[random.randrange(0,2)]
                else:
                    ans = up_t[random.randrange(0,1)] + '그리고' + down_h[random.randrange(0,3)]

            elif 22 >= t and h <= 35:
                print("현재 온도는 낮고 습도도 낮습니다.")
                ans = up_t[random.randrange(0,1)] + '그리고' + up_h[random.randrange(0,1)]

            elif 29 <= t and 35 < h < 65 :
                print("현재 온도가 높습니다.")
                ans = down_t[random.randrange(0,3)]

            elif 22 >= t and 35 < h < 65 :
                print("현재 온도가 낮습니다.")
                ans = up_t[random.randrange(0,1)]

            elif 22 < t < 29 and h >= 65 :
                print("현재 습도가 높습니다.")
                if find_dust >= 75 or today_h > h :
                    ans = down_h_dust[random.randrange(0,2)]
                else:
                    ans = down_h[random.randrange(0,3)]

            elif 22 < t < 29 and h <= 35 :
                print("현재 습도가 낮습니다.")
                ans = up_h[random.randrange(0,1)]

            else:
                print("현재 온도와 습도가 모두 쾌적한 상태입니다,")
                















            
            
