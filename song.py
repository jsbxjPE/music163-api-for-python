import requests
import json
from time import sleep

global so_name
global so_mp3
so_name = []
so_mp3 = []

headers = {'Referer': 'http://music.163.com/',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36'
}

def music(song_id = []):
    global so_name
    global so_mp3
    so_name = []
    so_mp3 = []
    for i in song_id:
        so_mp3 = (json.loads(requests.get('https://api.muxiaoguo.cn/api/163music?id={}'.format(song_id)).text)['data']['mp3url'])
    return so_mp3, so_name

def download(path):
    global so_mp3
    global so_name
    for i in range(len(so_mp3)):
        content = requests.get(url=so_mp3[i], headers=headers).content
        name = '{}/{}.mp3'.format(path, so_name[i])
        with open(name, 'wb') as f:
            f.write(content)
        #sleep(1.4)
