# encoding:utf-8

import requests

'''
短视频审核接口
'''

request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/video_censor/v2/user_defined"

params = {"extId": "视频id", "name": "视频名称", "videoUrl": "视频url地址"}
access_token = '[调用鉴权接口获取的token]'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json())
