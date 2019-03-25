"""
改脚本主要负责处理好友发送信息
"""
import itchat
from itchat.content import *
from ThuleanRoboot import *


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
