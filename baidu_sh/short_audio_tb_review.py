# encoding:utf-8
import os
import requests
import base64


def main():
    """
    音频审核接口
    """
    file_name_list = []
    file_path = './audio/'
    for j in range(2):
        for i in range(len(os.listdir(file_path + os.listdir(file_path)[j]))):
            filePath = './audio/'
            a = os.listdir(filePath)
            filePath = filePath + a[j]
            a = os.listdir(filePath)
            filePath = filePath + '/' + a[i]
            file_name_list.append(filePath)
    # print(file_name_list)
    for file_name in file_name_list:
        request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/voice_censor/v3/user_defined"
        # 二进制方式打开音频文件
        f = open(file_name, 'rb')
        data = base64.b64encode(f.read())
        params = {"base64": data, "fmt": "m4a"}
        access_token = '24.462fba5e452d5fa5faeee22dc99bdc6b.2592000.1692170135.282335-36291522'
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        file_name_1 = file_name.split('/')[-1]
        with open('ceshi_test_data/result_short_audio.json', mode='a', encoding='utf-8') as fi:
            if file_name_list.index(file_name) <= 49:
                fi.write(str({'bwg_'+file_name_1: response.json()})+'\n')
            else:
                fi.write(str({'wg_' + file_name_1: response.json()}) + '\n')


if __name__ == '__main__':
    main()

