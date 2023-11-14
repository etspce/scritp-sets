#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/25 17:12
# @Author  : Xzx
# @FileName: res_data_to_excel.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import openpyxl as op
import pandas as pd


def pd_toExcel(data, fileName):  # pandas库储存数据到excel
    ids = []
    names = []
    res_conclusion = []
    for i in range(len(data)):
        ids.append(data[i]["id"])
        names.append(data[i]["file_name"])
        res_conclusion.append(data[i]["conclusion"])

    dfData = {  # 用字典设置DataFrame所需数据
        'id': ids,
        'file_name': names,
        'conclusion': res_conclusion
    }
    df = pd.DataFrame(dfData)  # 创建DataFrame
    df.to_excel(fileName, index=False)  # 存表，去除原始索引列（0,1,2...）


if __name__ == '__main__':
    fileName = 'bd_info_review_img.xlsx'
    write_data_dict = {}
    write_data = []
    num = 1
    with open('./res_img_1000.jsonl', mode='r', encoding='utf-8') as f:
        data = f.readlines()
    for i in data:
        for key, val in eval(i).items():
            write_data_dict['id'] = num
            write_data_dict['file_name'] = key
            write_data_dict['conclusion'] = val.get('conclusion')
            write_data.append(write_data_dict)
            num += 1
            write_data_dict = write_data_dict.copy()

    pd_toExcel(write_data, fileName)





















