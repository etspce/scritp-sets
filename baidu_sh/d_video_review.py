# encoding:utf-8
import pandas as pd
import requests


def main():
    """
    短视频审核接口
    """
    a = 0
    df_bwg_video = pd.read_excel('./baidu_bwg_wg.xlsx')
    url_bwg_video_list = list(df_bwg_video['url'].values)
    request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/video_censor/v2/user_defined"
    for i in url_bwg_video_list[90: len(url_bwg_video_list)]:
        video_name = i.split('/')[-1]
        ext_id = video_name.split('_')[0] + '_' + str(a)
        params = {"extId": ext_id, "name": video_name, "videoUrl": i}
        access_token = '24.61563c9c0010c163eaddccbef2cb6fc1.2592000.1690684951.282335-35500948'
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        a += 1
        if response:
            with open('ceshi_test_data/res_bwg_video_file.json', mode='a', encoding='utf-8') as f:
                f.write(str({video_name: response.json()})+'\n')


if __name__ == '__main__':
    main()
