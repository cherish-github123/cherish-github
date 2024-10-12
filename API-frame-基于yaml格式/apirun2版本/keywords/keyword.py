import requests
import allure


class Keyword:

    @allure.step("发送get请求-------->")
    def request_get(self, **kwargs):   # 参数为字典形式，**kwargs不定长参数
        response = requests.get(**kwargs)
        return response

    @allure.step("发送post请求-------->")
    def request_post(self, **kwargs):  # 参数为字典形式，不定长参数
        response = requests.post(**kwargs)
        return response
