#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/26 16:16
# @Author  : Xzx
# @FileName: img_review_500.py
# @Software: PyCharm
import base64
import json
import os
import time

import requests
data_list = []
sub_dir = os.listdir('./第1批20230625-涉暴恐更新v1/')
for j in sub_dir:
    for i in os.listdir('./第1批20230625-涉暴恐更新v1/' + j + '/正样本/'):
        data_list.append('./第1批20230625-涉暴恐更新v1/' + j + '/正样本/'+i)
# print(len(data_list))
request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/img_censor/v2/user_defined"
for file_name in data_list[2575: len(data_list)]:  # todo 待加90
    # 二进制方式打开图片文件
    f = open(file_name, 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img}
    access_token = '24.462fba5e452d5fa5faeee22dc99bdc6b.2592000.1692170135.282335-36291522'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    time.sleep(1)
    if response.text:
        res_content = json.loads(str(response.text), strict=False)
        res_file_name = file_name.split('/')[-3]+file_name.split('/')[-2]+file_name.split('/')[-1]
        with open('ceshi_test_data/res_sbk_gx.json', mode='a', encoding='utf-8') as fi:
            fi.write(str({res_file_name: res_content}) + '\n')
    else:
        print('审核结果不存在。。。。')
