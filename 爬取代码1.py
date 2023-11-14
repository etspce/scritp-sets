import requests, json

session = requests.Session()
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'


def get_problem_by_slug(slug):
    url = "https://leetcode.com/graphql"
    params = {'operationName': "getQuestionDetail",
              'variables': {'titleSlug': slug},
              'query': '''query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                questionTitle
                questionTitleSlug
                content
                difficulty
                stats
                similarQuestions
                categoryTitle
                topicTags {
                        name
                        slug
                }
            }
        }'''
              }

    json_data = json.dumps(params).encode('utf8')

    headers = {'User-Agent': user_agent, 'Connection':
        'keep-alive', 'Content-Type': 'application/json',
               'Referer': 'https://leetcode.com/problems/' + slug}
    resp = session.post(url, data=json_data, headers=headers, timeout=10)
    content = resp.json()

    # 题目详细信息
    question = content['data']['question']
    print(question)