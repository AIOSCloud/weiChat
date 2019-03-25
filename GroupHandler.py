# -*-coding:utf-8-*-
"""
主要负责处理群组信息
"""
import itchat
from itchat.content import *


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isGroupChat=True)
def text_reply(msg):
    msg.user.send('%s: %s' % (msg.type, msg.text))


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def download_files(msg):
    msg.download(msg.fileName, tmpdir="tmp/")
    typeSymbol = {
        PICTURE: 'Picture',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)
