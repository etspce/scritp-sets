#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 14:09
# @Author  : Xzx
# @FileName: F1_acc.py
# @Software: PyCharm
def f1_acc(file_name: str):
    tp, fn, tn, fp = 0, 0, 0, 0
    with open('./'+file_name, mode='r', encoding='utf-8') as f:
        data = f.readlines()
        for dict_data in data:
            for i in eval(dict_data):
                if 'bwg' in i and eval(dict_data).get(i).get('data').get('contentCheckTask').get('checkResult') == 4:
                    # tp += 1
                    tn += 1
                elif 'bwg' in i and eval(dict_data).get(i).get('data').get('contentCheckTask').get('checkResult') != 4:
                    # fn += 1
                    fp += 1
                elif 'wg' in i and eval(dict_data).get(i).get('data').get('contentCheckTask').get('checkResult') != 2:
                    # fp += 1
                    fn += 1
                elif 'wg' in i and eval(dict_data).get(i).get('data').get('contentCheckTask').get('checkResult') == 2:
                    # tn += 1
                    tp += 1
    P = tp / (tp + fp)
    R = tp / (tp + fn)
    F1 = (2 * P * R) / (P + R)
    acc = (tp + tn) / len(data)
    print(f'tp:{tp}, fn:{fn}, fp:{fp}, tn:{tn}')
    print(f'P:{P}, R:{R}')
    print(f'F1为:{F1},acc为:{acc}')


if __name__ == '__main__':
    # f1_acc('res_img_new.json')
    # f1_acc('res_audio.json')
    f1_acc('res_video_1.json')
    # f1_acc('res_txt_cx.json')




