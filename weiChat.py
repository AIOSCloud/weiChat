"""
微信机器人聊天小程序
"""
from FriendsHandler import *

if __name__ == "__main__":
    """扫码登录微信"""
    itchat.auto_login(hotReload=True)
    itchat.run()
