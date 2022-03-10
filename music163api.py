import requests
import json
from time import sleep

global list_name
global list_id
global list_mp3
global list_data

headers = {'Referer': 'http://music.163.com/',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36'
}

def music_list(playlist_id):
    global list_name
    global list_id
    global list_mp3
    global list_data
    list_name = []
    list_id = []
    list_mp3 = []
    list_data = []
    list_data = json.loads(requests.get('https://music.163.com/api/playlist/detail?id={}'.format(str(playlist_id))).text)['result']['tracks']
    for i in list_data:
        list_name.append(i['name'])
        list_id.append(i['id'])
    for i in list_id:
        list_mp3.append(json.loads(requests.get('https://api.muxiaoguo.cn/api/163music?id={}'.format(i)).text)['data']['mp3url'])
    return list_mp3, list_name

def download(path):
    global list_mp3
    global list_name
    for i in range(len(list_mp3)):
        content = requests.get(url=list_mp3[i], headers=headers).content
        name = '{}/{}.mp3'.format(path, list_name[i])
        with open(name, 'wb') as f:
            f.write(content)
