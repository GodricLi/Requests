# _*_ coding=utf-8 _*_


import requests

# res = requests.get('https://www.baidu.com')
# print(type(res))
# print(res.status_code)
# print(res.text)
# print(type(res.text))
# print(res.cookies)


# GET请求
# res = requests.get('https://httpbin.org/get')
# print(res.text)
# 带参数
# data = {
#     'name': 'rain',
#     'age': 22
# }
# res = requests.get('https://httpbin.org/get', params=data)
# print(res.text)
# 转成字典
# print(type(res.json()))

# 抓取网页，发现—知乎
import requests
import re

# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
# }
# res = requests.get('https://www.zhihu.com/explore', headers=headers)
# parse = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# text = re.findall(parse,res.text)
# print(text)


# 抓取二进制文件
# res = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico','wb') as f:
#     f.write(res.content)


# POST请求
# data = {
#     'name':'rain',
#     'age':'22'
# }
# res = requests.post('https://httpbin.org/post',data=data)
# print(res.text)

# 获取响应信息
# res = requests.get('http://www.baidu.com')
# print(type(res.status_code), res.status_code)   # 响应状态码
# print(type(res.headers), res.headers)           # 响应头信息
# print(type(res.cookies), res.cookies)           # Cookies信息
# print(type(res.url), res.url)                   # 请求url
# print(type(res.history), res.history)           # 请求历史信息


# requests内置状态码查询
res = requests.get('http://www.baidu.com')
exit() if not res.status_code == requests.codes.ok else print("Request Successful!")
