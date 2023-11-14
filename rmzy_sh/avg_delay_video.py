#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/8/9 14:38
# @Author  : Xzx
# @FileName: avg_delay_video.py
# @Software: PyCharm
from datetime import datetime


def get_repeat_res(old_file_path, new_file_path):
    cw_num = 0
    count = 0
    old_dataId_list = []
    with open('./'+old_file_path, mode='r', encoding='utf-8') as f1:
        data1 = f1.readlines()
        for i in data1:
            for key in eval(i):
                odl_dataId = eval(i).get(key).get('data').get('contentCheckTask').get('dataId')
                # print(ys_url)
                old_dataId_list.append(odl_dataId)
        # print(old_dataId_list)
    review_time_total = 0
    new_dataId_list = []
    with open('./'+new_file_path, mode='r', encoding='utf-8') as f:
        data = f.read()
        for j in eval(data):
            dataId = j.get('data_id')
            new_dataId_list.append(dataId)
        for k in old_dataId_list:
            if k in new_dataId_list:
                file_url = eval(data)[new_dataId_list.index(k)].get('file_url')
                start_time = datetime.strptime(eval(data)[new_dataId_list.index(k)].get('start_time'), "%d/%m/%Y %H:%M:%S")
                end_time = datetime.strptime(eval(data)[new_dataId_list.index(k)].get('end_time'), "%d/%m/%Y %H:%M:%S")
                diff_time = (end_time - start_time).seconds
                review_time_total += diff_time
                count += 1
        avg_delay = review_time_total / count
        print(f'avg_delay, {avg_delay}')
        print(f'cw_num, {cw_num}')
        print(f'count, {count}')


if __name__ == '__main__':
    get_repeat_res(old_file_path='res_video.json', new_file_path='res_video_time.json')