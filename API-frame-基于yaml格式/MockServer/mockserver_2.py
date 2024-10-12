"""
需要先安装flask  pip install flask
Flask是一个轻量级的python web框架，可以搭建web应用，它是一个类，需要创建一个对象
"""

from flask import Flask, request

app = Flask(__name__)


# TODO 模拟一个访问首页的接口
# 3.因为是模拟接口，所以需要接口url、请求方法、请求参数、返回值等信息，定义一个接口，用来返回网页首页

@app.route("/index")  # 默认是get请求,两种方式都是访问首页
def index():
    return "网页的首页"



# TODO 模拟一个登录接口

@app.route("/api/login", methods=["POST"])
def login():
    # res=request.get_data()    # 服务器这边可以拿到post方法在发送请求时的参数数据,data参数就使用get_data方法获取
    res=request.get_json()    # json格式传参的数据就使用get_json方法获取
    print(res)
    return '登录页面'


# 4.启动flask服务,启动显示服务的IP地址和端口+/index，直接在网页浏览即可
if __name__ == '__main__':
    app.run(debug=True, port=8899)
