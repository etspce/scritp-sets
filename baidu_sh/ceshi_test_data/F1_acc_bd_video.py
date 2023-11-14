#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/17 14:25
# @Author  : Xzx
# @FileName: F1_acc_bd_video.py
# @Software: PyCharm
"""
    计算公式
    1.acc=所有正确的/所有数据量
    2.F1=（2*p*r）/(p+r)，其中P=tp/(tp+fp)，R=tp/(tp+fn)
    TP(真正例)：预测正确，样本为正
    TN(真反例)：预测正确，样本为负
    FP(假正例)：预测错误，样本被预测为正，但样本实际为负
    FN(假反例)：预测错误，样本被预测为负，但样本实际为正
    正样本：违规
    负样本：不违规
    :return:
"""
def tec_F1_acc():
    tp = 0  # 真正例
    fn = 0  # 假反例
    fp = 0  # 假正例
    tn = 0  # 真反例
    with open('res_bwg_video_file.json', mode='r', encoding='utf-8') as f:
        f_data_list = f.read().split('\n')
        for i in f_data_list[0:-1]:
            i_dict = eval(i)
            # if 'null' in i:
            #     i_dict = eval(i.replace('null', 'None'))
            # for key in i_dict.keys():
            #     if i_dict.get(key).get('Suggestion') == 'Pass':
            #         tp += 1
            #     else:
            #         fn += 1
        # print('tp:', tp, 'fn:', fn)

    # with open('./ceshi_test_data/res_bwg_video_file.json', mode='r', encoding='utf-8') as f1:
    #     f1_data_list = f1.read().split('\n')
    #     for j in f1_data_list[:-1]:
    #         j_dict = eval(j)
    #         # if 'null' in j:
    #         #     j_dict = eval(j.replace('null', 'None'))
    #         for key in j_dict.keys():
    #             if j_dict.get(key).get('Suggestion') != 'Pass':
    #                 tn += 1
    #             else:
    #                 fp += 1
    #     print('tn:', tn, 'fp:', fp)

    # P = tp / (tp + fp)
    # R = tp / (tp + fn)
    # F1 = (2 * P * R) / (P + R)
    # acc = (tp + tn) / (tp + tn + fp + fn)
    # print('F1:', F1, 'acc:', acc)


def bd_F1_acc():
    tp, fn, fp, tn = 0, 0, 0, 0
    with open('res_bwg_video_file.json', mode='r', encoding='utf-8') as f:
        f_data_list = f.read().split('\n')[0:-1]
        for i in f_data_list:
            i_dict = eval(i)
            for key in i_dict:
                if i_dict.get(key).get('conclusion') == '合规':
                    # tp += 1
                    tn += 1
                else:
                    # fn += 1
                    fp += 1
        print('tn:', tn, 'fp:', fp)

    with open('res_wg_video_file.json', mode='r', encoding='utf-8') as f1:
        f1_data_list = f1.read().split('\n')[0:-1]
        for j in f1_data_list:
            j_dict = eval(j)
            for key in j_dict:
                if j_dict.get(key).get('conclusion') == '不合规':
                    # tn += 1
                    tp += 1
                else:
                    # fp += 1
                    fn += 1
        print('tp:', tp, 'fn:', fn)

    P = tp / (tp + fp)
    R = tp / (tp + fn)
    F1 = (2 * P * R) / (P + R)
    acc = (tp + tn) / (tp + tn + fp + fn)
    print(f'P:{P}, R:{R}')
    print('bd_F1:', F1, 'bd_acc:', acc)


def f1_acc(file_name):
    tp, fn, tn, fp = 0, 0, 0, 0
    with open('./'+file_name, mode='r', encoding='utf-8') as f:
        data = f.readlines()
        for dict_data in data:
            for i in eval(dict_data):
                if 'bwg' in i and eval(dict_data).get(i).get('conclusion') == '合规':
                    # tp += 1
                    tn += 1
                elif 'bwg' in i and eval(dict_data).get(i).get('conclusion') != '合规':
                    # fn += 1
                    fp += 1
                elif 'wg' in i and eval(dict_data).get(i).get('conclusion') != '不合规':
                    # fp += 1
                    fn += 1
                elif 'wg' in i and eval(dict_data).get(i).get('conclusion') == '不合规':
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
    bd_F1_acc()
    # f1_acc(file_name='res_bwg_video_file.json')


