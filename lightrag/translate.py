# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import hashlib
import time
from importlib import reload

import time

reload(sys)

YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = '1dccd06ad455ac1e'
APP_SECRET = 'Z2Hx9TpwrBdu2auykuhw1F64IOW67oy9'


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def connect():
    q = "Hello World"

    data = {}
    data['from'] = 'auto'
    data['to'] = 'zh-CHS'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign
    data['vocabId'] = "您的用户词表ID"

    response = do_request(data)
    contentType = response.headers['Content-Type']
    if contentType == "audio/mp3":
        millis = int(round(time.time() * 1000))
        filePath = "合成的音频存储路径" + str(millis) + ".mp3"
        fo = open(filePath, 'wb')
        fo.write(response.content)
        fo.close()
    else:
        result = response.json()
        if result['errorCode'] == '0':
            translation = result['translation'][0]
            print(f"\n原文：{result['query']}")
            print(f"译文：{translation}")
            
            if 'webdict' in result:
                print(f"在线词典链接：{result['webdict']['url']}")
        else:
            print(f"翻译出错，错误代码：{result['errorCode']}")


def translate2zh(q:str) -> str:

    data = {}
    data['from'] = 'auto'
    data['to'] = 'zh-CHS'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign
    data['vocabId'] = "您的用户词表ID"

    response = do_request(data)
    contentType = response.headers['Content-Type']
    if contentType == "audio/mp3":
        millis = int(round(time.time() * 1000))
        filePath = "合成的音频存储路径" + str(millis) + ".mp3"
        fo = open(filePath, 'wb')
        fo.write(response.content)
        fo.close()
    else:
        result = response.json()
        if result['errorCode'] == '0':
            translation = result['translation'][0]
            print(f"\n原文：{result['query']}")
            print(f"译文：{translation}")
            return translation
            # if 'webdict' in result:
            #     print(f"在线词典链接：{result['webdict']['url']}")
        else:
            print(f"翻译出错，错误代码：{result['errorCode']}")  


if __name__ == '__main__':
    connect()