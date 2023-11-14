#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 15:14
# @Author  : Xzx
# @FileName: info.py
# @Software: PyCharm
import os
import time

import requests
import json
import pandas as pd
from threading import Thread

task_id_list = []
file_name_list = []

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjoie1widXNlcklkXCI6XCI4NFwiLFwidXNlcm5hbWVcIjpcImZhbnhpbnJ1XCJ9IiwiZXhwIjoxNjg5MjI4NzI0LCJqdGkiOiJjbm15UjZOb2JBIn0.xMqQjvIJtFoeSPqib77r2SWiwnxp662Rn1VcReCm4so'


def creatCheck(url_list):
    # print(f'>>>>>>>线程{name}，开始')
    a = 0
    for i in url_list:
        a += 1
        file_name = i.split('/')[-1]
        file_name_list.append(file_name)
        url_cre = 'http://10.33.28.103:41930/securityphone/contentcheck/createContentCheckTask'
        headers = {
            'Content-Type': 'application/json',
            'PMS-TOKEN': token,
        }
        params = {
            "taskName": "doc_review_" + str(a),
            "contentType": 4,  # 类型 1:图像  2:音频 3:视频 4:文本/文档
            "fileUrl": i,
            # "check_status": 0,
            "fileName": file_name
        }
        res_cre = requests.post(url=url_cre, data=json.dumps(params), headers=headers)
        task_id = dict(res_cre.json()).get('data').get('id')

        # 提交审核任务部分
        start = time.time()
        url_sub_c = 'http://10.33.28.103:41930/securityphone/contentcheck/submitCheck'
        params_id = {
            'id': task_id,
        }
        res_submit = requests.post(url=url_sub_c, headers=headers, data=json.dumps(params_id))
        # print('提交任务:', res_submit.json())
        end = time.time()
        if end - start >= 5:
            print(f'文挡审核失败。。时间超过{end - start}秒')
        with open('./taskId.json', mode='a', encoding='utf-8') as f:
            f.write(str(res_submit.json())+'\n')
        # time.sleep(120)


def get_task_check_info():
    # 获取结果部分
    with open('./taskId.json', mode='r', encoding='utf-8') as f1:
        data = f1.readlines()
        for index, taskId in enumerate(data):
            task_id = eval(taskId).get('id')
            headers = {
                'Content-Type': 'application/json',
                'PMS-TOKEN': token,
            }
            params_id = {
                'id': task_id,
            }
            url_info = 'http://10.33.28.103:41930/securityphone/contentcheck/getTaskCheckInfo'
            res = requests.post(url=url_info, headers=headers, data=json.dumps(params_id))
            print('获取结果:', res.json())
            with open('./res_txt.json', mode='a', encoding='utf-8') as f:
                if index <= 499:
                    f.write(str({'wg'+file_name_list[index]: res.json()}) + '\n')
                else:
                    f.write(str({'bwg'+file_name_list[index]: res.json()}) + '\n')
                # print(res.json())
            # print(f'>>>>>>>线程{name}，结束')


if __name__ == '__main__':
    """
    把并发的代码改一下，一秒钟发一个请求，一组10个，等待120秒再发下一组
    """
    df_data_list = list(pd.read_excel('./test_data/1100_txt_url_1.xlsx')['URL'].values)
    creatCheck(df_data_list)
    get_task_check_info()
