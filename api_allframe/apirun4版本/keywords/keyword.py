
import jsonpath
import requests
import allure
from day04.P01_pytest框架.apirun4版本.Global_context.global_context import GlobalContext

class Keyword():
    @allure.step("发送get请求-------->")
    def request_get(self, **kwargs):
        response = requests.get(**kwargs)
        # 调用封装好的方法，将当前的响应数据存储到全局变量字典中，变量名为current_response
        GlobalContext().set_dict("current_response", response.json())

        return response

    @allure.step("发送post请求-------->")
    def request_post(self, **kwargs):
        response = requests.post(**kwargs)
        GlobalContext().set_dict("current_response", response.json())
        return response

    @allure.step("提取json数据并存储到全局变量------->")
    def ex_jsonData(self, **kwargs):
        """
        1.params:  提取的数据是？ 提取的数据是响应数据
        2.params:  jsonpath表达式？  expression 必传
        3.params:  提取的下标？, index默认为0
        4.params: 提取后保存到全局变量的变量名  VAR_NAME  必传
        :param kwargs:
        :return:
        """
        # TODO 1: 先从存储的全局变量字典中获取响应数据
        response = GlobalContext().get_dict("current_response")

        # TODO 2 :  提取数据的json path表达式,
        expression = kwargs.get("expression", None)  # kwargs是一个字典，通过get(key)方法获取对应的值，没有则返回None

        # TODO 3； 提取数据的下标
        index = kwargs.get("index", 0)
        if index is None:
            index = 0
        ex_data = jsonpath.jsonpath(response, expression)[index]  # 实际从响应结果中提取的数据
        print("从全局变量提取的数据是：", ex_data)

        # TODO 4: 通过提取的数据存储成对应变量到全局变量字典中
        GlobalContext().set_dict(kwargs["var_name"], ex_data)

        print(GlobalContext().show_dict())
        return ex_data




if __name__ == '__main__':
    keywords = Keyword()
