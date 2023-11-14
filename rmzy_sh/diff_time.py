#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/8/9 14:48
# @Author  : Xzx
# @FileName: diff_time.py
# @Software: PyCharm
import json
from datetime import datetime


def modify_review_time(file_name):
    with open('./'+file_name, mode='r', encoding='utf-8') as f:
        data_str = f.read()
        data_list = eval(data_str)
        for i in data_list:
            start_time = datetime.strptime(i.get('start_time'), "%d/%m/%Y %H:%M:%S")
            end_time = datetime.strptime(i.get('end_time'), "%d/%m/%Y %H:%M:%S")
            diff_time = (end_time - start_time).seconds
            print(i.get('review_time'))
            i['review_time'] = diff_time
            print(i.get('review_time'))
            print('>>>>>>>>>>>>>')
    new_data_str = str(data_list)
    with open('./new_'+file_name, mode='a', encoding='utf-8') as f_new:
        f_new.write(new_data_str)


if __name__ == '__main__':
    modify_review_time('res_video_time.json')
    modify_review_time('res_audio_time.json')
    modify_review_time('res_img_time.json')
    modify_review_time('res_txt_file_time.json')
