import pandas as pd
import numpy as np

# 读取excel中70060的表
df_70060 = pd.read_excel(r'./原始数据for测试-V2.1.xlsx', sheet_name='70060')
# 获取70060表中去重用的imei
imei_70060_data = df_70060['imei2/用来双imei去重'].values[0]


def get_70059_brand_to_TAC_relat():
    TAC_to_trmnlBrand_dict = {}
    df_70059_data = pd.read_excel(r'./原始数据for测试-V2.1.xlsx', sheet_name='70059')
    TAC_data_list = list(df_70059_data['TAC'].values)
    trmnl_brand_data_list = list(df_70059_data['trmnl_brand'].values)
    for i in range(len(TAC_data_list)):
        TAC_to_trmnlBrand_dict[str(TAC_data_list[i])] = trmnl_brand_data_list[i]
    # print(TAC_to_trmnlBrand_dict)
    return TAC_to_trmnlBrand_dict


def get_remove_duplicates_excel():
    """
    分别获取三个70056去重后对应的表
    :return:
    """
    a = 0
    sheet_name_list = ['70056-第一批数据', '70056-第二批数据', '70056-第三批假数据']
    for sheet_name in sheet_name_list:
        df_70056_data = pd.read_excel(r'./原始数据for测试-V2.1.xlsx', sheet_name=sheet_name)
        #
        df = df_70056_data[~df_70056_data['imei/双imei去重用'].isin([imei_70060_data])]
        # print(df)
        a += 1
        df.to_excel('./remove_repeat_70056_' + str(a) + '.xlsx')


def get_remove_repeat_newent_1_num(a: int, prov: str):
    """
    获取去重表中 newent_imei_flag=1 各个品牌数量总和的函数
    月品牌新机用户数
    :return:
    """
    TAC_list = []
    # 读取去重表的 newent_imei_flag/是否换机用 字段
    df_70056_data = pd.read_excel(r'./remove_repeat_70056_' + str(a) + '.xlsx')
    newent_imei_flag_data = list(df_70056_data['newent_imei_flag/是否换机用'].values)
    TAC_all_data_list = list(df_70056_data['TAC/当前（换机后）tac,关联品牌和机型用'].values)
    df_70056_data_list_prov = list(df_70056_data['cmcc_prov_prvd_id/省份'].values)
    # 关系对应函数
    brand_name_to_TAC_dict = get_70059_brand_to_TAC_relat()

    # 获取去重表 newent_imei_flag=1 字段对应的 TAC 品牌名
    if prov == '全国':
        for ind, val in enumerate(newent_imei_flag_data):
            if val == 1:
                TAC_list.append(brand_name_to_TAC_dict.get(str(TAC_all_data_list[ind])))
    for index, value in enumerate(df_70056_data_list_prov):
        if value == prov and newent_imei_flag_data[index] == 1:
            TAC_list.append(brand_name_to_TAC_dict.get(str(TAC_all_data_list[index])))

    # 统计 各个品牌 的数量
    brand_count_dict = {}
    for j in TAC_list:
        if TAC_list.count(j) >= 1:
            brand_count_dict[j] = TAC_list.count(j)
    # print(brand_count_dict)
    return brand_count_dict


def get_brand_unchange_user_num(a: int):
    """
    获取当月该品牌换机后仍为该品牌的用户数
    :return:
    """
    # 读取去重后的excel表
    df_remove_repeat = pd.read_excel(r'./remove_repeat_70056_' + str(a) + '.xlsx')
    # 获取新excel里指定列['newent_imei_flag/是否换机用']['TAC']['TAC_ hj_bf/换机前的tac']的值
    newent_imei_flag_data = list(df_remove_repeat['newent_imei_flag/是否换机用'].values)
    TAC_list = list(df_remove_repeat['TAC/当前（换机后）tac,关联品牌和机型用'].values)
    TAC_hj_bf_list = list(df_remove_repeat['TAC_ hj_bf/换机前的tac'].values)
    TAC_to_brand_dict = get_70059_brand_to_TAC_relat()

    # TAC_ hj_bf=TAC 的总数量
    all_TAC_num_list = []
    for index, value in enumerate(newent_imei_flag_data):
        if value == 1 and TAC_to_brand_dict.get(str(TAC_list[index])) == TAC_to_brand_dict.get(
                str(TAC_hj_bf_list[index])):
            all_TAC_num_list.append(TAC_to_brand_dict.get(str(TAC_list[index])))

    per_brand_num = {}
    for i in all_TAC_num_list:
        if all_TAC_num_list.count(i) >= 1:
            per_brand_num[i] = all_TAC_num_list.count(i)
    # print(per_brand_num)
    return per_brand_num


def get_brand_out_user_num(a: int, prov: str):
    """
    月品牌流出用户数
    :return:
    """
    df_70056_data = pd.read_excel(r'./remove_repeat_70056_' + str(a) + '.xlsx')
    df_remove_repeat_TAC_hj_bf_list = list(df_70056_data['TAC_ hj_bf/换机前的tac'].values)
    df_remove_repeat_newent_imei_flag_list = list(df_70056_data['newent_imei_flag/是否换机用'].values)
    df_70056_data_list_prov = list(df_70056_data['cmcc_prov_prvd_id/省份'].values)
    # # 调用关系对应函数
    TAC_to_brand_dic = get_70059_brand_to_TAC_relat()

    TAC_hj_bf_newent_1_list = []
    out_user_num_dic = {}
    if prov == '全国':
        for ind, val in enumerate(df_remove_repeat_newent_imei_flag_list):
            if val != 0:
                TAC_hj_bf_newent_1_list.append(TAC_to_brand_dic.get(str(df_remove_repeat_TAC_hj_bf_list[ind])))
    for index, value in enumerate(df_70056_data_list_prov):
        if value == prov and df_remove_repeat_newent_imei_flag_list[index] != 0:
            TAC_hj_bf_newent_1_list.append(TAC_to_brand_dic.get(str(df_remove_repeat_TAC_hj_bf_list[index])))
    # 统计结果
    for i in TAC_hj_bf_newent_1_list:
        if TAC_hj_bf_newent_1_list.count(i) >= 1:
            out_user_num_dic[i] = TAC_hj_bf_newent_1_list.count(i)
    print(out_user_num_dic)
    return out_user_num_dic


def get_brand_in_user_num(a: int, prov: str):
    """
    月品牌流入用户数
    :return:
    """
    df_70056_data = pd.read_excel(r'./remove_repeat_70056_' + str(a) + '.xlsx')
    df_remove_repeat_TAC_list = list(df_70056_data['TAC/当前（换机后）tac,关联品牌和机型用'].values)
    df_remove_repeat_newent_imei_flag_list = list(df_70056_data['newent_imei_flag/是否换机用'].values)
    df_70056_data_list_prov = list(df_70056_data['cmcc_prov_prvd_id/省份'].values)
    # 调用关系对应函数
    TAC_to_brand_dic = get_70059_brand_to_TAC_relat()

    TAC_newent_1_list = []
    in_user_num_dic = {}
    if prov == '全国':
        for ind, val in enumerate(df_remove_repeat_newent_imei_flag_list):
            if val != 0:
                TAC_newent_1_list.append(TAC_to_brand_dic.get(str(df_remove_repeat_TAC_list[ind])))

    for index, value in enumerate(df_70056_data_list_prov):
        if value == prov and df_remove_repeat_newent_imei_flag_list[index] != 0:
            TAC_newent_1_list.append(TAC_to_brand_dic.get(str(df_remove_repeat_TAC_list[index])))
    # 统计结果
    for i in TAC_newent_1_list:
        if TAC_newent_1_list.count(i) >= 1:
            in_user_num_dic[i] = TAC_newent_1_list.count(i)
    # print(in_user_num_dic)
    return in_user_num_dic


def get_active_users(a: int, prov: str):
    """
    第一个指标：获取月品牌活跃用户数的函数
    :return:
    """
    df_70056_data_list_str = []

    # 读取去重表的TAC
    df_70056_data = pd.read_excel(r'./remove_repeat_70056_' + str(a) + '.xlsx')
    df_70056_data_list = list(df_70056_data['TAC/当前（换机后）tac,关联品牌和机型用'].values)
    df_70056_data_list_prov = list(df_70056_data['cmcc_prov_prvd_id/省份'].values)
    for num in df_70056_data_list:
        df_70056_data_list_str.append(str(num))

    # 调用关系对应函数
    brand_to_TAC_dict = get_70059_brand_to_TAC_relat()

    # 统计所有品牌的名称
    all_brand_name_list = []
    for i in df_70056_data_list_str:
        brand_name = brand_to_TAC_dict.get(i)
        all_brand_name_list.append(brand_name)
    # print(new_count_list)

    # 统计各个品牌的数量
    brand_name_list = []
    new_count_brand_num_dict = {}
    if prov == '全国':
        for j in all_brand_name_list:
            if all_brand_name_list.count(j) >= 1:
                new_count_brand_num_dict[j] = all_brand_name_list.count(j)
        return new_count_brand_num_dict
    for index, value in enumerate(df_70056_data_list_prov):
        if value == prov:
            brand_name_list.append(brand_to_TAC_dict.get(str(df_70056_data_list[index])))
    for i in brand_name_list:
        if brand_name_list.count(i) >= 1:
            new_count_brand_num_dict[i] = brand_name_list.count(i)
    return new_count_brand_num_dict


def get_percent(a: int, prov: str):
    """
    第二个指标获取月品牌新机活跃用户占比
    :return:
    """
    activ_dict = get_active_users(a, prov)
    brand_new_phone_num_dic = get_remove_repeat_newent_1_num(a, prov)
    perc_dic = {}
    # 获取公共key
    pub_key_list = activ_dict.keys()
    # 获取每一个表中对应的百分比
    for i in pub_key_list:
        perc = brand_new_phone_num_dic.get(i) / activ_dict.get(i)
        perc_dic[i] = perc
    return perc_dic


def get_brand_phone_loyal(a: int, prov='全国'):
    """
    第三个指标获取终端忠诚度
    :return:
    """
    brand_unchange_user_num_dic = get_brand_unchange_user_num(a)
    brand_out_user_num_dic = get_brand_out_user_num(a, prov)
    brand_loyal_dic = {}
    for i in brand_unchange_user_num_dic:
        brand_loyal_dic[i] = brand_unchange_user_num_dic.get(i) / brand_out_user_num_dic.get(i)
    print(brand_loyal_dic)
    return brand_loyal_dic


def brand_pure_in_user_num(a: int, prov: str):
    """
    第四个指标月品牌净流入用户数
    :return:
    """
    brand_in_user_num_dic = get_brand_in_user_num(a, prov)
    brand_out_user_num_dic = get_brand_out_user_num(a, prov)
    res_dic = {}
    for i in brand_in_user_num_dic:
        pure_in_user_num = brand_in_user_num_dic.get(
            i) - brand_out_user_num_dic.get(i)
        res_dic[i] = pure_in_user_num
    return res_dic


def brand_in_perc(a: int, prov: str):
    """
    第五个指标月品牌流入占比
    :return:
    """
    brand_in_user_num_dic = get_brand_in_user_num(a, prov)
    all_brand_in_user_num_dic = get_remove_repeat_newent_1_num(a, prov='全国')
    sum_brand = 0
    in_perc_dic = {}
    # 计算分母，月流入所有品牌总和
    for key, val in all_brand_in_user_num_dic.items():
        sum_brand += val

    # 计算百分比
    for i in brand_in_user_num_dic:
        in_prec = brand_in_user_num_dic.get(i) / sum_brand
        in_perc_dic[i] = in_prec
    print(in_perc_dic)
    return in_perc_dic


def cal_brand_score(a):
    activity_user_dict = get_active_users(a)  # 月品牌活跃用户数
    new_percent_dict = get_percent(a)  # 新机活跃数占比
    brand_loyal_dict = get_brand_phone_loyal(a)  # 品牌忠诚度
    brand_pure_in_dict = brand_pure_in_user_num(a)  # 月品牌净流入用户数
    brand_in_dict = brand_in_perc(a)  # 月品牌流入占比
    brand_list = activity_user_dict.keys()
    print("activity_user_dict", activity_user_dict)
    print("new_percent_dict", new_percent_dict)
    print("brand_loyal_dict", brand_loyal_dict)
    print("brand_pure_in_dict", brand_pure_in_dict)
    print("brand_in_dict", brand_in_dict)

    # 计算平均值
    average1 = np.mean(list(activity_user_dict.values()))  # 月品牌活跃用户数
    average2 = np.mean(list(new_percent_dict.values()))  # 新机活跃数占比
    average3 = np.mean(list(brand_loyal_dict.values()))  # 品牌忠诚度
    average4 = np.mean(list(brand_pure_in_dict.values()))  # 月品牌净流入用户数
    average5 = np.mean(list(brand_in_dict.values()))  # 月品牌流入占比

    # 计算方差
    len_brand = len(brand_list)
    sum_1 = sum_2 = sum_3 = sum_4 = sum_5 = 0
    for brand in brand_list:
        sum_1 += (activity_user_dict[brand] - average1) ** 2
        # variance_list.append(S2_1)
        sum_2 += (new_percent_dict[brand] - average2) ** 2
        # variance_list.append(S2_2)
        sum_3 += (brand_loyal_dict[brand] - average3) ** 2
        # variance_list.append(S2_3)
        sum_4 += (brand_pure_in_dict[brand] - average4) ** 2
        # variance_list.append(S2_4)
        sum_5 += (brand_in_dict[brand] - average5) ** 2
    S2_1 = (1 / len_brand) * sum_1  # 月品牌活跃用户数的方差
    S2_2 = (1 / len_brand) * sum_2  # 新机活跃数占比的方差
    S2_3 = (1 / len_brand) * sum_3  # 品牌忠诚度的方差
    S2_4 = (1 / len_brand) * sum_4  # 月品牌净流入用户数的方差
    S2_5 = (1 / len_brand) * sum_5  # 月品牌流入占比的方差

    # 计算指标折算分
    activity_user_conver = {}
    new_percent_conver = {}
    brand_loyal_conver = {}
    brand_pure_in_conver = {}
    brand_in_cover = {}
    for brand in brand_list:
        activity_user_conver[brand] = 80 + 10 * (activity_user_dict[brand] - average1) / S2_1
        # print("app_user_num_conver",app_user_num_conver)
        new_percent_conver[brand] = 80 + 10 * (new_percent_dict[brand] - average2) / S2_2
        brand_loyal_conver[brand] = 80 + 10 * (brand_loyal_dict[brand] - average3) / S2_3
        brand_pure_in_conver[brand] = 80 + 10 * (brand_pure_in_dict[brand] - average4) / S2_4
        brand_in_cover[brand] = 80 + 10 * (brand_in_dict[brand] - average5) / S2_5
    print("activity_user_conver", activity_user_conver)
    print("new_percent_conver", new_percent_conver)
    print("brand_loyal_conver", brand_loyal_conver)
    print("brand_pure_in_conver", brand_pure_in_conver)
    print("brand_in_cover", brand_in_cover)

    # 计算品牌分
    brand_market_month = {}
    for brand in brand_list:
        brand_market_month[brand] = activity_user_conver[brand] * 0.2 + new_percent_conver[brand] * 0.2 + \
                                    brand_loyal_conver[brand] * 0.2 + brand_pure_in_conver[brand] * 0.2 + \
                                    brand_in_cover[brand] * 0.2
    print("brand_market_month", brand_market_month)


if __name__ == '__main__':
    # print(get_active_users(2, '河北'))     # 第一个指标，获取月活跃用户数 已改
    # print(get_percent(2, '全国'))            # 第二个指标，月新机活跃用户占比
    # get_remove_repeat_newent_1_num(2)
    # get_brand_unchange_user_num(2)
    # get_brand_out_user_num(2)
    # get_brand_in_user_num(2)

    # get_brand_phone_loyal(2)                        # 第三个指标，终端忠诚度
    # print(brand_pure_in_user_num(2, '河北'))      # 第四个指标， 月净流入用户数
    brand_in_perc(2, '河北')                      # 第五个指标，月流入占比
    # brand_in_perc(2, '北京')                      # 第五个指标，月流入占比
    # brand_in_perc(2, '全国')                      # 第五个指标，月流入占比

    # all_in_perc_dic = brand_in_perc(2)
    # print(all_in_perc_dic)
    # new_percent_dict = get_percent(1)
    # print(new_percent_dict)
    # cal_brand_score(2)
    # print(get_brand_unchange_user_num(1))
