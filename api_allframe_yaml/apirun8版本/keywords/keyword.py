import jsonpath
import requests
import allure
from pymysql import cursors

from api_allframe_yaml.apirun8版本.Global_var.global_var import GlobalVar
import pymysql


class Keyword():
    @allure.step("发送get请求-------->")
    def request_get(self, **kwargs):
        response = requests.get(**kwargs)
        # 调用封装好的方法，将当前的响应数据存储到全局变量字典中，变量名为current_response
        GlobalVar().set_dict("current_response", response.json())

        return response

    @allure.step("发送post请求-------->")
    def request_post(self, **kwargs):
        response = requests.post(**kwargs)
        GlobalVar().set_dict("current_response", response.json())
        return response

    @allure.step("发送普通表单格式的pos请求--------->")
    def request_post_form_urlencoded(self, **kwargs):
        """
        思路：因为yaml文件里面的变量名是我们自己写的，所以需要将yaml文件里面的变量名转换为post请求需要的变量名才能发送请求
        :param kwargs:
        :return:
        """
        url = kwargs.get("url地址", None)
        params = kwargs.get("路径", None)
        headers = kwargs.get("headers", None)
        data = kwargs.get("参数", None)
        # 将转换为正常post请求的变量名后，进行参数打包，打包成字典
        request_data = {
            "url": url,
            "params": params,
            "headers": headers,
            "data": data}

        # 在发送请求时，进行拆包
        response = requests.post(**request_data)
        GlobalVar().set_dict("current_response", response.json())
        return response

    @allure.step("从响应中提取json数据并存储到全局变量------->")
    def ex_jsonData(self, **kwargs):
        """
        1.params:  提取的数据是？ 提取的数据是响应数据
        2.params:  jsonpath表达式？  expression 必传
        3.params:  提取的下标？, index默认为0
        4.params: 提取后保存到全局变量的变量名  var_name  必传
        :param kwargs:
        :return:
        """
        # TODO 1: 先从存储的全局变量字典中获取响应数据
        response = GlobalVar().get_dict("current_response")

        # TODO 2 :  提取数据的json path表达式,
        expression = kwargs.get("expression", None)  # kwargs是一个字典，通过get(key)方法获取对应的值，没有则返回None

        # TODO 3； 提取数据的下标
        index = kwargs.get("index", 0)
        # 如果index没有获取到显示为None,则给默认值为0
        if index is None:
            index = 0

        # TODO 4: 通过传入响应数据，jsonpath表达式，下标，提取数据
        ex_data = jsonpath.jsonpath(response, expression)[index]  # 实际从响应结果中提取的数据
        print("从全局变量提取的数据是：", ex_data)

        # TODO 5: 将提取的数据存储成对应变量到全局变量字典中
        GlobalVar().set_dict(kwargs["var_name"], ex_data)

        # print(GlobalVar().show_dict())
        return ex_data

    @allure.step("从数据库提取数据并存储到全局变量----->")
    def ex_databaseData(self,**kwargs):
        """
        :param kwargs: host  数据库地址
        :param kwargs: port  端口
        :param kwargs: user  数据库用户名
        :param kwargs:password  数据库密码
        :param kwargs: database 数据库名称
        :return:
        数据库连接步骤：
        1.导入pymysql
        2.创建数据库连接对象connection
        3.创建游标对象cursor
        4.执行sql语句，获取结果集result
        5.关闭游标对象cursor
        6.关闭数据库连接对象connection
        """
        connection = pymysql.connect(host="shop-xo.hctestedu.com",
                                     port=3306,
                                     user="api_test",
                                     password="Aa9999!",
                                     database="shopxo_hctested",
                                     cursorclass=cursors.DictCursor)   # 以字典格式返回数据

        cursor = connection.cursor()
        cursor.execute(kwargs["sql"])
        result = cursor.fetchall()
        print(result)
        cursor.close()
        connection.close()
        return result




    def

    @allure.step("断言处理：响应数据单个字段断言---------->")
    def assert_method(self, **kwargs):
        """
        :param kwargs: expectdata 期望结果
        :param kwargs: sjdata 实际结果
        :param kwargs: opr_type比较运算符  > < == !=
        :param kwargs:
        :return:
        """
        # 采用字典加匿名函数的方式，将期望结果与实际结果进行比较
        comparators = {
            # 定义字典的键和值，键是比较运算符，值就是执行操作
            ">": lambda a, b: a > b,
            "<": lambda a, b: a < b,
            "==": lambda a, b: a == b,
            "!=": lambda a, b: a != b,
            ">=": lambda a, b: a >= b,
            "<=": lambda a, b: a <= b,
        }
        if kwargs["opr_type"] != comparators:
            raise ValueError(f"没有该断言运算符方式：{kwargs['opr_type']}")

        # 调用断言方法
        if not comparators[kwargs["opr_type"]](kwargs["expectdata"], kwargs["sjdata"]):
            raise AssertionError(f"期望结果：{kwargs['expectdata']}与实际结果：{kwargs['sjdata']} 断言{kwargs['opr_type']}失败")







if __name__ == '__main__':
    keyword = Keyword()
    # keyword.database_dataextract("select id,username from sxo_user where username like 'hami%'")
    keyword.assert_method(expectdata=1,sjdata=1,opr_type="==")