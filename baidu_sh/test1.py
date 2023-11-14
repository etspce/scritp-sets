tec_res_dic = {}
bd_res_dic = {}
same_list = []
file_name_list_all = []
with open('./ceshi_test_data/res_sbk_gx.json', mode='r', encoding='utf-8') as f_bd:
    data = f_bd.readlines()
    for i in data:
        for file_name in eval(i):
            res_review = eval(i).get(file_name).get('conclusion')
            if res_review == '不合规':
                bd_res_dic[file_name] = res_review
                # bd_res.append()
    # print(bd_res_dic)
    # print(len(bd_res_dic))


with open('./ceshi_test_data/res_img_ten_gx.json', mode='r', encoding='utf-8') as f_tec:
    data1 = f_tec.readlines()
    for j in data1:
        if 'null' in j:
            j = j.replace('null', 'None')
        for file_name1 in eval(j):
            res_review1 = eval(j).get(file_name1).get("Suggestion")
            if res_review1 == 'Block':
                tec_res_dic[file_name1] = res_review1
    # print(tec_res_dic)
    # print(len(tec_res_dic))

for same_name in bd_res_dic:
    if same_name in tec_res_dic:
        same_list.append(same_name)

# print(same_list)
for same_list_data in same_list:
    print(same_list_data)
    file_name_list = same_list_data.split('正样本')
    file_name_list_all.append(file_name_list)
# print(same_list)

# print(file_name_list_all)
# print(len(file_name_list_all))


for name_data in file_name_list_all:
    file_path = name_data[0]
    file_name_1 = name_data[1]
