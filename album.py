import requests
import json
from time import sleep

global al__name
global al_id
global al_mp3
global al_data

headers = {'Referer': 'http://music.163.com/',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36'
}

def music(album_id):
    global al_name
    global al_id
    global al_mp3
    global al_data
    al_name, al_id, al_mp3, al_data = [], [], [], []
    al_data = json.loads(requests.get('http://music.163.com/api/album/{}?ext=true&id={}&offset=0&total=true'.format(str(album_id), str(album_id))).text)['album']['songs']
    for i in al_data:
        al_name.append(i['name'])
        al_id.append(i['id'])
    for i in al_id:
        al_mp3.append(json.loads(requests.get('https://api.muxiaoguo.cn/api/163music?id={}'.format(i)).text)['data']['mp3url'])
    return al_mp3, al_name

def download(path):
    global al_mp3
    global al_name
    for i in range(len(al_mp3)):
        content = requests.get(url=al_mp3[i], headers=headers).content
        name = '{}/{}.mp3'.format(path, al_name[i])
        with open(name, 'wb') as f:
            f.write(content)
        #sleep(1.4)
