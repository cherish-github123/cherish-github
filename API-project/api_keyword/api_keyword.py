import requests
import pymysql
import json
import jsonpath
from config import *
import allure
from deepdiff import DeepDiff


class ApiKeys():
    # TODO 发送get请求
    @allure.step("测试步骤：发送get请求")
    def get(self, url, params=None, **kwargs):
        """
        :param url: 请求地址
        :param params:  get方法的参数，一般拼接在url后面
        :param kwargs: 其他参数
        :return: 返回响应数据
        """
        res = requests.get(url, params=params, **kwargs)
        return res

    # TODO 发送post请求
    @allure.step("测试步骤：发送post请求")
    def post(self, url, data=None, json=None, headers=None, **kwargs):
        """
        :param url: 请求地址
        :param data: 普通表单格式的参数放在data中
        :param json: json格式的参数放在json中
        :param kwargs: 其他参数
        :return:  返回响应数据
        """
        res = requests.post(url=url, data=data, json=json, headers=headers, **kwargs)
        return res

    # TODO 提取响应数据
    @allure.step("测试步骤：json path提取响应数据")
    def get_data(self, response, value):
        """
        :param reponse: 响应结果
        :param value: 要从响应结果中获取的数据，json path表达式
        :return: 返回获取的结果,因为获取到的数据类型是列表，故返回第一个值
        """
        if isinstance(response, str):
            # 判断如果传入的response是json格式的字符串：'{"name": "John", "age": 30, "city": "New York"}'，就转换为python对象（字典或者列表）
            response = json.loads(response)
            print(response)

        value_list = jsonpath.jsonpath(response, value)
        return value_list[0]


    # TODO 从数据库里面提取数据
    @allure.step("测试步骤：从数据库提取数据")
    def get_data_from_database(self, select_sql):
        """
        :param sql: sql语句
        :return: 返回sql语句查询结果
        """
        # todo 1 连接数据库
        connection = pymysql.Connection(
            host=DATABASE_HOST,  # 数据库地址，已在config.py文件中配置好的常量，可以直接导入使用
            port=DATABASE_PORT,  # 端口号
            user=DATABASE_USERNAME,  # 数据库用户名
            password=DATABASE_PASSWORD,  # 数据库密码
            db=DATABASE_NAME,  # 数据库名称
        )
        # todo 2 创建游标对象，使用游标对象操作数据库
        cursor = connection.cursor()
        # todo 3  编写sql语句
        sql = select_sql
        # todo 4  使用游标对象执行sql语句
        cursor.execute(sql)
        # todo 5 获取结果集
        result = cursor.fetchone()
        # todo 6 关闭游标对象
        cursor.close()
        # todo 7 关闭数据库连接对象
        connection.close()
        return result[0]  # 得到的数据是一个元组

    # TODO 数据对比
    @allure.step("测试步骤：响应数据全量对比")
    def jsondeepdiff(self, json1, json2, **other):
        """
        :param json1: 期望结果
        :param json2:  实际结果
        :param other:   对比规则,例如忽略规则：ignore_string_case=True,忽略大小写
        :return:  布尔值，如果对比一致，就返回一个空字典，不一致就返回不一致的内容
        """
        res = DeepDiff(json1, json2, **other)
        # 对比一致，则返回空字典
        if res == {}:
            return True
        else:
            return False


if __name__ == '__main__':
    apikey = ApiKeys()
    url = "http://shop-xo.hctestedu.com/?s=api/user/login"
    public_params = {"application": "app", "application_client_type": "weixin"}
    data = {"accounts": "tyl151006", "pwd": "123456", "type": "username"}
    # 发送请求，登录接口
    res = apikey.post(url=url, params=public_params, data=data)
    print(res.json())

    # 获取登录成功后的token
    token = apikey.get_data(res.json(), "$..token")
    print(token)

    # 从数据库中获取数据
    sql = "select username from sxo_user where username='tyl151006'"
    print(apikey.get_data_from_database(select_sql=sql))
