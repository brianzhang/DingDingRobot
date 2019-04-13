# -*- coding: utf-8 -*-
import sys
import socket
import time
import requests
import json

settings = {
  "DINGDING_ROBOT_URL": 'https://oapi.dingtalk.com/robot/send?access_token=7a314f5a0c629c8aecf75308818041d3fc9bfe4733bf31e11f09450abc9c71b5',
  "BING_IMG": 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
}


def send_dingding_msg(text='', title=None, is_markdown=False):
    # DINGDING_ROBOT_URL
    print(is_markdown)
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
    print(data)
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    r = requests.post(settings['DINGDING_ROBOT_URL'], headers=headers, data=json.dumps(data))

if __name__ == '__main__':
  res = requests.get(settings['BING_IMG']).json()
  
  img = 'http://s.cn.bing.net%s' % res['images'][0]['url']

  send_dingding_msg(u"""#### 任务进度关注 \n > 各位亲，下班时间快到了哦 \n\n > ![screenshot](%s)\n > ###### 快来更新一下 [redmine](http://redmine.oss.yunsom.cn/projects)的进度 \n""" % img, u'任务进度更新', True)
