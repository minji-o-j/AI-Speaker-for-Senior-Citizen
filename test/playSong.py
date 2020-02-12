from urllib.request import urlopen, Request
import urllib
import bs4
from bs4 import BeautifulSoup as bs
import requests
import re
import argparse, pafy, ffmpeg#, pyaudio

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

YOUTUBE_API_VERSION = 'v3'
YOUTUBE_API_SERVICE_NAME='youtube'
DEVELOPER_KEY=''

def youtube_search(options):
    try:
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

        parser = argparse.ArgumentParser()
        parser.add_argument('--q', help='Search term', default=options)
        parser.add_argument('--max-results', help='Max results', default=25)
        args = parser.parse_args()

        search_response = youtube.search().list(
            q=args.q,
            part='id,snippet',
            maxResults=args.max_results
        ).execute()

        videos = []
        url = []

        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                videos.append('%s (%s)' % (search_result['snippet']['title'],search_result['id']['videoId']))
                url.append(search_result['id']['videoId'])
        resultURL = "https://www.youtube.com/watch?v=" + url[0]
        print('url: '+resultURL)
        return resultURL
        

    except :
        print("Youtube Error")


#==============================================================================
text=input("")
text2=''
print('Recognized Text: '+text)

if text.find("틀어줘") >= 0 or text.find("들려줘") >=0 :

    if(text.find("노래 틀어줘")>=0):
        for i in range (0,text.find("노래 틀어줘")):
            text2+=text[i]
        print(text2)
        print(youtube_search(text2))
        
    elif(text.find("노래 들려줘")>=0):
        for i in range (0,text.find("노래 들려줘")):
            text2+=text[i]
        print(text2)
        print(youtube_search(text2))

    elif(text.find("틀어줘")>=0):
        for i in range (0,text.find("틀어줘")):
            text2+=text[i]
        print(text2)
        print(youtube_search(text2))

    elif(text.find("들려줘")>=0):
        for i in range (0,text.find("들려줘")):
            text2+=text[i]
        print(text2)
        print(youtube_search(text2))
    
else:
    print("정확한 명령어를 말해주세요")

        



    
