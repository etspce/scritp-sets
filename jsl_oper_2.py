import jsonlines


new_dev_all_text_list = []
with open('./2/new_dev_all.jsonl', 'r+', encoding='utf-8') as f_new_dev_all:
    for item_new_dev_all in jsonlines.Reader(f_new_dev_all):
        new_dev_all_text_list.append(item_new_dev_all["原文本"])
    # print(new_dev_all_text_list)
    # print(len(new_dev_all_text_list))

new_test_all_text_list = []
with open('./2/new_test_all.jsonl', 'r+', encoding='utf-8') as f_new_test_all:
    for item_new_test_all in jsonlines.Reader(f_new_test_all):
        new_test_all_text_list.append(item_new_test_all["原文本"])


new_train_all_text_list = []
with open('./2/new_train_all.jsonl', 'r+', encoding='utf-8') as f_new_train_all:
    for item_new_train_all in jsonlines.Reader(f_new_train_all):
        new_train_all_text_list.append(item_new_train_all["原文本"])


def check_repeat(check_item, ):
    count = 0
    data_text_list = []
    with open('./2/data.jsonl', 'r+', encoding='utf-8') as f_data:
        for item_data in jsonlines.Reader(f_data):
            data_text_list.append(item_data["原文本"])
        for i in check_item:
            if i in data_text_list:
                count += 1
        # print(len(data_text_list))
        print(count)


if __name__ == '__main__':
    check_repeat(new_dev_all_text_list) # new_dev_all
    check_repeat(new_test_all_text_list)
    check_repeat(new_train_all_text_list)











