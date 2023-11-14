import json
import pandas as pd


def positive_sample():
    with open('ceshi_test_data/result_img_file.jsonl', mode='r+', encoding='utf-8') as f:
        data = f.readlines()

    for i in data:
        data_dict = eval(i)
        for key, val in data_dict.items():
            if '正' in key and val.get('conclusion') == '合规':
                with open('../../js_cl/res_bd_photo_filter_file.json', mode='a', encoding='utf-8') as res_positive_sample_no_voilat_file:
                    res_positive_sample_no_voilat_file.write(str({key: val})+'\n')


def negative_sample():
    with open('ceshi_test_data/result_img_file.jsonl', mode='r', encoding='utf-8') as f:
        data = f.readlines()

    for i in data:
        data_dict = eval(i)
        for key, val in data_dict.items():
            print(type(key), type(str(val)))
            print(key, str(val))
            break
        break
            # if '负' in key and val.get('conclusion') != '合规':
            #     with open('res_bd_photo_filter_file.json', mode='a+', encoding='utf-8') as res_negative_voilat_file:
            #         res_negative_voilat_file.write(str({key: val})+'\n')


def write_to_excel():
    with open('ceshi_test_data/result_img_file.jsonl', mode='r', encoding='utf-8') as f:
        data = f.readlines()
    data_dict_list = []
    for i in data:
        data_dict = eval(i)
        data_dict_list.append(data_dict)

    # pandas库储存数据到excel
    ids = []
    names = []
    prices = []
    for i in range(len(data_dict_list)):
        ids.append(data[i]["id"])
        names.append(data[i]["name"])
        prices.append(data[i]["price"])

    dfData = {  # 用字典设置DataFrame所需数据
        '序号': ids,
        '酒店': names,
        '价格': prices
    }
    df = pd.DataFrame(dfData)  # 创建DataFrame
    df.to_excel(fileName, index=False)  # 存表，去除原始索引列（0,1,2...）
#
"-------------数据用例-------------"
testData = [
    {"id": 1, "name": "立智", "price": 100},
    {"id": 2, "name": "维纳", "price": 200},
    {"id": 3, "name": "如家", "price": 300},
]
fileName = '测试2.xlsx'
#
#
#
#
if __name__ == '__main__':
#     positive_sample()
    # negative_sample()
    write_to_excel()













