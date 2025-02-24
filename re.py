from wsgiref import headers
import re
import requests
import json
from pprint import pprint
def GetResponse(url):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
        "Referer":"https://www.bilibili.com/"
    }
    response=requests.get(url=url, headers=headers)
    return response
def GetInfo():
    name=input()
    link="https://www.bilibili.com/video/"+name+"/"
    response=GetResponse(link)
    html=response.text
    info=re.findall('<script>window.__playinfo__=(.*?)</script>',html)[0]
    #print(html)
    json_Data=json.loads(info)
    #pprint(json_Data)
    audiourl=json_Data['data']['dash']['audio'][0]['baseUrl']
    videourl = json_Data['data']['dash']['video'][0]['baseUrl']
    title=re.findall('"part":"(.*?)",',html)[0]
    #print(title)
    # print( audiourl)
    # print( videourl)
    return audiourl,videourl,title
def Save(title,audiourl,videourl):
    audio_content=GetResponse(url=audiourl).content
    video_content=GetResponse(url=videourl).content
    with open('video\\'+title+'.mp3', 'wb') as audio:
        audio.write(audio_content)
    with open('video\\'+title+'.mp4', 'wb') as video:
        video.write(video_content)
if __name__ == '__main__':
    audiourl,videourl,title=GetInfo()
    Save(title,audiourl,videourl)