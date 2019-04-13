import time
import random
import requests
import json
settings = {
  'DINGDING_ROBOT_URL': 'https://oapi.dingtalk.com/robot/send?access_token=7a314f5a0c629c8aecf75308818041d3fc9bfe4733bf31e11f09450abc9c71b5',
  'BING_IMG': 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
}

def send_dingding_msg(text='', title=None, is_markdown=False):
    # DINGDING_ROBOT_URL
    res = requests.get(settings.BING_IMG)
    print(res)
    data = {
        "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {
            "isAtAll": True
        }
    }
    if is_markdown:
        data = {
            'msgtype': 'markdown',
            'markdown': {
                'title': title,
                'text': text.strip()
            },
            "at": {
                "isAtAll": True
            }
        }
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    # r = requests.post(settings.DINGDING_ROBOT_URL, headers=headers, data=json.dumps(data))