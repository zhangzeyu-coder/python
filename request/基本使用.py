import requests

# 找到目标url
url = 'http://www.baidu.com'


# 发送请求
response=requests.get(url)
print(response)
# r = requests.post('http://httpbin.org/post', data = {'key':'value'})


# 传递URL参数
payload={'name':'zhangtong','age':'21'}
r = requests.get(url, params=payload)
print(r.url)

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get(url, params=payload)
print(r.url)
print()
