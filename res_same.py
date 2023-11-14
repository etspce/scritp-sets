#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/5 17:50
# @Author  : Xzx
# @FileName: res_same.py
# @Software: PyCharm
import pandas as pd


def get_bd_res():
    all_res_read_ele_dic = {}
    with open('./res_bd_photo_filter_file.json', mode='r', encoding='utf-8') as f_bd:
        res_read = f_bd.readlines()
        for res_read_ele in res_read:
            res_read_ele_dic = eval(res_read_ele)
            for key, val in res_read_ele_dic.items():
                all_res_read_ele_dic[key] = val
        # print(all_res_read_ele_dic)
        bd_img_name_list = []
        for i in all_res_read_ele_dic:
            bd_img_name_list.append(i)  # print(i) # 获取了百度的所有不一致的图片名称
        return bd_img_name_list, all_res_read_ele_dic


def get_tenc_res():
    all_res_read_ele_tenc_dic = {}
    with open('./res_tenc_photo_filter_file.jsonl', mode='r', encoding='utf-8') as f_tenc:
        res_read_tenc = f_tenc.readlines()
        for res_read_ele_tenc in res_read_tenc:
            res_read_ele_tenc_dic = eval(res_read_ele_tenc)
            for key, val in res_read_ele_tenc_dic.items():
                all_res_read_ele_tenc_dic[key] = val
        # print(all_res_read_ele_dic)
        tenc_img_name_list = []
        for i in all_res_read_ele_tenc_dic:
            tenc_img_name_list.append(i)  # print(i) # 获取了腾讯的所有不一致的图片名称
    return tenc_img_name_list, all_res_read_ele_tenc_dic


def get_same_res():
    same_list = []
    bd_list = get_bd_res()
    tenc_list = get_tenc_res()
    for i in bd_list[0]:
        if i in tenc_list[0]:
            same_list.append(i)
    # print(same_list)
    print(len(same_list))
    return same_list


def to_excel(file_name):
    same_bd = get_bd_res()
    same_tenc = get_tenc_res()
    same_res_list = get_same_res()
    write_Data = []
    for i in same_res_list:
        img_name = i
        bd_res = same_bd[1].get(i)
        tec_res = same_tenc[1].get(i)
        write_dic_ele = {"img_name": img_name, "bd_res": bd_res, "tec_res": tec_res}
        write_Data.append(write_dic_ele)

    img_name_s = []
    bd_res_s = []
    tec_res_s = []
    for j in range(len(write_Data)):
        img_name_s.append(write_Data[j]["img_name"])
        bd_res_s.append(write_Data[j]["bd_res"])
        tec_res_s.append(write_Data[j]["tec_res"])

    dfData = {  # 用字典设置DataFrame所需数据
        '图片名称': img_name_s,
        '百度结果': bd_res_s,
        '腾讯结果': tec_res_s
    }
    df = pd.DataFrame(dfData)  # 创建DataFrame
    df.to_excel(file_name, index=False)  # 存表，去除原始索引列（0,1,2...）


if __name__ == '__main__':
    # get_same_res()
    to_excel('same_res.xlsx')
