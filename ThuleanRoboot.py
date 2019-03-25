"""
图灵机器人
"""
import requests

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
