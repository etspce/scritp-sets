# encoding:utf-8
import time


import requests



def submit():
    """
    长视频审核接口
    """
    # param = "strategyId=" + "策略Id（可选）" + "&url=" + "待审核视频url（必填）"
    #                     + "&noticeUrl=" + "审核结论通知地址（必填有效地址）" + "&frequency=" + "抽帧频率（可选）"
    #                     +"&extId=" + "用户定义唯一标识（必填）"
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    params = {'url': 'http://localhost:8000/js_img/pic/0_1.mp4', 'extId': '0_1'}  #
    access_token = '24.588e32622bcbc06a317cd8df9bf6d44f.2592000.1688866159.282335-34584796'
    request_url = 'https://aip.baidubce.com/rest/2.0/solution/v1/video_censor/v1/video/submit'
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())


def recive():
    request_url = 'http://localhost:8000/'
    params = {'appId': '34584796', 'taskId': '16866238911714360', 'taskDuration': '90', 'extId': '0_1'}
    access_token = '24.588e32622bcbc06a317cd8df9bf6d44f.2592000.1688866159.282335-34584796'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    result = client.videoCensorPull(taskId, options)


def pull():
    # file_name = input('请输入要审核长视频的名称：')
    params = {'taskId': '16866238911714360'}
    access_token = '24.588e32622bcbc06a317cd8df9bf6d44f.2592000.1688866159.282335-34584796'
    request_url = 'https://aip.baidubce.com/rest/2.0/solution/v1/video_censor/v1/video/pull'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())

    # with open('result_'+file_name+'.json', mode='w', encoding='utf-8') as fi:
    #     fi.write(str({file_name: response.json()}))


if __name__ == '__main__':
    # submit()
    # recive()
    # time.sleep(30)
    pull()
