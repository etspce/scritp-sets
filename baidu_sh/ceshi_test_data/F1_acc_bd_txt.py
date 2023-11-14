#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/25 9:45
# @Author  : Xzx
# @FileName: F1_acc_bd_txt.py
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


def f1_acc():
    tp, fn, tn, fp = 0, 0, 0, 0
    with open('./result_txt.json', mode='r', encoding='utf-8') as f:
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
    f1_acc()
