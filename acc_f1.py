# -*- coding: UTF-8 -*-
import json


def tp_fn():
    tp = 0
    fn = 0
    with open('./result_select_bwg_video.txt', 'r', encoding='utf-8') as f1:
        content = f1.read()
    # print(content)
    cont_list = content.split('\n')[:-1]
    print(len(cont_list))
    for cont in cont_list:
        jon_cont = json.loads(cont)
        file_name_cont = list(jon_cont.keys())[0]
        suggestion_cont = jon_cont[file_name_cont]["Suggestion"]
        # print(file_name_cont,suggestion_cont)
        if suggestion_cont == "Pass":
            tp += 1
        else:
            fn += 1
    print(tp, fn)
    return tp, fn


def tn_fp():
    with open("./result_select_short_wg_video2.txt", "r", encoding='utf-8') as f:
        con = f.read()
    con = con.split("\n")[:-1]
    # print(json.loads(con))
    tn = 0
    fp = 0
    for i in con:
        # print(i)
        json_con = json.loads(i)
        file_name = list(json_con.keys())[0]
        suggestion = json_con[file_name]["Suggestion"]
        if suggestion == "Pass":
            fp += 1
        else:
            tn += 1
    print(tn, fp)
    return tn, fp


def calculate_metrics(tp, tn, fp, fn):
    # 计算准确率
    accuracy = (tp + tn) / (tp + tn + fp + fn)

    # 计算精确率（P）
    precision = tp / (tp + fp)
    print('PPPPPP', precision)
    # 计算召回率（R）
    recall = tp / (tp + fn)
    print('RRRRR', recall)

    # 计算F1值
    f1_score = (2 * precision * recall) / (precision + recall)
    print(accuracy, f1_score)
    return accuracy, f1_score


# 腾讯违规检测的统计结果
# 视频
tp, fn = tp_fn()
tn, fp = tn_fp()
calculate_metrics(tp, tn, fp, fn)
