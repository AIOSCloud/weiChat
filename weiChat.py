"""
微信机器人聊天小程序
"""
import requests
import itchat
import time
import random
import os

KEY = "b27f9fe757c84fdfae3864ad7b0f6215"


def get_response(msg):
    """获取机器人恢复消息"""
    apiUrl = "http://openapi.tuling123.com/openapi/api/v2"
    data = {
        "perception": {
            "inputText": {
                "text": msg
            }
        },
        "userInfo": {
            "apiKey": "b27f9fe757c84fdfae3864ad7b0f6215",
            "userId": "weichat"
        }
    }
    print(data)
    try:
        response = requests.post(apiUrl, json=data).json()
        print(response)
        print(response.get("results")[0].get("values").get("text"))
        return response.get("results")[0].get("values").get("text")
    except:
        return


# 文字处理
def text_reply(msg):
    print(msg)
    print(msg["Text"])
    defaultReply = "I received: " + msg["Text"]
    reply = get_response(msg["Text"])
    return reply or defaultReply


# 语音处理
def recording_reply(msg):
    # 保存MP3语音
    msg['Text'](msg['FileName'])
    # 时间戳
    timeData = str(time.time())
    # Nonce官网给的信息:随机正整数,与timestamp联合起来,用于防止重放攻击
    nonceData = int(random.random() * 10000)
    with open(msg["FileName"], 'rb') as f:
        # 读取mp3语音,获取byte数据,格式为b'\x..'
        voiceDta = f.read()
    # 删除MP3语音
    os.remove(msg["FileName"])
    # 读取base64编码之前的文件长度
    DataLenData = len(voiceDta)
    # time stamp
    tmp = int(timeData)
    pass


def system_reply(msg):
    print(msg)
    print(msg["Text"])
    pass


# 语音动恢复
@itchat.msg_register(itchat.content.INCOME_MSG)
def voice_reply(msg):
    if msg["Type"] == itchat.content.TEXT:
        # 文字和简单的表情处理
        text_reply(msg)
        pass
    if msg["Type"] == itchat.content.RECORDING:
        # 语音处理
        recording_reply(msg)
        pass
    if msg["Type"] == itchat.content.PICTURE:
        # 图片处理
        pass
    if msg["Type"] == itchat.content.MAP:
        # 地图处理
        pass
    if msg["Type"] == itchat.content.SYSTEM:
        system_reply(msg)


if __name__ == "__main__":
    """扫码登录微信"""
    itchat.auto_login(hotReload=True)
    itchat.run()
