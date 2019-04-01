"""
百度语音机器人
"""
import base64
from urllib import request, parse
import json
import requests
import os
import urllib


# 获取通行证token。
def get_token():
    client_id = 'cy57gvVAsEpxHpwtBB9zI9np'
    client_secret = 'T0QiUe8DGXUIS0mIABodTXGhVViTtGYr'

    login_data = parse.urlencode([
        ('grant_type', 'client_credentials'),
        ('client_id', client_id),
        ('client_secret', client_secret)
    ])

    req = request.Request('https://openapi.baidu.com/oauth/2.0/token')

    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        data = f.read().decode('utf-8')
        token = json.loads(data)['access_token']
        return token


# 获取语音数据speech
def get_base64_wav():
    path = 'D:\Python3Projects\TorndoServer3\scr\RESTTEST\\Microphone.wav'
    print(path)

    with open(path, 'rb') as f:
        wav = f.read()

        print('wav : ', type(wav))
        wav_base64 = base64.b64encode(wav).decode('utf-8')
        size = len(wav)
        f2 = open('D:\Python3Projects\TorndoServer3\scr\RESTTEST\\test.txt', 'w')
        f2.write(wav_base64)
        f2.close()

        return wav_base64, size


# 直接获得识别后的文字数据
def post_wav():
    token = get_token()
    speech, size = get_base64_wav()
    print('likai : ', size)
    dict_name_value_pairs = {
        'format': 'wav',
        'rate': 8000,
        'channel': 1,
        'cuid': 'yxh5274',
        'token': token,
        'speech': speech,
        'len': size,
        'lan': 'zh'
    }
    headers = {'Content-Type': 'application/json'}
    post_data = json.dumps(dict_name_value_pairs)

    url = 'http://vop.baidu.com/server_api'

    data = requests.post(url, data=post_data, headers=headers)

    print(data.text)
