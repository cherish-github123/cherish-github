"""
需要先安装flask  pip install flask
Flask是一个轻量级的python web框架，可以搭建web应用，它是一个类，需要创建一个对象
"""

from flask import Flask


# 2，创建flask对象
app = Flask(__name__)  # __name__魔术方法，代表的就是当前这个文件的名字，将当前的文件当成一个服务


# 3.因为是模拟接口，所以需要接口url、请求方法、请求参数、返回值等信息，定义一个接口，用来返回网页首页
@app.route("/")
@app.route("/index")    # 默认不写请求方法时，是get请求,这两种方式都是访问首页
def index():
    return "这里是网页的首页"


# 4.启动flask服务,启动后，就会显示服务的IP地址和端口+/index，直接在网页浏览即可
if __name__ == '__main__':
    app.run(debug=True)