import pandas as pd


def get_70059_style_to_TAC_relat():
    TAC_to_trmnl_style_dict = {}
    df_70059_data = pd.read_excel(r'./原始数据for测试-V2.1.xlsx', sheet_name='70059')
    TAC_data_list = list(df_70059_data['TAC'].values)
    trmnl_style_data_list = list(df_70059_data['trmnl_style'].values)
    for i in range(len(TAC_data_list)):
        TAC_to_trmnl_style_dict[str(TAC_data_list[i])] = trmnl_style_data_list[i]
    return TAC_to_trmnl_style_dict


def get_uchge_tac_num(a):
    """
    获取不变用户数
    :return:
    """
    df_70056_data = pd.read_excel(r'./remove_repeat_70056_' + str(a) + '.xlsx')
    df_70056_data_tac_list = list(df_70056_data['TAC/当前（换机后）tac,关联品牌和机型用'].values)
    df_70056_data_tac_hj_bf_list = list(df_70056_data['TAC_ hj_bf/换机前的tac'].values)
    newent_imei_flag_data = list(df_70056_data['newent_imei_flag/是否换机用'].values)
    # 获取 newent_imei_flag字段为1，且TAC_ hj_bf=TAC的各机型对应的数量

    uchge_user_num_list = []
    for index, value in enumerate(newent_imei_flag_data):
        if value == 1 and df_70056_data_tac_list[index] == df_70056_data_tac_hj_bf_list[index]:
            uchge_user_num_list.append(str(df_70056_data_tac_list[index]))

    # 调用关系对应函数
    style_to_TAC_relat_dic = get_70059_style_to_TAC_relat()
    # 统计换机后仍为该机型的用户数量
    per_style_num = {}
    for i in uchge_user_num_list:
        if uchge_user_num_list.count(i) >= 1:
            per_style_num[style_to_TAC_relat_dic.get(i)] = uchge_user_num_list.count(i)
    # print(per_style_num)

    # 获取机型列表
    style_list = []
    for key, val in style_to_TAC_relat_dic.items():
        if val not in style_list:
            style_list.append(val)
    # print(style_list)

    # 换机后，机型改变的补零
    for j in style_list:
        if j not in per_style_num:
            per_style_num[j] = 0
    print(per_style_num)
    return per_style_num


def get_remove_repeat_newent_1_num(a):
    """
    获取去重表中 newent_imei_flag=1 各个机型数量总和的函数
    :return:
    """
    # 读取去重表的 newent_imei_flag/是否换机用 字段
    df_new_excel = pd.read_excel(r'./remove_repeat_70056_' + str(a) + '.xlsx')
    newent_imei_flag_data = list(df_new_excel['newent_imei_flag/是否换机用'].values)
    TAC_all_data_list = list(df_new_excel['TAC/当前（换机后）tac,关联品牌和机型用'].values)

    # 获取去重表 newent_imei_flag=1 字段对应的 TAC
    TAC_list = []
    for i in range(len(newent_imei_flag_data)):
        if newent_imei_flag_data[i] == 1:
            TAC_list.append(str(TAC_all_data_list[i]))
    # print(TAC_list)

    style_name_to_TAC_dict = get_70059_style_to_TAC_relat()

    # 统计 各个机型 的数量
    style_dic = {}
    for j in TAC_list:
        if style_name_to_TAC_dict.get(j) in style_dic:
            style_dic[style_name_to_TAC_dict.get(j)] += 1
        else:
            style_dic[style_name_to_TAC_dict.get(j)] = 1

    # print(style_dic)
    return style_dic


def get_tac_in_num(a: int, prov: str):
    """
    月机型流入用户数
    :return:
    """
    df_70056_data = pd.read_excel(r'./remove_repeat_70056_' + str(a) + '.xlsx')
    df_remove_repeat_TAC_list = list(df_70056_data['TAC/当前（换机后）tac,关联品牌和机型用'].values)
    df_remove_repeat_newent_imei_flag_list = list(df_70056_data['newent_imei_flag/是否换机用'].values)
    df_70056_data_list_prov = list(df_70056_data['cmcc_prov_prvd_id/省份'].values)
    # 调用关系对应函数
    rela_dic = get_70059_style_to_TAC_relat()

    # 统计newent不为0的机型
    TAC_newent_1_list = []
    if prov == '全国':
        for j in range(len(df_remove_repeat_newent_imei_flag_list)):
            if df_remove_repeat_newent_imei_flag_list[j] != 0:
                TAC_newent_1_list.append(rela_dic.get(str(df_remove_repeat_TAC_list[j])))
    for index, value in enumerate(df_70056_data_list_prov):
        if prov == value and df_remove_repeat_newent_imei_flag_list[index] != 0:
            TAC_newent_1_list.append(rela_dic.get(str(df_remove_repeat_TAC_list[index])))

    in_user_dic = {}
    for i in TAC_newent_1_list:
        if TAC_newent_1_list.count(i) >= 1:
            in_user_dic[i] = TAC_newent_1_list.count(i)
    # print(in_user_dic)
    return in_user_dic


def get_tac_out_num(a: int, prov: str):
    """
    月机型流出用户数
    :return:
    """
    df_70056_data = pd.read_excel(r'./remove_repeat_70056_' + str(a) + '.xlsx')
    df_remove_repeat_TAC_hj_bf_list = list(df_70056_data['TAC_ hj_bf/换机前的tac'].values)
    df_remove_repeat_newent_imei_flag_list = list(df_70056_data['newent_imei_flag/是否换机用'].values)
    df_70056_data_list_prov = list(df_70056_data['cmcc_prov_prvd_id/省份'].values)
    # 调用关系对应函数
    rela_dic = get_70059_style_to_TAC_relat()

    # 统计newent不为零的值
    TAC_newent_1_list = []
    if prov == '全国':
        for j in range(len(df_remove_repeat_newent_imei_flag_list)):
            if df_remove_repeat_newent_imei_flag_list[j] != 0:
                TAC_newent_1_list.append(rela_dic.get(str(df_remove_repeat_TAC_hj_bf_list[j])))
    for index, value in enumerate(df_70056_data_list_prov):
        if prov == value and df_remove_repeat_newent_imei_flag_list[index] != 0:
            TAC_newent_1_list.append(rela_dic.get(str(df_remove_repeat_TAC_hj_bf_list[index])))

    out_user_dic = {}
    for i in TAC_newent_1_list:
        if TAC_newent_1_list.count(i) >= 1:
            out_user_dic[i] = TAC_newent_1_list.count(i)
    # print(out_user_dic)
    return out_user_dic


def get_tac_activ_user_num(a: int, prov: str):
    """
    第一个指标月机型活跃用户数
    :return:
    """

    # 读取去重表的TAC
    df_70056_data = pd.read_excel(r'./remove_repeat_70056_' + str(a) + '.xlsx')
    df_70056_data_list = list(df_70056_data['TAC/当前（换机后）tac,关联品牌和机型用'].values)
    df_70056_data_list_prov = list(df_70056_data['cmcc_prov_prvd_id/省份'].values)
    df_70056_data_list_str = []
    tac_active_num_dic = {}

    # 调用对应关系函数
    rela_dic = get_70059_style_to_TAC_relat()
    if prov == '全国':
        for num in df_70056_data_list:
            df_70056_data_list_str.append(rela_dic.get(str(num)))
    for index, value in enumerate(df_70056_data_list_prov):
        if value == prov:
            df_70056_data_list_str.append(rela_dic.get(str(df_70056_data_list[index])))

    # 统计每个表对应机型的数量
    for i in df_70056_data_list_str:
        if df_70056_data_list_str.count(i) >= 1:
            tac_active_num_dic[i] = df_70056_data_list_str.count(i)
    # print(tac_active_num_dic)
    return tac_active_num_dic


def get_tac_perc(a):
    """
    # 第二个指标获取月机型新机活跃用户占比
    :return:
    """
    per_dic = {}
    tac_activ_user_num_dic = get_tac_activ_user_num(a, prov='全国')
    newent_1_num_dic = get_remove_repeat_newent_1_num(a)
    for i in tac_activ_user_num_dic:
        res_tac_per = newent_1_num_dic.get(i) / tac_activ_user_num_dic.get(i)
        per_dic[i] = res_tac_per
    print(per_dic)


def get_loyal(a):
    """
    第三个指标获取忠诚度
    :return:
    """
    tac_activ_user_num_dic = get_tac_activ_user_num(a, prov='全国')
    tac_out_num_dic = get_tac_out_num(a, prov='全国')
    style_loyal_dic = {}
    for i in tac_activ_user_num_dic:
        rat = tac_out_num_dic.get(i) / tac_activ_user_num_dic.get(i)
        style_loyal_dic[i] = 1 - rat
    print(style_loyal_dic)


def get_pure_in_user_num(a: int, prov: str):
    """
    第四个指标获取月机型净流入用户数
    :return:
    """
    tac_in_num_dic = get_tac_in_num(a, prov)
    tac_out_num_dic = get_tac_out_num(a, prov)
    res_dic = {}
    for i in tac_in_num_dic:
        pure_in_user_num = tac_in_num_dic.get(i) - tac_out_num_dic.get(i)
        res_dic[i] = pure_in_user_num
    print(res_dic)


def get_in_perc(a: int, prov: str):
    """
    第五个指标：获取月机型流入占比
    :return:
    """
    tac_in_user_dic = get_tac_in_num(a, prov)
    remove_repeat_newent_1_num_dic = get_remove_repeat_newent_1_num(a)
    in_perc_dic = {}
    sum_style = 0
    for j in remove_repeat_newent_1_num_dic:
        sum_style += remove_repeat_newent_1_num_dic.get(j)
    for i in tac_in_user_dic:
        in_prec = tac_in_user_dic.get(i) / sum_style
        in_perc_dic[i] = in_prec
    print(in_perc_dic)


if __name__ == '__main__':
    # get_70059_style_to_TAC_relat()

    # get_uchge_tac_num(2)
    # get_loyal(2)  # 第三个指标 机型忠诚度  # 已改对

    # get_tac_activ_user_num(2, '河北')         # 搞定,第一个指标 月活跃用户数        已改对
    get_tac_perc(2)                          # 搞定,第二个指标 月新机活跃用户占比   已改对
    # get_pure_in_user_num(2, '河北')                  # 搞定,第四个指标 月净流入用户数       已改对
    # get_in_perc(2, '河北')                           # 搞定,第五个指标 月流入占比          已改对
    # get_tac_in_num()                         # 已改对
    # get_tac_out_num()                        # 已改对
