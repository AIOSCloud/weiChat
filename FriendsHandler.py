"""
改脚本主要负责处理好友发送信息
"""
import itchat
from itchat.content import *
from ThuleanRoboot import *
import json


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isFriendChat=True)
def text_reply(msg):
    msg.user.send(get_response(msg))


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True)
def download_files(msg):
    msg.download(msg.fileName)
    if msg.type == PICTURE:
        # 如果用户发送的图片,解析图片中文字,然后定制化处理
        pass
    if msg.type == RECORDING:
        # 如果是录音,解析录音为文字,然后调用文字机器人组特殊化处理
        pass
    if msg.type == ATTACHMENT:
        # 如果是ATTACHMENT
        pass
    if msg.type == VIDEO:
        # 如果是视频
        pass
    typeSymbol = {
        PICTURE: 'Picture',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    msg.user.send('@%s@%s' % (typeSymbol, msg.fileName))


# 爬取好友信息
def get_friends():
    print("Hello word start")
    friends = itchat.get_friends(update=True)[:]
    total = len(friends[1:])
    male = 0
    female = 0
    for f in friends:
        male = male + 1
        female = female + 1
        print(f)
    print("男性好友:%.2f%%" % (float(male) / total * 100))
