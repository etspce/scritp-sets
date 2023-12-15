# encoding:utf-8
import time

import requests
import base64
import os


def main():
    """
    图像审核接口
    """
    file_name_list = []
    sub_dir = ['AVdzzs', 'ys', 'xqgll', 'xxw', 'pfll']
    for sub_dir_data in sub_dir:
        for i, j, k, in os.walk('./derp20230625-sh/' + sub_dir_data + '/'):
            for sub_k_data in k:
                file_name_list.append(i + sub_k_data)
    request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/img_censor/v2/user_defined"
    # while 1:
    try:
        for file_name in file_name_list[4641: len(file_name_list)]:  # todo 待加90
            # 二进制方式打开图片文件
            f = open(file_name, 'rb')
            img = base64.b64encode(f.read())
            params = {"image": img}
            access_token = '24.462fba5e452d5fa5faeee22dc99bdc6b.2592000.1692170135.282335-36291522'
            request_url = request_url + "?access_token=" + access_token
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            response = requests.post(request_url, data=params, headers=headers)
            if response.json():
                # print(response.json())
                res_file_name = file_name.split('/')[1] + file_name.split('/')[2] + file_name.split('/')[3]
                with open('ceshi_test_data/result_img_file.jsonl', mode='a', encoding='utf-8') as fi:
                    fi.write(str({res_file_name: response.json()}) + '\n')
            else:
                print('审核结果不存在。。。。')
    except requests.exceptions.JSONDecodeError:
        print('我是')


if __name__ == '__main__':
    main()

# {'7二次元刀剑正样本0222.jpg': {'error_code': 2, 'error_msg': 'Service temporarily unavailable'}}
