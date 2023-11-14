import jsonlines


def read_jsl(path1, path2, path3):
    i = 0
    data_list = []
    data_list_all = []
    path_list = [path1, path2, path3]
    while i < len(path_list):
        with open(path_list[i], 'r+', encoding='utf-8') as f_data:
            for item in jsonlines.Reader(f_data):
                data_list.append(item["原文本"])
        data_list_all.append(data_list)
        i += 1

    count_repeat = 0
    j = 0
    k = 0
    # while True:
    for item in data_list_all[k]:
        while j != len(data_list_all) - 1:
            if item in data_list_all[j+1]:
                count_repeat += 1
            j += 1
        k += 1
        j = k
    # for j in data_list1:
    #     if j in data_list3:
    #         print(count_repeat + 1, j)
    #         count_repeat += 1
    # print("test_data 与 dev 重复数：", count_repeat)
    # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # print(data_list)


def check_repeat(data_list1, data_list2, data_list3):
    count_repeat = 0
    for i in data_list1:
        if i in data_list3:
            print(count_repeat + 1, i)
            count_repeat += 1
    print("test_data 与 dev 重复数：", count_repeat)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    count_test_data_train_repeat = 0
    for j in data_list2:
        if j in data_list3:
            print(count_test_data_train_repeat + 1, j)
            count_test_data_train_repeat += 1
    print("test_data 与 train 重复数：", count_test_data_train_repeat)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    count_dev_train = 0
    for k in data_list1:
        if k in data_list2:
            print(count_dev_train + 1, k)
            count_dev_train += 1
    print("dev 与 train 重复数：", count_dev_train)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


if __name__ == '__main__':
    read_jsl('./remake/re_data1/new_dev_all.jsonl', './remake/re_data1/new_train_all.jsonl', './remake/re_data1/test_data.jsonl')
