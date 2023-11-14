import requests


def submit():
    """
    文档内容审核接口
    :return: None
    """
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    params = {"fileName": "test_word.txt"}
    request_url = 'https://aip.baidubce.com/rest/2.0/solution/v1/solution/document/v1/submit'
    access_token = '24.588e32622bcbc06a317cd8df9bf6d44f.2592000.1688866159.282335-34584796'
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(url=request_url, data=params, headers=headers)

    if response:
        print(response.json())


def pull():
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    params = {'taskId': '任务Id'}
    request_url = 'https://aip.baidubce.com/rest/2.0/solution/v1/solution/document/v1/pull'
    access_token = '24.588e32622bcbc06a317cd8df9bf6d44f.2592000.1688866159.282335-34584796'
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(url=request_url, data=params, headers=headers)

    if response:
        print(response.json())


if __name__ == '__main__':
    submit()
    pull()


