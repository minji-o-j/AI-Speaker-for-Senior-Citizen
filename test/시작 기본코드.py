from __future__ import print_function

import ex1_kwstest as kws
import ex2_getVoice2Text as gv2t
import ex4_getText2VoiceStream as tts
import Adafruit_DHT as dht
import time
import MicrophoneStream as MS

def checkCommand(result):
    humidity, temperature = dht.read_retry(dht.DHT22, 4)
    text = result
    if text.find("온도 알려줘") >= 0:
        print("현재 온도는 {0:0.1f} 도 입니다 ".format(temperature))
        return("현재 온도는 {0:0.1f} 도 입니다ㅏ ".format(temperature))
    elif text.find("습도 알려줘") >= 0:
        print("현재 습도는 {0:0.1f} 퍼센트 입니다 ".format(humidity))
        return("현재 습도는 {0:0.1f} 퍼센트 입니다ㅏ. ".format(humidity))
    else:
        return("정확한 명령을 말해주세요요오~")

def main(): #Example7 KWS+STT
    KWSID = ['기가지니', '지니야', '친구야', '자기야']
    while 1:
        recog=kws.test(KWSID[0])
        if recog == 200:
            print('KWS Dectected …\n Start STT…')
            text = gv2t.getVoice2Text()
            print('Recognized Text: '+ text)
            tts.getText2VoiceStream(checkCommand(text), "result_TTS.wav")
            MS.play_file("result_TTS.wav")
            time.sleep(2)
        else:
            print('KWS Not Dectected …')
if __name__ == '__main__':
    main()
