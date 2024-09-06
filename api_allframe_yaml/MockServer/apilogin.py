import requests

url = "http://127.0.0.1:8899/api/login"  # 启动flask服务后登录接口的url地址
data = {"username": "17812345678", "password": "123456"}
# response = requests.post(url=url, data=data)
response=requests.post(url=url, json=data)
print(response.text)