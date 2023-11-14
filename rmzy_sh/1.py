#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 14:19
# @Author  : Xzx
# @FileName: 1.py
# @Software: PyCharm

with open('./res_video_time.json', mode='r') as f:
    data_str = f.read()
    data_list = eval(data_str)
    data_list[0]['review_time'] = 1
    print(data_list[0])
    print(data_list[0].get('review_time'))
    # print(type(data_list[0]))







