#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/24 16:06
# @Author  : Xzx
# @FileName: word_review_thread.py
# @Software: PyCharm
import os
from threading import Thread
import pandas as pd
import requests
import time


def main():
    """
    文本审核接口
    :return:
    """
    file_name = os.listdir('file_txt/wg_txt/')
    request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/text_censor/v2/user_defined"
    for i in file_name:
        f = open('./file_txt/wg_txt/'+i, mode='r', encoding='utf-8')
        content = f.readline()
        # params = {"text": "不要侮辱伟大的乐侃扒拉巴黎杀死他"}
        params = {"text": content}
        access_token = '24.462fba5e452d5fa5faeee22dc99bdc6b.2592000.1692170135.282335-36291522'
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.text)
        with open('result_txt_thread.json', mode='a', encoding='utf-8') as fi:
            fi.write(str({'wg_'+i: response.text})+'\n')
        time.sleep(1)


if __name__ == '__main__':
    main()